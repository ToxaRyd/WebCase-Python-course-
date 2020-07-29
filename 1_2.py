c = []
count = 0
sum = 0
while  True:
	try:
		a = input('Enter digit: ')
		if a == "":
			print("numbers: ", c)
			print("count = ",count," sum = ",sum," lowest = ",min(c)," highest = ",max(c)," mean = ",sum/count)
			break
		b = int(a)
		c.append(b)
		count += 1
		sum += b
	except ValueError:
		print('Wrong')
		continue
input('Press Enter to finish!')