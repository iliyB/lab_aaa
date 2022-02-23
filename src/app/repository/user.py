from typing import Optional

from fastapi.encoders import jsonable_encoder
from pymongo.collection import Collection

from app.domain.user import UserScheme


class UserRepository:
    def __init__(self, collection: Collection) -> None:
        self.collection = collection

    async def create_user(self, user: UserScheme) -> bool:
        user_data = jsonable_encoder(user)
        new_user = await self.collection.insert_one(user_data)
        return bool(new_user)

    async def search_user_by_username(self, username: str) -> Optional[UserScheme]:
        user = await self.collection.find_one({"username": username})
        return UserScheme(**user) if user else None
