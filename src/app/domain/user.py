from pydantic import BaseModel, Field


class UserApiScheme(BaseModel):

    username: str = Field(max_length=100)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "username",
                "password": "password",
            }
        }


class UserScheme(UserApiScheme):

    salt: str = Field(max_length=100)

    class Config:
        schema_extra = {
            "example": {
                "username": "username",
                "password": "password",
                "salt": "salt"
            }
        }
