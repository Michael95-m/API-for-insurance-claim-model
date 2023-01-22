from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse
from typing import Any
from loguru import logger

from api import api_router

app = FastAPI(
    tilte="Insurance Claim Model", openapi_url="/api/v1")

root_router = APIRouter()

@root_router.get("/")
def index(request: Request) -> Any:
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to the API</h1>"
        "<div>"
        "Check the docs: <a href='/docs'>here</a>"
        "</div>"
        "</body>"
        "</html>"
    )

    return HTMLResponse(body)

app.include_router(api_router, prefix="/api/v1")
app.include_router(root_router)

if __name__ == "__main__":
    import uvicorn
    logger.warning("This is the development mode. Do not run this in production environment")
    uvicorn.run(app, host="localhost", port=8001, log_level="debug")

