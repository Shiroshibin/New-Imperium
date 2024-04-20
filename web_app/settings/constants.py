import os
from dotenv import load_dotenv
from pathlib import Path

from flask import Flask
from sqlalchemy import create_engine


load_dotenv()


BASEDIR = Path(__file__).parent.parent

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DB_PORT = os.getenv("DB_PORT")
DB_HOST = os.getenv("DB_HOST")

# создаем движок SqlAlchemy
ENGINE = create_engine(f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

app = Flask(__name__, template_folder=f'{BASEDIR}/templates', static_folder=f'{BASEDIR}/static')
