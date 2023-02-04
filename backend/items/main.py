
from fastapi import APIRouter, Depends ,HTTPException,status , File, UploadFile
from sqlalchemy.orm import Session
from . import crud, models, schemas

from database import engine, get_db
models.Base.metadata.create_all(bind=engine)

import shutil

router = APIRouter(
    prefix="/items",
    tags=["Items"],
)

@router.get("/")
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(skip=skip, limit=limit, db=db)
    return items

@router.get("/category/{id}")
def read_items_by_category_id(id: int, db: Session = Depends(get_db)):
    items = crud.get_items_by_category_id(id=id, db=db)
    if items :
        return items
    return []
    
@router.get("/{id}")
def read_items_by_id(id: int, db: Session = Depends(get_db)):
    db_items = crud.get_items_by_id(id=id, db=db)
    if db_items is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Items not found")
    return db_items

@router.post("/")
def create_items(items: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_items(items=items, db=db)

@router.put("/{id}")
def update_items(id: int, items: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_items = crud.update_items(id=id, items=items, db=db)
    if db_items is None:
        raise HTTPException(status_code=404, detail="Items not found")
    return db_items

@router.delete("/{id}")
def delete_items(id: int, db: Session = Depends(get_db)):
    db_items = crud.delete_items(id=id, db=db)
    if db_items is None:
        raise HTTPException(status_code=404, detail="Items not found")
    return db_items


@router.post("/upload/")
def upload_image(file: UploadFile , db: Session = Depends(get_db)):

    shutil.copyfileobj(file.file, open(f"static/{file.filename}", "wb"))
    
    # crud.upload_image(id=id, image=f"static/{file.filename}", db=db)
    
    return {"filename": file}