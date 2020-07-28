'''
Классы для работы с банковскими операциями и клиентами!

>>> tr14_07 = Transaction(100, '14-07-2020', currency = 'EUR', ex_rate = 1.14, desc = 'For my pal for his bday)')
>>> tr14_07.amount()
100

>>> tr14_07.date()
14-07-2020

>>> tr14_07.currency()
EUR

>>> tr14_07.usd_convertion_rate()
1.14

>>> tr14_07.usd()
114

>>> tr14_07.description()
For my pal for his bday)

>>> a = Account('12345', 'For Holidays')
>>> a.balance()
0

>>> len(a)
0

>>> a.apply(tr14_07)
>>> len(a)
1

>>> tr14_08 = Transaction(150, '14-08-2020', currency = 'EUR', ex_rate = 1.14, desc = 'For another pal for his bday)')
>>> tr14_09 = Transaction(200, '14-09-2020', currency = 'USD', ex_rate = 1, desc = 'For my own bday)')
>>> tr14_10 = Transaction(300, '14-10-2020', currency = 'USD', ex_rate = 1, desc = 'For someone else bday)')

>>> a.apply(tr14_08)
>>> a.apply(tr14_09)
>>> a.apply(tr14_10)

>>> len(a)
4

>>> a.save()
>>> a.load(12345)
>>> a.remove(12345)
'''
import os
import pickle

class Transaction:

	def __init__(self, amount, date, currency = 'USD', ex_rate = 1, desc = None):
		self.__amount = amount
		self.__date = date
		self.__currency = currency
		self.__ex_rate = ex_rate
		self.__desc = desc

	def amount(self):
		print(self.__amount)

	def date(self):
		print(self.__date)

	def currency(self):
		print(self.__currency)

	def usd_convertion_rate(self):
		print(self.__ex_rate)

	def description(self):
		print(self.__desc)

	def usd(self):
		print(round(self.__amount * self.__ex_rate))

class Account:

	def __init__(self, acc_number, acc_name, trans_list = []):
		self.__acc_number = acc_number
		self.trans_list = trans_list
		self.length = len(self.trans_list)
		if len(acc_name) < 4:
			print('Account name cannot be shorter than 4 symbols!')
			exit
		else:
			self.acc_name = acc_name

	def __len__(self):
		return len(self.trans_list)

	def balance(self):
		bal = 0
		for i in self.trans_list:
			bal += i.usd()
		return(bal)

	def all_usd(self):
		for i in self.trans_list:
			if i.currency() != 'USD':
				return False 
			return True

	def apply(self, trans):
		self.trans_list.append(trans)

	def save(self):
		with open(f'{self.__acc_number}.acc', 'wb') as f:
			pickle.dump(self, f)

	def load(self, name):
		with open(f'{name}.acc', 'rb') as f:
			# self =  pickle.load(f)
			return pickle.load(f)

	def remove(self, name):
		path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{name}.acc')
		os.remove(path) 

if __name__ == '__main__':
    import doctest
    doctest.testmod()