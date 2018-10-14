year_of_founding = 1991
today = 2018
our_departament = ['selling', 'cooking']
class NameExc(Exception):
    pass

class YearExc(Exception):
    pass

class DepartmentExc(Exception):
    pass

class Employee():

    def __init__(self, name, sername, department, year_of_employment):
        self.name = name
        self.sername = sername
        if len(name) < 1 or type(name) != str or len(sername) < 1 or type(sername) != str:
            raise NameExc
        self.year_of_employement = int(year_of_employment)
        if year_of_employment < year_of_founding or year_of_employment > today:
            raise YearExc
        self.departament = department
        if department not in our_departament:
            raise DepartmentExc

try:
    num1 = Employee('Vlad', 'Maksymenko', 'selling', 1990)
except NameExc:
    print('Your name or surname has been entered wrong')
except YearExc:
    print('The year of employment has been entered wrong')
except DepartmentExc:
    print('The department has been entered wrong')

