"""
Данная программа служит для определения номеров телефона американского формата, 
их преобразования и вывода в фиксированном формате.
"""
import re
import sys

number = re.compile(r"(?P<b1>[(])?[- ]?(?P<b2>\d{3})?[- ]?(?P<b3>[)])?[- ]?(?P<b4>\d{3})?[- ]?(?P<b5>\d{4})", re.VERBOSE)

for i in sys.stdin:
    numb = number.match(i)
    if numb:
        print("("+(numb.group('b2'))+")",numb.group('b4'),numb.group('b5'))
    else:
        print("Введен неверный формат телефона!")
