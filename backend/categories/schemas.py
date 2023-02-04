from pydantic import BaseModel

class CategoriesBase(BaseModel):
    name: str
    link: str

class CategoriesCreate(CategoriesBase):
    pass

class Categories(CategoriesBase):
    id: int
    class Config:
        orm_mode = True 




