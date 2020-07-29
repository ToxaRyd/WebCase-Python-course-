"""
Класс мигающей герлянды)

>>> p = lamp()
>>> print(p.light())
Red
>>> print(p.light())
Brown
>>> print(p.light())
Green
>>> print(p.light())
Yellow
>>> print(p.light())
Red
"""
import itertools

class lamp:
	def __init__(self):
		self.colour = itertools.cycle(['Red','Brown','Green','Yellow'])
	def light(self):
		return next(self.colour)

if __name__ == '__main__':
	import doctest
	doctest.testmod()