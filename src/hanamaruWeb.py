import psycopg2, datetime, re, os

class DatabaseControl():

    def __init__(self):
        self.DATABASE_URL = os.getenv("SQL_URL")

    def article_insert(self, contents, information):
        if len(information[0]) >= 100 or len(information[1]) >= 20 or len(information[2]) >= 255:
            print('The data is too long!')
            return 1
        try:
            db = psycopg2.connect(self.DATABASE_URL)
        except:
            print('Database connect error!')
            return 1
        currentDateTime = datetime.datetime.now().replace(microsecond=0)
        pattern = re.compile(r'<[^>]+>', re.S)
        introduction = pattern.sub('', information[3])
        introduction = introduction[0:120]
        cursor = db.cursor()
        insertQuery = """INSERT INTO hanamaruWeb_article VALUES (%s, %s, %s, %s, %s, %s, %s);"""
        cursor.execute(insertQuery, 
                (information[0], information[1], information[2], introduction, information[3], contents, currentDateTime))
        db.commit()
        cursor.close()
        db.close()
        return 0
    
