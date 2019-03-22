#coding=utf-8
'''
多种格式数据加载、处理与存储
实际的场景中，我们会在不同的地方遇到各种不同的数据格式（比如大家熟悉的csv与txt，比如网页HTML格式，比如XML格式）
，我们来一起看看python如何和这些格式的数据打交道
'''

import numpy as np
from  pandas import DataFrame,Series,Index
import pandas as pd

dataframe1=pd.read_csv('data1.csv',sep=',',header=None,names=['1','2','3','4','5'])
print(dataframe1)

dataframe2=pd.read_csv('data2.csv',sep=',',names=['a', 'b', 'c', 'd', 'message'],index_col=['message'])
print(dataframe2)

#使用列作为index
dataframe3=pd.read_csv('csv_mindex.csv',index_col=['key1','key2'])
print(dataframe3.ix['one','a'][0])

#字段分隔符使用正则
dataframe4=pd.read_table('data3.txt',sep='\s+')
print(dataframe4)

#跳过指定行
dataframe5=pd.read_csv('data4.csv',skiprows=[0,2,3])
print(dataframe5)

#指定空值数据的格式
dataframe6=pd.read_csv('data5.csv',na_values=['NULL','NULL2'])
print(dataframe6)


#指定column 中空值的格式
sentinels = {'message': ['foo', 'NA'], 'something': ['two']} #‘message列中 foo 和NA 视为NaN’
dataframe7=pd.read_csv('data5.csv',na_values=sentinels)
print(dataframe7)

#分块读取数据 防止文件过大 导致 Memorry Error
def chunkRead():
	reader = pd.read_csv('data6.csv', sep=',', chunksize=1000)
#print(reader.get_chunk(5)['key'].value_counts())
	series=Series([])
	for chunk in reader:
		series=series.add(chunk['key'].value_counts(),fill_value=0)
	print(series.sort_values(ascending=False)[:10])

#将数据写入文件
dataframe8=pd.read_csv('data1.csv',index_col=['message'])
print(dataframe8)
dataframe8.to_csv('out.csv')

if __name__ == '__main__':
    chunkRead()