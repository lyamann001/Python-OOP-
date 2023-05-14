
# Person isimli bir sınıf oluşturalım. FirstName, LastName, Departmant, Salary object attribute'leri olsun. ShowInformation fonksiyonu olsun.
# employee listesi oluşturalım. Bu listenin item'ları Person sınıfından kalıtım alınmış olan objeler olsun.
# HumanResource isimli bir sınıf oluşturalım. ChangeDepartmant fonksiyonu olsun dışarıdan aldıüı çalışan adı üzerinden kişi bularak birimini güncelleme yeteneği olsun.
# Manager isimli bir sınıf oluşturalım. AdditialSalary fonksiyonu olsun dışarıdan aldığı çalışan adı üzerinden kişiyi bularak maaşına zam yapsın

lstPerson = []


class Person:
    def __init__(self, firstName, lastName, department, salary):
        self.salary = salary
        self.department = department
        self.lastName = lastName
        self.firstName = firstName

# region Fake Data
p1 = Person('Burak', 'Yilmaz', 'ARGE', 20000)
p2 = Person('İpek', 'Yilmaz', 'Art Historian', 0)
p3 = Person('Hakan', 'Yilmaz', 'Chemist', 18000)
# endregion

class HumanResource(Person):
    def __init__(self, *args, **kwargs):
        super(HumanResource, self).__init__(*args, **kwargs)

    def createEmployee(self, newEmployee: Person):
        lstPerson.append(newEmployee)
        print('Employee has been added..!')

    def listEmployees(self):
        for person in lstPerson:
            print(f'First Name: {person.firstName}\nLast Name: {person.lastName}\nDepartment: {person.department}\nSalary: {person.salary}')

    def changeDepartment(self, firstName: str, newDepartment: str):
        for person in lstPerson:
            if person.firstName == firstName:
                person.department = newDepartment
                print(f'{person.firstName} {person.lastName} department has been changed..!')
                break
        else:
            print(f'No person named {firstName} was found..!')

    def employeeDetail(self, firstName: str):
        for person in lstPerson:
            if person.firstName == firstName:
                print(f'First Name: {person.firstName}\nLast Name: {person.lastName}\nDepartment: {person.department}\nSalary: {person.salary}')
                break
        else:
            print(f'No person named {firstName} was found..!')

    def deleteEmployee(self, firstName: str):
        for person in lstPerson:
            if person.firstName == firstName:
                lstPerson.remove(person)
                print(f'{person.firstName} has been removed..!')
                break
        else:
            print(f'No person named {firstName} was found..!')

h1 = HumanResource("Ayşe","Yıldız","IK",12)
h1.createEmployee(p1)
h1.createEmployee(p2)
h1.createEmployee(p3)
h1.listEmployees()
h1.changeDepartment(
    input('Please type into employee name: '),
    input('Please type into new department: ')
)
h1.employeeDetail('Burak')