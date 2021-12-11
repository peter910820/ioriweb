import uvicorn
from fastapi import FastAPI, Request, HTTPException, Form, Cookie, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

import os
import re
import psycopg2

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# 網頁端 #
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('index.html',{'request':request})

@app.get("/note", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('note.html',{'request':request})

@app.get("/article", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('/article.html',{'request':request})

@app.get("/article/0810_PJSK", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('/article/0810_PJSK.html',{'request':request})

@app.get("/article/0817_TenkafuMA", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('/article/0817_TenkafuMA.html',{'request':request})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    uvicorn.run("Main:app", host="0.0.0.0", port=port, reload=True)