# -*- coding: utf-8 -*-
"""
create excel
"""
import pandas as pd
import glob
csv_files = glob.glob('*.xlsx')
list = []
for file in csv_files:
	list.append(pd.read_csv(file))

df = pd.concat(list)
df.to_csv("total.xlsx" , index=False)