# Encapsulation (Veri Gizleme)
# Sınıfın üyelerine erişimi kısıtlama yada kontrollü bir şekilde erişmek için kullandığımız bir mekanizmadır. Burada ki amaç sınıfın üyesine erişimi sınırlandırmak yani müdahele edilmesini engellemektir. Yada belirli bir şart doğrultusunda bunu yapmaktır.

import datetime, enum, uuid, socket


class Status(enum.Enum):
    Active = 1
    Modified = 2
    Passive = 3

# Not: '__' double underscore bir sınıfın içerisindeki üyeyi dış erişime kapamak için kullanılır. Farklı programlama dillerinde örneğin C#'ta bunun için access modifier olarak adlandırılan 'private' anahtar sözcüğü kullanılır.
class BaseEntity:
    def __init__(self):
        # dışarıdan değer aldığımızda burada methoda parametre olarak veriyorduk. Encapsulation yaptığımızda bunu yapmıyoruz. Çünkü burada tanımlanacak attribute'ler dış erişime kapatıalccak.
        self.__id = "" # id bigisi normalde veri tabanında otomatik olarak üretilir. bu sebepten ötürü burada dış erişime kapadık.
        self.__createDate = ""
        self.__status = ""
        self.__createdComputerName = ""
        self.__createdIpAddress = ""

    def setValues(self):
        self.__id = uuid.uuid4()
        self.__createDate = datetime.datetime.now()
        self.__createdComputerName = socket.gethostname()
        self.__createdIpAddress = socket.gethostbyname(socket.gethostname())

    def showInformation(self):
        print(f'Id: {self.__id}\n'
              f'Create Date: {self.__createDate}\n'
              f'Computer Name: {self.__createdComputerName}\n'
              f'Ip Addess: {self.__createdIpAddress}')

# b1 = BaseEntity()
# b1.setValues()
# b1.showInformation()


class Category(BaseEntity):
    def __init__(self, name, description):
        super(Category, self).__init__()
        self.description = description
        self.name = name

    def showInformation(self):
        super(Category, self).showInformation()
        print(f'Category Name: {self.name}\n'
              f'Description: {self.description}')

# c1 = Category("Boxing Gloves", "You can find best boxing gloves this site..!")
# c1.setValues()
# c1.showInformation()


class Product(BaseEntity):
    def __init__(self, name, description):
        super(Product, self).__init__()
        self.description = description
        self.name = name
        self.__price = 0
        self.__stock = 0

    def setProductValue(self, price, stock):
        super(Product, self).setValues()
        if price >= 0 and stock >= 0:
            self.__stock = stock
            self.__price = price
            self.showInformation()
        else:
            print("Product hasn't been created..!")

    def showInformation(self):
        super(Product, self).showInformation()
        print(f'Product Name: {self.name}\n'
              f'Description: {self.description}\n'
              f'Price: {self.__price}\n'
              f'Stock: {self.__stock}')

p1 = Product("Training Gloves", "Everlast 14inç boxing gloves")
p1.setProductValue(12, 43)