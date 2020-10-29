# -*- coding: utf-8 -*-
"""
Pythonにドラッグ&ドロップでファイルをわたす
"""

import sys
import openpyxl as excel

fp = sys.argv[1]
print(fp) #出力なし

wb = excel.load_workbook(fp)
ws = wb.active

for row in ws.iter_rows():
    print(row[0].value)

print(fp)
    