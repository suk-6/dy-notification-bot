import os
from fastapi import FastAPI
from models import NotificationModel
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from api import API


KAKAOBOT_API_KEY = os.getenv("KAKAOBOT_API_KEY")
PASSWORD = os.getenv("PASSWORD")

app = FastAPI()
api = API(KAKAOBOT_API_KEY)


@app.get("/")
def index():
    return FileResponse("frontend/public/index.html")


@app.post("/notification")
async def notification(notification: NotificationModel):
    if notification.password != PASSWORD:
        return {"error": "Invalid password"}

    return api.sendMessageAll(notification.content, notification.send)


app.mount("/", StaticFiles(directory="frontend/public"))
app.mount("/build", StaticFiles(directory="frontend/public/build"))

if __name__ == "__main__":
    import uvicorn
    from dotenv import load_dotenv

    load_dotenv()
    uvicorn.run(app, host="0.0.0.0", port=8000)
