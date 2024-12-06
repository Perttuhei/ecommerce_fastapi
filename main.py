from flask.cli import load_dotenv

from controllers import users, products, categories

load_dotenv()
from fastapi import FastAPI
from fastapi_pagination import add_pagination

app = FastAPI()
# pagination https://www.workfall.com/learning/blog/how-to-implement-pagination-using-fastapi-in-python/
add_pagination(app)


app.include_router(users.router)
app.include_router(products.router)
app.include_router(categories.router)