from fastapi import APIRouter, Body, Depends
from starlette.responses import JSONResponse

from app.core.database import user_collection
from app.domain.user import UserApiScheme
from app.repository.user import UserRepository
from app.service.user import UserService

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


def get_user_service() -> UserService:
    user_repository = UserRepository(user_collection)
    return UserService(user_repository)


@router.post("/registration", status_code=201)
async def registration_view(
    user_service: UserService = Depends(get_user_service),
    user: UserApiScheme = Body(...)
) -> JSONResponse:
    if await user_service.registration(user):
        return JSONResponse(status_code=201, content={"success": True})
    else:
        return JSONResponse(status_code=400, content={"success": False})


@router.post("/login", status_code=200)
async def login_view(
    user_service: UserService = Depends(get_user_service),
    user: UserApiScheme = Body(...)
) -> JSONResponse:
    if await user_service.login(user):
        return JSONResponse(status_code=200, content={"success": True})
    else:
        return JSONResponse(status_code=400, content={"success": False})
