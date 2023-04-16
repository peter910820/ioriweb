import sqlite3, datetime

class DataControl():

    def __init__(self):
        self.DATABASE_URL = './database/ioriweb.db'


    def insert_galgameArticle(self, article_array, articleTitle_array):
        currentDateTime = datetime.datetime.now()
        try:
            db = sqlite3.connect(self.DATABASE_URL)
        except:
            print('Database connect error!')
            return
        try:
            cursor = db.cursor()
            insertQuery = """INSERT INTO galgameArticle VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
            cursor.execute(insertQuery, 
                    (article_array[0], article_array[4], article_array[1], article_array[2],
                    article_array[6], f'{article_array[4]},{article_array[5]}', article_array[3], article_array[7],
                    currentDateTime))
            db.commit() 
            insertQuery = """INSERT INTO galgameTitle VALUES (?, ?, ?);"""
            cursor.execute(insertQuery, 
                    (articleTitle_array[0], articleTitle_array[1],
                    currentDateTime))
            db.commit()
            print('Data created.')
        except:
            print('Data created error!')
        return
    
    def searchArticle(self, articleTitle):
        try:
            db = sqlite3.connect(self.DATABASE_URL)
        except:
            print('Database connect error!')
            return
        cursor = db.cursor()
        result = cursor.execute('''SELECT TITLE FROM galgameTitle;''')
        db.commit()
        for r in result:
            if r[0] == articleTitle:
                print('ok')
        try:
            title = cursor.execute(f'''SELECT * FROM galgameArticle WHERE TITLE = "{articleTitle}";''')
            db.commit()
            articleData = []
            for t in title:
                articleData.append(t)
            print(articleData)
            return articleData
        except:
            print('Inconsistent data!')
            return