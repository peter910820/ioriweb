import psycopg2

db = psycopg2.connect('postgres://seaotter:OC5okdJZpXu3zo8RSmpKyyowcfrawdPh@dpg-cgpajv0u9tun42shmebg-a.oregon-postgres.render.com/ioriweb', sslmode='require')
cursor = db.cursor()
# cursor.execute(
# '''CREATE TABLE tag(
#     tagName VARCHAR(255) NOT NULL,
#     CREATE_TIME timestamp);''')
db.commit()
cursor.close()