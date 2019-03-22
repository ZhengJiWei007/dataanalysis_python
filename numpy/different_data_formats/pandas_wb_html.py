#coding=utf-8
'''
python web api 收集数据

'''

from lxml.html import parse
from urllib.request import urlopen
from  pandas import Series,DataFrame
from pandas.io.parsers import TextParser
url='https://finance.yahoo.com/quote/AAP/options?ltr=1'

def getRootDoc(url):
	parsed = parse(urlopen(url))
	return parsed.getroot()

#解析 表格th 和td 内容
def _unpack(row,kind='td'):
	elts = row.findall('.//%s' % kind)
	return [ele.text_content() for ele in elts]

#将table 转化成 DataFrame
def parse_table(table):
	rows = table.findall('.//tr')
	head = _unpack(rows[0],kind='th')
	data = [_unpack(row,kind='td')for row in rows[1:]]
	#df	= TextParser(cifar10_data,names=head)
	df = DataFrame(data,columns=head)
	print(df.head(5))

if __name__ == '__main__':
	doc = getRootDoc(url=url)
	# elets = doc.findall('.//a')
	# [print('href:%s    text-content:%s'%(ele.get('href'),ele.text_content())) for ele in elets]
	tables = doc.findall('.//table')
	calls=tables[0]
	# rows1=calls.findall('.//tr')

	puts=tables[1]
	# rows2=puts.findall('.//tr')
	# print(_unpack(rows1[0],kind='th'))

	parse_table(calls)











