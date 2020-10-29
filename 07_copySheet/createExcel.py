# -*- coding: utf-8 -*-
"""
このモジュールの説明
"""
import pandas as pd

df = pd.DataFrame({'ID':[1,2,3],'Name':['Amy','Tom','Lili']})
# df.to_excel('D:\\400_project\\600_program\\40_python\\output.xlsx')
print(df)

# df = df.set_index('ID')
print(df)
df.to_excel('D:\\400_project\\600_program\\40_python\\output.xlsx')

df_type = pd.DataFrame()
print(df_type)
print(type(df_type))
