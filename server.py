from fastapi import FastAPI, Request, Response, Header
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
import setup

config = setup.BaseSettings().start()
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3002"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

templates = Jinja2Templates(directory="templates")


@app.get("/login/", response_class=HTMLResponse)
async def test(request: Request, user_id: str):
    return templates.TemplateResponse(
        'login.html', {
            "request": request,
            "ID": user_id,
            "server": config.GO_SERVER})


@app.get("/redirect")
async def redirect(
        redirect: str,
        response: Response,
        authorization: str = Header(None)
        ):

    # response.headers["Authorization": authorization]
    # response.redirected = True
    print("REDIRECT: ", redirect)
    return RedirectResponse(redirect)

if __name__ == '__main__':
    uvicorn.run("server:app", host=config.HOST, port=config.PORT, reload=True)
