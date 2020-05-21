from abc import ABC
from abc import abstractmethod

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    @abstractmethod

    def __init__(self, code, name, salary):
        if (type(self) == Employee):
            raise TypeError(
                'A classe Employee não deve ser instanciada diretamente')

        self.code = code
        self.name = name
        self.salary = salary

    def calc_bonus(self):
        pass

    def get_hours(self):
        return 8

    def get_department(self):
        return self.__departament.name

    def set_department(self, name, code):
        self.__departament = Department(name, code)


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('sellers', 2)
        self.__sales = 0

    def calc_bonus(self):
        return self.__sales * 0.15

    def get_sales(self):
        return self.__sales

    def put_sales(self, value):
        self.__sales += value
