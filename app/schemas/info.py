from pydantic import BaseModel


class Info(BaseModel):
    name: str
    api_version: str
    model_version: str
