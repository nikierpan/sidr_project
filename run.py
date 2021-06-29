from os import getenv
from pathlib import Path
from dotenv import load_dotenv

from app import create_app

BASE_DIR = Path(__file__).resolve().parent

dotenv_path = BASE_DIR.joinpath('.flaskenv')
if Path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = create_app(getenv('FLASK_CONFIG') or 'default')
