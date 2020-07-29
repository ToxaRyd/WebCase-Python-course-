'''
Класс - представляющий совершенное здание робо- города!

>>> Building(1, 2, 2, 2).corners()
{'north-west': [3, 2], 'north-east': [3, 4], 'south-west': [1, 2], 'south-east': [1, 4]}

>>> Building(1, 2.5, 4.2, 1.25).area()
5.25

>>> Building(1, 2.5, 4.2, 1.25, 101).volume()
530.25

>>> str(Building(1, 2.5, 4.2, 1.25))
'Building(1, 2.5, 4.2, 1.25, 10)'
'''

class Building:

	def __init__(self, south, west, width_WE, width_NS, height=10):
		self.__south = south
		self.__west = west
		self.__width_WE = width_WE
		self.__width_NS = width_NS
		if height < 10:
			self.__height = 10
			print('Высота не може быть меньше 10 - значение по умолчанию!')
		else:
			self.__height = height

	def corners(self):
		cor = {}
		cor['north-west'] = [self.__south + self.__width_NS, self.__west]
		cor['north-east'] = [self.__south + self.__width_NS, self.__west + self.__width_WE]
		cor['south-west'] = [self.__south, self.__west]
		cor['south-east'] = [self.__south, self.__west + self.__width_WE]
		return(cor)

	def area(self):
		return(self.__width_WE * self.__width_NS)

	def volume(self):
		return self.area() * self.__height

	def __repr__(self):
		return f'Building({self.__south}, {self.__west}, {self.__width_WE}, {self.__width_NS}, {self.__height})'

	def __str__(self):
		return f'Building({self.__south}, {self.__west}, {self.__width_WE}, {self.__width_NS}, {self.__height})'

if __name__ == '__main__':
    import doctest
    doctest.testmod()