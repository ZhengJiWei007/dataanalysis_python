
from pandas import DataFrame,ExcelFile

'''
pandas 读取excel 数据 DataFrame
'''

xlsFile = ExcelFile('cifar10_data.xlsx')
df = xlsFile.parse('工作表1')
print(df.dtypes)
