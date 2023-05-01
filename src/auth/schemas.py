from fastapi_users import schemas


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    is_active: bool | None = True
    is_superuser: bool | None = False
    is_verified: bool | None = False


class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    email: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserUpdate(schemas.BaseUserUpdate):
    password: str | None
    email: str | None
    is_active: bool | None
    is_superuser: bool | None
    is_verified: bool | None
