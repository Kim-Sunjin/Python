# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XMy_5Qv4CEnyRjuLJ8kWg7b0km0PscOO

# Unit7. 출력
"""

a, b = map(int, input('정수 두개 이벽> ').split())
print(a)
print(b)

print(a, b, sep=',')

"""## 줄바꿈 활용"""

print(a,b, sep='\n')

print(a, b, sep='/\\')

print(a, end=' ')
print(b)

