from pydantic import BaseModel


class BaseDataModel(BaseModel):
    class Config:
        frozen = True
        orm_mode = True
