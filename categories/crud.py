from sqlalchemy.orm import Session
from . import models, schemas

def get_categories(skip: int = 0, limit: int = 100, db: Session = None):
    return db.query(models.Categories).offset(skip).limit(limit).all()
def get_categories_by_id(id: int, db: Session = None):
    return db.query(models.Categories).filter(models.Categories.id == id).first()
def create_categories(categories: schemas.CategoriesCreate, db: Session = None):
    db_categories = models.Categories(**categories.dict())
    db.add(db_categories)
    db.commit()
    return db_categories
def update_categories(id: int, categories: schemas.CategoriesCreate, db: Session = None):
    db_categories = db.query(models.Categories).filter(models.Categories.id == id).update(categories.dict())
    if db_categories:
        db.commit()
        return db_categories
    else :
        return False
def delete_categories(id: int, db: Session = None):
    db_categories = db.query(models.Categories).filter(models.Categories.id == id).delete(synchronize_session=False)
    if db_categories :
        db.commit()
        return db_categories
    return db_categories


