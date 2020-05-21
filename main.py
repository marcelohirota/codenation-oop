from abc import ABC, abstractmethod

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
   
    @abstractmethod
    def __init__(self, code, name, salary, department):
        if (type(self) == Employee):
            raise TypeError(
                'A classe Employee não deve ser instanciada diretamente')
        self.code = code
        self.name = name
        self.salary = salary
        self.__department = department
        self.workload_employee = 8

    @abstractmethod
    def calc_bonus(self):
        pass

    def get_hours(self):
        return self.workload_employee

    def set_department(self, department, dep_code):
        self.__department = Department(department, dep_code)

    def get_departament(self):
        return self.__department.name


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * 0.15
    

class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    def calc_bonus(self):
        return self.__sales * 0.15

    def get_sales(self):
        return self.__sales

    def put_sales(self, value):
        self.__sales += value