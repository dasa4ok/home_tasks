year_of_founding = 1991
today = 2018
our_departament = ['selling', 'cooking']
class UniversalException(Exception):
    def __init__(self, text):
        UniversalException.txt = text

class Employee():

    def __init__(self, name, sername, department, year_of_employment):
        try:
            self.name = name
            self.sername = sername
            if len(name) < 1 or type(name) != str or len(sername) < 1 or type(sername) != str:
                raise UniversalException('Your name or surname has been entered wrong')
        except UniversalException:
            print(UniversalException.txt)

        try:
            self.year_of_employement = int(year_of_employment)
            if year_of_employment < year_of_founding or year_of_employment > today:
                raise UniversalException('The year of employment has been entered wrong')
        except UniversalException:
            print(UniversalException.txt)

        try:
            self.departament = department
            if department not in our_departament:
                raise UniversalException('The department has been entered wrong')
        except UniversalException:
            print(UniversalException.txt)


num1 = Employee('Vlad', 'Maksymenko', 'selling', 1990)





