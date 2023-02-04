from sqlalchemy.orm import Session
from . import models, schemas

def get_items(skip: int = 0, limit: int = 100, db: Session = None):
    return db.query(models.Items).offset(skip).limit(limit).all()

def get_items_by_id(id: int, db: Session = None):
    return db.query(models.Items).filter(models.Items.id == id).first()

def get_items_by_category_id(id: int, db: Session = None):
    return db.query(models.Items).filter(models.Items.category_id == id).all()
    
def create_items(items: schemas.ItemCreate, db: Session = None):
    db_items = models.Items(**items.dict())
    db.add(db_items)
    db.commit()
    return db_items

def update_items(id: int, items: schemas.ItemCreate, db: Session = None):
    db_items = db.query(models.Items).filter(models.Items.id == id).update(items.dict())
    if db_items:
        db.commit()
        return db_items
    else :
        return False

def delete_items(id: int, db: Session = None):
    db_items = db.query(models.Items).filter(models.Items.id == id).delete(synchronize_session=False)
    if db_items :
        db.commit()
        return db_items
    return db_items

def upload_image(id: int, image: str, db: Session = None):
    db_items = db.query(models.Items).filter(models.Items.id == id).update({'image': image})
    if db_items:
        db.commit()
        return db_items
    else :
        return False