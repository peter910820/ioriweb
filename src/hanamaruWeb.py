import psycopg2, datetime

class DatabaseControl():

    def __init__(self):
        self.DATABASE_URL = 'postgres://seaotter:OC5okdJZpXu3zo8RSmpKyyowcfrawdPh@dpg-cgpajv0u9tun42shmebg-a.oregon-postgres.render.com/ioriweb'

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
        cursor = db.cursor()
        insertQuery = """INSERT INTO hanamaruWeb_article VALUES (%s, %s, %s, %s, %s, %s);"""
        cursor.execute(insertQuery, 
                (information[0], information[1], information[2], information[3], contents, currentDateTime))
        db.commit()
        cursor.close()
        db.close()
        return 0
    
