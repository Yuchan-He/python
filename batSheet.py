# -*- coding: utf-8 -*-
"""
ファイルの明細を書く
"""
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print('hello')
print('おはよう')

print(sys.stdout)