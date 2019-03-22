#coding=utf-8

import pandas as pd
import numpy as np

dataframe = pd.read_csv('kaggle_bike_competition_train.csv', header=0, error_bad_lines=False).head(100)
# print(dataframe.head(10))
# print(dataframe['datetime'].head(10))

#将日期字段 分为date 和 time
#print(dataframe.iloc[:,:5])
datetime_index = pd.DatetimeIndex(dataframe['datetime'])
dataframe['date']=datetime_index.date
dataframe['time']=datetime_index.time
dataframe['hour']=datetime_index.hour
dataframe['dayofweek']=datetime_index.dayofweek
dataframe['dateDays']=(dataframe['date']-dataframe['date'][0]).astype('timedelta64[D]')
# print((dataframe['date']-dataframe['date'][0]))
# print((dataframe['date']-dataframe['date'][0]).astype('timedelta64[D]').dtype)
#print(dataframe.head(5))
# print(dataframe.columns)
#
# print(dataframe.loc[:,['datetime','hour','time','dayofweek']])
# print(dataframe.iloc[:,-3:])
# print(dataframe['hour'])
# print(dataframe.iloc[:,['date','time','hour','datetime']].head(5))

'统计下一周各天自行车租凭情况（分注册的人和没注册的人）'
#注册的人 --根据 dayofweek 分组求和
res_reg=dataframe.groupby('dayofweek')['registered'].sum()
# print(res_reg)
#没注册的人
res_cas=dataframe.groupby('dayofweek')['casual'].sum()
# print(res_cas)

dataframe['Saturday']=0
dataframe['Sunday']=0
print(dataframe)
dataframe.Saturday[dataframe.dayofweek==5]=1
dataframe['Sunday'][dataframe['dayofweek']==6]=1
print(dataframe.loc[:,['dayofweek','Saturday','Sunday']])






