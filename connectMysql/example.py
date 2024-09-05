import pymysql
import pandas as pd

db = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    db='pydb',
    charset='utf8')

cur = db.cursor()
cur.execute('select * from todo')
result = cur.fetchall()

for row in result:
    print(row)

columns = [desc[0] for desc in cur.description]
df = pd.DataFrame(result, columns=columns)
# print(df)

db.close()