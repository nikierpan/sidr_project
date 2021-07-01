from os import getenv
from pathlib import Path
from dotenv import load_dotenv
from flask_migrate import Migrate

from app import create_app, db
from app.models import User

BASE_DIR = Path(__file__).resolve().parent

dotenv_path = BASE_DIR.joinpath('.flaskenv')
if Path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = create_app(getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
