from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    price: int 
    link: str
    image: str = None
    category_id: int = None
    description: str = None
    price_per_month: int = None
    isActive: bool = True
    colors: str = None
    characteristics: str = None



class ItemCreate(ItemBase):
    pass
    
class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

    pass


