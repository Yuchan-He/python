# -*- coding: utf-8 -*-
"""
このモジュールの説明
02_シートコピー.xlsx
"""

# import library'
from openpyxl import load_workbook
# from openpyxl import Workbook
from datetime import datetime
import io
import sys

# fix the code
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# set the path of the file
filepath = 'D:/400_project/600_program/40_python/excel/02_シートコピー.xlsx'

# read the excel file
wb = load_workbook(filename=filepath)
ws1 = wb['Sheet1']
ws2 = wb['blank']

# make the data in sheet to a list
values1 = [[cell.value for cell in row1] for row1 in ws1]

# make the list of customers
"""
1.delete the header
2.reverse the array of values1
3.delete the repeated data
"""

# 1.delete the header
del values1[0]

# 2.reverse the array of values1
conv_value1 = list(zip(*values1))

# 3.delete the repeated data
customers_list = list(set(conv_value1[0]))
print(len(values1))
print(customers_list)
customers_list.remove(None)
print(customers_list)


# loop the customers_list
for customers in customers_list:
	product_data = []
	for i in range(len(values1)):
		if values1[i][0] == customers:
			product_data.append(values1[i])
	# print(product_data)
	# print(customers)
	# create a new sheet to save new data
	# ws3 = wb.copy_worksheet(ws1)
	# 若在有数据的excel上复制，会覆盖对应数据的地方，没有覆盖的地方会留下原有数据
	# ws3 = wb.copy_worksheet(ws2)
	# rename the sheet
	# ws3.title = customers
	ws3 = wb.create_sheet(customers)
	
	for y,row in enumerate(product_data):
		for x,cell in enumerate(row):
			ws3.cell(row=y+2 , column=x+1 , value=product_data[y][x])

# now = datetime.now()
# filename = 'test.xlsx'

wb.save(filename=filepath)