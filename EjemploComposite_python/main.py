from abc import ABCMeta, abstractmethod, abstractstaticmethod


class IDepartment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, employees):
        """Implement en clase hija"""

    @abstractstaticmethod
    def print_department():
        """inplement en clase hija"""

class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Departamento de Contabilidad: {self.employees}")

class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Departamento de Desarrollo: {self.employees}")

class ParentDepartment(IDepartment):
    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees

    def print_department(self):
       print("Departamento Padre") 
       print(f"Departamento Padre, Empleados Base: {self.base_employees} ")
       for dept in self.sub_depts:
            dept.print_department()
       print(f"Número de empleados totales: {self.employees}")

dept1 = Accounting(200)
dept2 = Development(120)

parent_dept = ParentDepartment(30)
parent_dept.add(dept1)
parent_dept.add(dept2)

parent_dept.print_department()