from passlib.handlers.pbkdf2 import pbkdf2_sha256

from app.domain.user import UserScheme, UserApiScheme
from app.repository.user import UserRepository
from app.utils import get_random_string


class UserService:
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    async def registration(self, user: UserApiScheme) -> bool:
        if await self.repo.search_user_by_username(user.username):
            return False

        print("Регистрация нового пользователя")
        print(f"Юзернейм пользователя {user.username}")
        print(f"Исходный пароль пользователя {user.password}")
        salt = get_random_string()
        print(f"Сгенерированная соль для пользователя - {salt}")
        new_pas = pbkdf2_sha256.hash(user.password + salt)
        print(f"Пароль при сложение с солью: \n {user.password + salt}")
        print(f"Пароль после хеширования{new_pas}")
        user_data = {
            "username": user.username,
            "password": new_pas,
            "salt": salt
        }

        return bool(await self.repo.create_user(UserScheme(**user_data)))

    async def login(self, user: UserApiScheme) -> bool:
        user_db = await self.repo.search_user_by_username(user.username)
        if not user_db:
            return False

        print(f"Авторизация пользователя: {user_db.username}")
        print(f"Введенный пользователем пароль {user.password}")
        print()
        print(f"Пароль пользователя, хранящиеся в БД {user_db.password}")
        print(f"Соль пользователя, хранящиеся в БД {user_db.salt}")
        print()
        print(f"Введенный пароль пользователя с солью {user.password + user_db.salt}")
        print(f"Пароль с солью после хеширования {pbkdf2_sha256.hash(user.password + user_db.salt)}")
        print(f"Удачность авторизации - {pbkdf2_sha256.verify(user.password + user_db.salt, user_db.password)}")

        return pbkdf2_sha256.verify(user.password + user_db.salt, user_db.password)
