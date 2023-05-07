import uvicorn
from fastapi import FastAPI, Request, HTTPException, Form, Cookie, Response,UploadFile,File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import os, re, psycopg2

from src.hanamaruWeb import DatabaseControl
from src.data_control import DataControl

app = FastAPI(docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/static/css", StaticFiles(directory="static/css"), name="static/css")

templates = Jinja2Templates(directory="templates")
hanamaru = Jinja2Templates(directory="templates/HanamaruWeb")
galgame = Jinja2Templates(directory="templates/GalgameWeb")

# @app.get("/home/{home}")
# async def index(home):
#     return {"message": home}

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('index.html',{'request': request})
#------------------------------------------------------------------------------#

@app.get("/hanamaru", response_class=HTMLResponse)
async def hanamaru_root(request: Request):
    try:
        #initialization(make HanamaruWeb article image)
        db = psycopg2.connect('postgres://seaotter:OC5okdJZpXu3zo8RSmpKyyowcfrawdPh@dpg-cgpajv0u9tun42shmebg-a.oregon-postgres.render.com/ioriweb')
        cursor = db.cursor()
        amount = len(os.listdir('./static/img/hanamaruWeb/article_img/'))
        if amount == 1:
            cursor.execute('''SELECT title, article_img FROM hanamaruWeb_article;''')
            data = cursor.fetchall()
            for d in data:
                file = open(f"./static/img/hanamaruWeb/article_img/{d[0]}","wb")
                file.write(d[1])
                file.close
    except:
        print('HanamaruWeb article image create failed!')
        return hanamaru.TemplateResponse('error.html',{'request': request})
    try:    
        cursor.execute('''SELECT title, author, tag, introduction, create_time FROM hanamaruWeb_article;''')
        data = cursor.fetchall()
        return hanamaru.TemplateResponse('home.html',{'request': request, 'data' : data})
    except:
        print('Select database failed!')
        return hanamaru.TemplateResponse('error.html',{'request': request})

@app.get("/hanamaru/newarticle", response_class=HTMLResponse)
async def hanamaru_newarticle(request: Request):
    return hanamaru.TemplateResponse('newArticle.html',{'request': request})

@app.post("/hanamaru/submit", response_class=HTMLResponse)
async def hanamaru_submit(request: Request, image: UploadFile = File(...), information : list = Form(...)):
    if information[-1] == '0000':
        if image.filename[-3:] == 'png' or image.filename[-3:] == 'jpg':
            information[0] = information[0] + '.' + image.filename[-3:]
            contents = image.file.read()
            control = DatabaseControl()
            control.article_insert(contents, information)
            file = open(f'./static/img/hanamaruWeb/article_img/{information[0]}','wb')
            file.write(contents)
            file.close
            return hanamaru.TemplateResponse('submit.html',{'request': request})
        else:
            print('File is not a image!')
            return hanamaru.TemplateResponse('error.html',{'request': request})
    else:
        print('Password error!')
        return hanamaru.TemplateResponse('error.html',{'request': request})

@app.get("/hanamaru/article/{articleTitle}", response_class=HTMLResponse)
async def hanamaru_articleTitle(request: Request, articleTitle):
    try:
        db = psycopg2.connect('postgres://seaotter:OC5okdJZpXu3zo8RSmpKyyowcfrawdPh@dpg-cgpajv0u9tun42shmebg-a.oregon-postgres.render.com/ioriweb')
        cursor = db.cursor()
        cursor.execute(f'''SELECT content FROM hanamaruWeb_article WHERE title LIKE '{articleTitle}.___';''')
        data = cursor.fetchall()
        tmp =  data[0][0]
        articleData = tmp.replace('\\u0009', '\t').replace('\\u000A', '\n')
        return hanamaru.TemplateResponse('/article.html',{'request': request, 'articleData' : articleData})
    except:
        print('sql error!')
        return hanamaru.TemplateResponse('/error.html',{'request': request})


@app.get("/hanamaru/testter", response_class=HTMLResponse)
async def hanamaru_testter(request: Request):
    return hanamaru.TemplateResponse('testter.html',{'request': request})

#------------------------------------------------------------------------------#

@app.get("/galgame", response_class=HTMLResponse)
async def galgameRoot(request: Request):
    db = psycopg2.connect('postgres://seaotter:OC5okdJZpXu3zo8RSmpKyyowcfrawdPh@dpg-cgpajv0u9tun42shmebg-a.oregon-postgres.render.com/ioriweb')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM galgameTitle;''')
    data = cursor.fetchall()
    return galgame.TemplateResponse('home.html',{'request': request,'data' : data})

@app.get("/galgame/resource", response_class=HTMLResponse)
async def resource(request: Request):
    return galgame.TemplateResponse('resource.html',{'request':request})

@app.get("/galgame/databaseOperate", response_class=HTMLResponse)
async def databaseOperate(request: Request):
    return galgame.TemplateResponse('databaseoperate.html',{'request':request})

@app.get("/galgame/tag/{tagName}", response_class=HTMLResponse)
async def tagName(request: Request, tagName):
    data_control = DataControl()
    titleList = data_control.searchTag(tagName)
    return galgame.TemplateResponse('/tagname.html',{'request': request, 'tagName':tagName, 'titleList':titleList})

@app.get("/galgame/article/{articleTitle}", response_class=HTMLResponse)
async def articleTitle(request: Request, articleTitle):
    data_control = DataControl()
    articleData = data_control.searchArticle(articleTitle)
    return galgame.TemplateResponse('/article.html',{'request': request, 'articleData' : articleData[0]})

@app.get("/galgame/aboutme", response_class=HTMLResponse)
async def aboutme(request: Request):
    return galgame.TemplateResponse('/aboutme.html',{'request':request})

@app.get("/galgame/newGalgameArticle", response_class=HTMLResponse)
async def newGalgameArticle(request: Request):
    db = psycopg2.connect('postgres://seaotter:OC5okdJZpXu3zo8RSmpKyyowcfrawdPh@dpg-cgpajv0u9tun42shmebg-a.oregon-postgres.render.com/ioriweb')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM tag;''')
    data = cursor.fetchall()
    return galgame.TemplateResponse('/newGalgameArticle.html',{'request':request, 'data':data})

@app.post("/galgame/submmit", response_class=HTMLResponse)
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
        data_control.galgameArticle_insert(article_array, articleTitle_array)
    else:
        print('password error!')
    return galgame.TemplateResponse('/submmit.html',{'request':request})

@app.post("/galgame/sabi", response_class=HTMLResponse)
async def sabi(request: Request, tagInformation : list = Form(...)):
    if tagInformation[-1] == '1111':
        tagInformation.pop(-1)
        tagName = tagInformation[0]
        data_control = DataControl()
        data_control.tagName_insert(tagName)
    else:
        print('password error')
    return galgame.TemplateResponse('/submmit.html',{'request':request})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=True)