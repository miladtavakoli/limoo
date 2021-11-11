import os
from os.path import join, dirname
from dotenv import load_dotenv


def get_env(var):
    return os.environ[var]


file_path = join(dirname(__file__), '.env')

dotenv_path = join(file_path)
if os.path.isfile(file_path):
    load_dotenv(file_path)

SECRET_KEY = os.getenv("MY_SECRET")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ACCESS_TOKEN_EXPIRED = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRED"))
JWT_REFRESH_TOKEN_EXPIRED = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRED"))

SQL_URL = os.getenv("SQL_URL")
SQL_USERNAME = os.getenv("SQL_USERNAME")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")
SQL_DATABASE = os.getenv("SQL_DATABASE")
