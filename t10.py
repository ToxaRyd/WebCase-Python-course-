"""
is_ascii() -- возвращает True, если все символы в заданной строке имеют числовые коды меньше 127;
is_ascii_punctuation() -- возвращает True, если все символы в заданной строке содержатся в строке string.punctuation;
is_ascii_printable() -- возвращает True, если все символы в заданной строке содержатся и в строке string.printable;

>>> is_ascii('ojqfub9qbfiosdubhsyfb')
True
>>> is_ascii('ojqfub9qbЖИЗАfiosdubhsyfb')
False

>>> is_ascii_punctuation('!,=>< .')
True
>>> is_ascii_punctuation('ojqfub9qbЖИЗАfiosdubhsyfb')
False

>>> is_ascii_printable('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<=>?@[]^_`{|}~')
True
>>> is_ascii_printable('ojqfub9qbЖИЗАfiosdubhsyfb')
False

"""

is_ascii = lambda var_str: all([ord(c) < 127 for c in var_str])
is_ascii_punctuation = lambda var_str: len(var_str) == len(var_str.encode())
is_ascii_printable = lambda var_str: all([c.isascii() for c in var_str])
is_ascii.__doc__ = is_ascii_punctuation.__doc__ = is_ascii_printable.__doc__

if __name__ == '__main__':
	import doctest
	doctest.testmod()
