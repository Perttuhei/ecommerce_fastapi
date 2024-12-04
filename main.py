from flask.cli import load_dotenv

from controllers import users, products

load_dotenv()
from fastapi import FastAPI

app = FastAPI()

app.include_router(users.router)
app.include_router(products.router)