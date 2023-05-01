from pydantic import BaseModel


class PlayerRead(BaseModel):
    name: str
    age: int
    photo_url: str
    nationality: str
    flag_url: str
    club: str
    club_logo_url: str
    value: str
    foot: str
    height: str
    weight: str
    kit_number: int

    class Config:
        orm_mode = True
