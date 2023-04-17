import uvicorn
from fastapi import FastAPI, Request, HTTPException, Form, Cookie, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import os, psycopg2

from src.data_control import DataControl

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# 網頁端 #
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    db = psycopg2.connect('postgres://seaotter:OC5okdJZpXu3zo8RSmpKyyowcfrawdPh@dpg-cgpajv0u9tun42shmebg-a.oregon-postgres.render.com/ioriweb')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM galgameTitle;''')
    data = cursor.fetchall()
    return templates.TemplateResponse('home.html',{'request': request,'data' : data})

@app.get("/resource", response_class=HTMLResponse)
async def resource(request: Request):
    return templates.TemplateResponse('resource.html',{'request':request})

@app.get("/note", response_class=HTMLResponse)
async def note(request: Request):
    return templates.TemplateResponse('note.html',{'request':request})

@app.get("/article/{articleTitle}", response_class=HTMLResponse)
async def root(request: Request, articleTitle):
    data_control = DataControl()
    articleData = data_control.searchArticle(articleTitle)
    return templates.TemplateResponse('/article.html',{'request': request, 'articleData' : articleData[0]})

@app.get("/newGalgameArticle", response_class=HTMLResponse)
async def newGalgameArticle(request: Request):
    return templates.TemplateResponse('/newGalgameArticle.html',{'request':request})

@app.get("/newArticle", response_class=HTMLResponse)
async def newArticle(request: Request):
    return templates.TemplateResponse('/newArticle.html',{'request':request})

@app.post("/submmit", response_class=HTMLResponse)
async def submmit(request: Request, information : list = Form(...)):
    if information[-1] == '0000':
        information.pop(-1)
        data_control = DataControl()
        article_array = []
        articleTitle_array = []
        articleTitle_array.append(information[0])
        articleTitle_array.append(f'{information[4]},{information[5]}')
        for i in information:
            article_array.append(i)
        article_array[6]  = 'https://www.youtube.com/embed/' + article_array[6][32:]
        data_control.insert_galgameArticle(article_array, articleTitle_array)
    else:
        print('password error')
    return templates.TemplateResponse('/submmit.html',{'request':request})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)