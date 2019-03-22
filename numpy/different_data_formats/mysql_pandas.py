#coding=utf-8

'从mysql 拉去数据转化成DataFrame'


import pymysql
from pandas import DataFrame
import pandas
import tushare as ts
from sqlalchemy import create_engine
host='localhost'
port = 3306
user='root'
passwd='root'
db ='test3'
conn= pymysql.connect(host=host,port=port,user=user,passwd=passwd,db=db)
cursor = conn.cursor()
query='''
    select * from heroinfo
'''
# cursor.execute(query)
# results = cursor.fetchall()
# print(results)
# print(cursor.description)

# df = ts.get_hist_data('000875')#读取数据，格式为DataFrame
# print(df)
engine = create_engine('mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(user, passwd, host, port, db))
'''
def to_sql(self, name, con, flavor=None, schema=None, if_exists='fail',
               index=True, index_label=None, chunksize=None, dtype=None):
'''
#df.to_sql('tick_data',engine,if_exists='append')
query='SELECT * FROM test3.`tick_data` limit 5'
#df2 = pandas.read_sql(sql=query,con=engine, index_col='date', parse_dates=['date'])
df3=pandas.read_sql_query(query,con=engine,parse_dates=['date'],index_col='date')
print(df3)
#dataframe = sql.execute(query,conn,cur=cursor)
#print(dataframe)