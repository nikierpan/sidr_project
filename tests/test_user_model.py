import unittest
import time

from app.models import User
from app import db


class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password='test')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='test')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='test')
        self.assertTrue(u.verify_password('test'))
        self.assertFalse(u.verify_password('false'))

    def test_password_salts_are_random(self):
        u = User(password='test')
        u2 = User(password='test')
        self.assertTrue(u.password_hash != u2.password_hash)

    def test_valid_confirmation_token(self):
        u = User(password='cat')
        db.session.add(u)
        db.session.commit()
        token = u.generate_confirmation_token()
        self.assertTrue(u.confirm(token))
        db.session.delete(u)
        db.session.commit()

    def test_invalid_confirmation_token(self):
        u = User(password='cat')
        u2 = User(password='dog')
        db.session.add(u)
        db.session.add(u2)
        db.session.commit()
        token_u = u.generate_confirmation_token()
        self.assertFalse(u2.confirm(token_u))
        db.session.delete(u)
        db.session.delete(u2)
        db.session.commit()

    def test_expired_confirmation_token(self):
        u = User(password='cat')
        db.session.add(u)
        db.session.commit()
        token = u.generate_confirmation_token(expiration=1)
        time.sleep(2)
        self.assertFalse(u.confirm(token))
        db.session.delete(u)
        db.session.commit()