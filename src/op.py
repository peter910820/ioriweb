import psycopg2, datetime

db = psycopg2.connect('postgres://seaotter:OC5okdJZpXu3zo8RSmpKyyowcfrawdPh@dpg-cgpajv0u9tun42shmebg-a.oregon-postgres.render.com/ioriweb', sslmode='require')
currentDateTime = datetime.datetime.now()
cursor = db.cursor()
# # cursor.execute(
# '''CREATE TABLE galegmaeCompany(
#     tagName VARCHAR(255) NOT NULL,
#     CREATE_TIME timestamp);''')

# insertQuery = """INSERT INTO tag VALUES (%s, %s);"""
# cursor.execute(insertQuery, 
#         ('KEY', currentDateTime))
db.commit() 
cursor.close()