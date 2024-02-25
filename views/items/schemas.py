from pydantic import BaseModel


class CreateItems(BaseModel):
    name: str