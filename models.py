from pydantic import BaseModel


class NotificationModel(BaseModel):
    content: str
    password: str
    send: str
