from pydantic import BaseModel


class PlayerRead(BaseModel):
    name: str
    nationality: str
    club: str
    age: int
    photo_url: str
    flag_url: str
    club_logo_url: str
    value: str
    foot: str
    height: str
    weight: str
    kit_number: int

    class Config:
        orm_mode = True


class PlayerPreview(BaseModel):
    name: str
    nationality: str
    club: str

    class Config:
        orm_mode = True
