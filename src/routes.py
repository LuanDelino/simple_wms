from fastapi import APIRouter
from interface.user_interface import router as user_router

api_router = APIRouter()

# ADD ROUTES
api_router.include_router(user_router, prefix='/users', tags=['cursos'])
