import random
x = [['a', 'the', 'her', 'his', 'my', 'other', 'another'], ['man', 'women', 'book', 'girl', 'cat', 'parrot', 'doggo'], ['read', 'ran', 'jumped', 'worked', 'flew', 'barked', 'sang'], ['quietly', 'loudly', 'funny', 'silly', 'badly', 'invaluably', 'strangely']]
z = 0
try:
	s = int(input('***Type number of rows: '))
	if 0>s>10:
		print('Number should be in range 1 - 10! Number remains standart (5)!')
		s = 5
except ValueError:
	print("Wrong input! Number remains standart (5)!\n")
	s = 5
print('\n')
while z < s:
	for i in x:
		y = int(random.randrange(0, 7))
		print(i[y], end=' ')
	print('\n')
	z += 1
input('\n***Type ENTER to exit')