import random
x = [['a', 'the', 'her', 'his', 'my', 'other', 'another'], ['man', 'women', 'book', 'girl', 'cat', 'parrot', 'doggo'], ['read', 'ran', 'jumped', 'worked', 'flew', 'barked', 'sang'], ['quietly', 'loudly', 'funny', 'silly', 'badly', 'invaluably', 'strangely']]
z = 0

while z < 5:
	for i in x:
		y = int(random.randrange(0, 7))
		print(i[y], end=' ')
	print('\n')
	z += 1