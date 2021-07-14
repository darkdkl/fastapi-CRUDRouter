import uvicorn
from fastapi import FastAPI
from crud_test.db import database, metadata, engine
from crud_test.route import post_router, category_router, comment_router

app = FastAPI()

metadata.create_all(engine)
app.state.database = database


@app.on_event('startup')
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event('shutdown')
async def shutdown() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.disconnect()

app.include_router(comment_router)
app.include_router(post_router)
app.include_router(category_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")