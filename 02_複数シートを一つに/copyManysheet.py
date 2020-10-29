# -*- coding: utf-8 -*-
"""
combine many sheet
"""

import glob
import pandas as pd

files = glob.glob('Excel*.xlsx')
list = []

for file in files:
    list.append(pd.read_excel(file))

print(list)
df = pd.concat(list)
df.to_excel('total2.xlsx', index=False)
