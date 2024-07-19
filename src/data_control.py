import psycopg2, datetime, os

class DataControl():

    def __init__(self):
        self.DATABASE_URL = os.getenv("SQL_URL")


    def galgameArticle_insert(self, article_array, articleTitle_array):
        currentDateTime = datetime.datetime.now()
        try:
            db = psycopg2.connect(self.DATABASE_URL)
        except:
            print('Database connect error!')
            return
        try:
            cursor = db.cursor()
            insertQuery = """INSERT INTO galgameArticle VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            cursor.execute(insertQuery, 
                    (article_array[0], article_array[4], article_array[1], article_array[2],
                    article_array[6], f'{article_array[4]},{article_array[5]}', article_array[3], article_array[7],
                    currentDateTime))
            db.commit() 
            insertQuery = """INSERT INTO galgameTitle VALUES (%s, %s, %s);"""
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
            db = psycopg2.connect(self.DATABASE_URL)
        except:
            print('Database connect error!')
            return
        cursor = db.cursor()
        cursor.execute('''SELECT TITLE FROM galgameTitle;''')
        result = cursor.fetchall()
        for r in result:
            if r[0] == articleTitle:
                print('ok')
        try:
            cursor.execute(f'''SELECT * FROM galgameArticle WHERE TITLE = '{articleTitle}';''')
            title = cursor.fetchall()
            articleData = []
            for t in title:
                articleData.append(t)
            print(articleData)
            return articleData
        except:
            print('Inconsistent data!')
            return
        
    def tagName_insert(self, tagName):
        try:
            db = psycopg2.connect(self.DATABASE_URL)
        except:
            print('Database connect error!')
            return
        cursor = db.cursor()
        insertQuery = """INSERT INTO tag VALUES (%s, %s);"""
        cursor.execute(insertQuery, 
                (tagName, datetime.datetime.now()))
        db.commit()

    def searchTag(self, tagName):
        try:
            db = psycopg2.connect(self.DATABASE_URL)
        except:
            print('Database connect error!')
            return
        titleList = []
        cursor = db.cursor()
        cursor.execute("""SELECT * FROM galgameTitle;""")
        data = cursor.fetchall()
        for d in data:
            tmp = d[1].split(',')
            for t in tmp:
                if tagName == t:
                    titleList.append(d[0])
        return titleList