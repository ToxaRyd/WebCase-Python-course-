import math
import sys

def price(m):
	z = math.ceil(m/60)
	if z <=100:
		p = z*1
	else:
		p = 100 + ((z-100)*2)
	return(p)

log = {}
try:
	with open(argv[1], 'r', encoding=('utf8')) as f:
		fi = f.readlines()
except FileNotFoundError:
    print('Файл не найден!')
for i in fi:
	if i[1] not in log.keys():
		log[i[1]] = price(int(i[3]))
	else:
		a = log.get(i[1])
		b = price(int(i[3]))
		log[i[1]] = a+b

total = 0

for i in log.keys():
	total += log.get(i)

for i in log.keys():
	print(('Стоимость звонков за {0} составляет - {1} монет'.format(i, log.get(i))))
print(('\nОбщая стоимость звонков - {0} монет.'.format(total)))