from flask.cli import load_dotenv
from controllers import products, categories, auth, cart, order, account
from custom_exceptions.category_exist_exception import CategoryExistsException
from custom_exceptions.forbidden_exception import ForbiddenException
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
app.include_router(cart.router)
app.include_router(order.router)
app.include_router(account.router)

@app.exception_handler(NotFoundException)
async def not_found(request, exc):
    raise HTTPException(status_code=404, detail=str(exc))

@app.exception_handler(UsernameTakenException)
async def username_taken_exception(request, exc):
    raise HTTPException(status_code=400, detail=str(exc))

@app.exception_handler(UnauthorizedException)
async def unauthorized_exception(request, exc):
    raise HTTPException(detail=str(exc), status_code=401)

@app.exception_handler(ForbiddenException)
async def forbidden_exception(request, exc):
    raise HTTPException(detail=str(exc), status_code=403)
@app.exception_handler(CategoryExistsException)
async def category_exists_exception(request, exc):
    raise HTTPException(status_code=400, detail=str(exc))

