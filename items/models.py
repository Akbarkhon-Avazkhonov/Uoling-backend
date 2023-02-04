from sqlalchemy import Column,Integer, String , Boolean

from database import Base



'''
interface Productdata {
  id: number;
  isAdmin?: boolean;
  name: string;
  price: number;
  image: string;
  link: string;
  colors: {
    id: number;
    name: string;
    code: string;
    images: {
      id: number;
      src: string;
    }[];
  }[];
  characteristics: {
    id: number;
    name: string;
    value: {
      id: number;
      name: string;
      price: number;
      description: string;
    }[]
    }[];

    

  price_per_month: number;

  
    

  
  category_id: number;
  description: string;
  isActive?: boolean;


};

'''
class Items(Base):
    __tablename__ = "Items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer, index=True)
    link = Column(String, index=True)
    image = Column(String, index=True)
    category_id = Column(Integer, index=True)
    description = Column(String, index=True)
    price_per_month = Column(Integer, index=True)
    isActive = Column(Boolean, index=True)
    colors = Column(String, index=True)
    characteristics = Column(String, index=True)
    

  

