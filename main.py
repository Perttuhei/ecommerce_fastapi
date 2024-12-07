from flask.cli import load_dotenv
from controllers import products, categories, auth
from custom_exceptions.not_found_exception import NotFoundException
from custom_exceptions.unauthorized_exception import UnauthorizedException
from custom_exceptions.username_taken_exception import UsernameTakenException

load_dotenv()
from fastapi import FastAPI, HTTPException
from fastapi_pagination import add_pagination

app = FastAPI()
# pagination https://www.workfall.com/learning/blog/how-to-implement-pagination-using-fastapi-in-python/
add_pagination(app)


app.include_router(auth.router)
app.include_router(products.router)
app.include_router(categories.router)

@app.exception_handler(NotFoundException)
async def not_found(request, exc):
    raise HTTPException(status_code=404, detail=str(exc))

@app.exception_handler(UsernameTakenException)
async def username_taken_exception(request, exc):
    raise HTTPException(status_code=400, detail=str(exc))

@app.exception_handler(UnauthorizedException)
async def unauthorized_exception(request, exc):
    raise HTTPException(detail=str(exc), status_code=401)
