#coding=utf-8

import  pandas as pd

dataframe=pd.read_csv('data1.csv')
dataframe.to_pickle('to_pickle')