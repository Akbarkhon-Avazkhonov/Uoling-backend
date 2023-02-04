import shutil
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from debug_toolbar.middleware import DebugToolbarMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    debug=True,
    title="Uoling API",
    version="0.1.1",
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


from categories import main as categories
app.include_router(categories.router)

from items import main as items

app.include_router(items.router)

app.add_middleware(
    DebugToolbarMiddleware,
    panels=["debug_toolbar.panels.sqlalchemy.SQLAlchemyPanel"],
)


app.mount("/static", StaticFiles(directory="static"), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
            app, 
            host="0.0.0.0", 
            port=8000,
            ssl_certfile='sslcert.pem',
            ssl_keyfile='sslkey.pem',
            )

    

