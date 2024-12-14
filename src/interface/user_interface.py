# from http import HTTPStatus
from fastapi import APIRouter
# from sqlalchemy.ext.asyncio import AsyncSession
# from src.infra.deps import get_session
# from src.domain.model.user_model import UserModel
# from dto.user_dto import UserResponseDTO

router = APIRouter()


@router.get('/')
async def get_user():
    return {'message': 'teste'}


# @router.post('/', status_code=HTTPStatus.CREATED, response_model=UserResponseDTO)
# async def post_user(user: UserModel, db: AsyncSession = Depends(get_session)):
#     new_user = UserModel(**user)
#     db.add(new_user)
#     await db.commit()
#     return new_user
