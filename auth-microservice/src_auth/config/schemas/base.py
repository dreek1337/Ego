from pydantic import BaseModel


class BaseDataModel(BaseModel):
    class Config:
        orm_mode = True
