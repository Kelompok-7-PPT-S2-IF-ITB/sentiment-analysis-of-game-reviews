from pydantic import BaseModel


class Msg(BaseModel):
    msg: str

class Reviews(BaseModel):
    review: str