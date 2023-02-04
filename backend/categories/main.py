from fastapi import APIRouter, Depends ,HTTPException,status
from sqlalchemy.orm import Session
from . import crud, models, schemas

from database import engine, get_db
models.Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)



@router.get("/")
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = crud.get_categories(skip=skip, limit=limit, db=db)
    return categories


@router.get("/{id}")
def read_categories_by_id(id: int, db: Session = Depends(get_db)):
    db_categories = crud.get_categories_by_id(id=id, db=db)
    if db_categories is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categories not found")
    return db_categories


@router.post("/")
def create_categories(categories: schemas.CategoriesCreate, db: Session = Depends(get_db)):
    return crud.create_categories(categories=categories, db=db)

@router.put("/{id}")
def update_categories(id: int, categories: schemas.CategoriesCreate, db: Session = Depends(get_db)):
    db_categories = crud.update_categories(id=id, categories=categories, db=db)
    if db_categories is None:
        raise HTTPException(status_code=404, detail="Categories not found")
    return db_categories

@router.delete("/{id}")
def delete_categories(id: int, db: Session = Depends(get_db)):
    db_categories = crud.delete_categories(id=id, db=db)
    if db_categories is None:
        raise HTTPException(status_code=404, detail="Categories not found")
    return db_categories


