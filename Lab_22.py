
# Multiple Inheritance (Çoklu Kalıtım)
"""
class GrandFather:
    def greet(self):
        print("hello foks")


class Father:
    def hello(self):
        print("salve..!")


class Child(GrandFather, Father):
    def greetPeople(self):
        print("No war..!Only Peace..!")


burak = Child()
burak.greet()
burak.hello()
burak.greetPeople()

"""

# Kernel sınıf oluşturuyoruz. Bu Kernel isimli sınıfın sadece id attribute encapsule olacak şekilde oluşturualcak.
# BaseEntity sınıfı oluşturuyoruz. Bu sınıfta Status, CreateDate attribute'leri encapsule olacak şekilde oluşturualcak.
# Role isimli bir enum oluşturalım. Admin, Employee, Member
# AppUser sınıfı oluşturalım. Bu sınıf Kernel ve BaseEntity sınıflarından kalıtım alsın. FirstName, LastName, UserName, Password ve Age bilgileri olsun. Age encapsule edelim.
import enum
from uuid import uuid4
from datetime import datetime


class Status(enum.Enum):
    Active = 1
    Modified = 2
    Passive = 3


class Role(enum.Enum):
    Admin = 1
    Author = 2
    Member = 3


class Kernel:
    def __init__(self):
        self.__id = ""

    def setKernelValue(self):
        self.__id = uuid4()

    def getKernelValue(self):
        print(f'Id: {self.__id}')


class BaseEntity:
    def __init__(self):
        self.__status = ""
        self.__createDate = ""

    def setBeseEntityValue(self):
        self.__status = Status.Active.name
        self.__createDate = datetime.now()

    def getBaseEntityValue(self):
        print(f'Create Date: {self.__createDate}Status: {self.__status}')


class AppUser(Kernel, BaseEntity):
    def __init__(self, firstName, lastName, userName, password):
        super(AppUser, self).__init__()
        super(AppUser, self).__init__()
        self.password = password
        self.userName = userName
        self.lastName = lastName
        self.firstName = firstName
        self.__role = ""
        self.__age = 0

    def setAppUserValue(self, age):
        super(AppUser, self).setKernelValue()
        super(AppUser, self).setBeseEntityValue()
        self.__role = Role.Member.name
        if age > 18:
            self.__age = age
            print("Membership process has been completed..!")
            print(f'Account Information')
            print(f'===================')
            super(AppUser, self).getKernelValue()
            super(AppUser, self).getBaseEntityValue()
            print(f'First Name: {self.firstName}')
            print(f'Last Name: {self.lastName}')
            print(f'User Name: {self.userName}')
            print(f'Password: {self.password}')
            print(f'Role: {self.__role}')
            print(f'Age: {self.__age}')
        else:
            print("Your age is not valid this club..!")


user = AppUser("Burak", "Yilmaz", "beast", "123")
user.setAppUserValue(33)