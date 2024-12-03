from flask.cli import load_dotenv

load_dotenv()
from fastapi import FastAPI

app = FastAPI()