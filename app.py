import uvicorn
from fastapi import FastAPI, Request, HTTPException, Form, Cookie, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import os, re, psycopg2,sqlite3,datetime

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# 網頁端 #
@app.get("/", response_class=HTMLResponse)

async def root(request: Request):
    db = sqlite3.connect('./database/ioriweb.db')
    cursor = db.cursor()
    data = cursor.execute('''SELECT * FROM galgameTitle;''')

    return templates.TemplateResponse('home.html',{'request':request,'data' : data})

@app.get("/note", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('note.html',{'request':request})

@app.get("/newArticle", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('/newArticle.html',{'request':request})

@app.post("/submmit", response_class=HTMLResponse)
async def root(request: Request, information : list = Form(...)):
    if information[-1] == '0000':
        db = sqlite3.connect('./database/ioriweb.db')
        cursor = db.cursor()
        insertQuery = """INSERT INTO galgameTitle VALUES (?, ?, ?);"""
        currentDateTime = datetime.datetime.now()
        cursor.execute(insertQuery, (information[0], f'{information[4]},{information[5]}', currentDateTime))
        print('Data created.')
        db.commit()
    else:
        print('password error')
    print(information)
    return templates.TemplateResponse('/submmit.html',{'request':request})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    uvicorn.run("app:app", host="127.0.0.1", port=port, reload=True)