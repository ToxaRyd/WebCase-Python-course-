'''
Модуль для нахождения самых дорогих товаров!

>>> bigger_price(2, [{'name': 'bread', 'price': 100}, {'name': 'wine', 'price': 138}, {'name': 'meat', 'price': 15}, {'name': 'water', 'price': 1}])
[{'name': 'wine', 'price': 138}, {'name': 'bread', 'price': 100}]

>>> bigger_price(1, [{'name': 'pen', 'price': 5}, {'name': 'whiteboard', 'price': 170}])
[{'name': 'whiteboard', 'price': 170}]
'''

def bigger_price(limit: int, data: list) -> list:
	l = []
	data.sort(key=lambda  data: data["price"])
	data.reverse()
	for i in range(limit):
		l.append(data[i])
	return l

if __name__ == '__main__':
    import doctest
    doctest.testmod()