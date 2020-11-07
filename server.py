from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import uvicorn


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def test(request: Request):
    return templates.TemplateResponse('login', {"request": request})

if __name__ === '__main__':
    uvicorn.run()

