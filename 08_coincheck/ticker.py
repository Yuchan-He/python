# -*- coding: utf-8 -*-
"""
このモジュールの説明
02_シートコピー.xlsx
"""
import requests
import json

URL = 'https://coincheck.com/api/accounts/balance'
# coincheck = requests.get(URL).json() 
coincheck = requests.get(URL).json()
print(coincheck)
# for key, item in coincheck.items():
    # print("%-9s : %-10.9s " % (key, item))
    # print(key,item)