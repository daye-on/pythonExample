from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    'mysql+pymysql://root:root@localhost:3306/pydb')

conn = engine.connect()
result = pd.read_sql_query("SELECT * FROM todo", conn)
print(result)

result2 = pd.read_sql_query("SELECT * FROM todo WHERE title like '%%plan%%'", conn)
print(result2)
conn.close()