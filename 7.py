"""
Данный класс создан для хранения персональной (смею предположить, корпоративной) информации.

Ниже приведены doc тесты/примеры работы с классом.

>>> Employee = Person('James', 'Holt', '19.09.1989', 'surgeon', '3', '5000', 'Germany', 'Berlin', 'male')
>>> Employee.name
James Holt
>>> Employee.age
29 years old
>>> Employee.work
He is a surgeon
>>> Employee.money
180 000
>>> Employee.home
Lives in Berlin, Germany
"""


class Person:

    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='uknown'):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birth_date = birth_date
        self.__job = job
        self.__working_years = working_years
        self.__salary = salary
        self.__country = country
        self.__city = city
        self.__gender = gender

    @property
    def name(self):
        print(f'{self.__first_name} {self.__last_name}')

    @property
    def age(self):
        a = list(self.__birth_date.split('.'))
        b = 2018 - int(a[2])
        print(f'{b} years old')

    @property
    def work(self):
        ci = {'male': 'He', 'female': 'She', 'uknown': 'He/She'}
        print('{0} is a {1}'.format(ci[self.__gender], self.__job))

    @property
    def money(self):
        m = int(self.__working_years) * int(self.__salary) * 12
        print('{0:,}'.format(m).replace(',', ' '))

    @property
    def home(self):
        print(f'Lives in {self.__city}, {self.__country}')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
