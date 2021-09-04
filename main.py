from app.lib.const import APP_HOST, APP_PORT
from fastapi import FastAPI
import uvicorn

from app.routes import router


app = FastAPI()
app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)
