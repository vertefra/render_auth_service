from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import uvicorn
import setup

config = setup.BaseSettings().start()
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/login/", response_class=HTMLResponse)
async def test(request: Request, user_id: str):
    print("user id=", user_id)
    return templates.TemplateResponse(
        'login.html', {"request": request, "ID": user_id})

if __name__ == '__main__':
    uvicorn.run("server:app", host=config.HOST, port=config.PORT, reload=True)
