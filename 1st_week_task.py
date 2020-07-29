print("""
 Данная программа осуществляет взаимодействие со списком задач.

	Ниже приведены команды для взаимодействия:

	-create -- создание новой задачи;
	-read   -- чтение выбранной задачи;
	-update -- обновление выбранной задачи;
	-delete -- удаление выбранной задачи;
	-done   -- обновление статуса выбранной задачи как "выполнено";
	-list   -- вывод списка всех задач.
""")

import sys
import datetime

main = []

try:
	with open('tasks.txt', 'r', encoding=('utf8')) as f:
		for row in f:
			main.append(row)
except FileNotFoundError:
    print('Не найден предыдущий список задач! Будет создан новый!')

with open('tasks.txt', 'w', encoding=('utf8')) as f:
	a = input("Введите желаемую команду: ")
	if a == '-create':
	    a1 = input('Введите название задачи: ')
	    a2 = input('Введите описание: ')
	    a3 = ('{0:^9} / {1:^9} / {2:^16} / {3:^16} /     {4}\n'.format(a1, 'Активно', 
	    	(str(datetime.datetime.now())[0:16]), '***', a2))
	    main.append(a3)
	    print('Задача успешно создана!')
	if a == '-read':
		a1 = input('Введите название задачи: ')
		c = 1
		for row in main:
			if a1 in row[0:10]:
				print(row)
			elif c == len(main):
				print('Задача не найдена!')
			else:
				c += 1
	if a == '-update':
	    a0 = input('Введите название задачи: ')
	    c = 1
	    for row in main:
	    	if a0 in row[0:10]:
	    		a1 = input('Обновите название задачи: ')
	    		a2 = input('Обновите описание: ')
	    		ma = (row.split('/'))
	    		main.pop((main.index(row)))
	    		main.append(('{0:^9} / {1:^9} / {2:^16} / {3:^16} /     {4}\n'.format(a1, ma[1].strip(), 
	    			ma[2].strip(), ma[3].strip(), a2)))
	    		print('Обновление задачи выполнено успешно!')
	    	elif c == len(main):
	    		print('Задача не найдена!')
	    	else:
	    		c += 1
	if a == '-delete':
		a0 = input('Введите название задачи: ')
		c = 1
		if a0 in row[0:10]:
			main.pop((main.index(row)))
			print('Удаление задачи выполнено успешно!')
		elif c == len(main):
			print('Задача не найдена!')
		else:
			c += 1
	if a == '-done':
		a0 = input('Введите название задачи: ')
		c = 1
		for row in main:
			if a0 in row[0:10]:
				ma = (row.split('/'))
				main.pop((main.index(row)))
				main.append(('{0:^9} / {1:^9} / {2:^16} / {3:^16} /     {4}\n'.format(ma[0].strip(), 'Завершено', 
		    			ma[2].strip(), (str(datetime.datetime.now())[0:16]), ma[4].strip())))
				print('Задача успешно помечена завершенной!')
			elif c == len(main):
				print('Задача не найдена!')
			else:
				c += 1
	if a == '-list':
		for row in main:
			print(row)
	for row in main:
	    f.write(row)