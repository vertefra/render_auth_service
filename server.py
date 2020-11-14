from fastapi import FastAPI, Request, Header, Response, Body
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
    allow_origins="*",
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


@app.post("/redirect")
async def redirect(
        response: Response,
        authorization: str = Header(None),
        redirectURL: str = Body(None)):

    # response.headers["Authorization": authorization]
    # response.redirected = True
    print(redirectURL)
    return RedirectResponse(redirectURL)


if __name__ == '__main__':
    uvicorn.run("server:app", host=config.HOST, port=config.PORT, reload=True)
