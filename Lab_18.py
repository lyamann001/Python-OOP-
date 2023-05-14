# Inheritance (Kalıtım)
# Yazılımda ki kalıtım mantığı ile biyolojideki kalıtım mantığı aynıdır. Nasıl ki biz atalarımızdan kalıtım yoluyla bazı özellik ve yetenekleri kazanıyorsak, yazılımda da üst sınıflardan yani ata sınflardan alt sınıflar kalıtım yaklaşımıyla yetenek ve özellik kazanmaktadır.
# Bir çok programlama dili çoklu kalıtımı desteklemeyip çoklu kalıtım için arayüzleri kullanırken, Python çoklu kalıtımı direk olarak uygulamaktadır. Çoklu kalıtım ise bir alt sınıfın birden fazla ata sınıftan kalıtım almasıdı.
"""
class person:
    age = 0

    def __init__(self, first_name, last_name):
        self.firstName = first_name
        self.lastName = last_name
        print("Person has been created..!")

    def getFullName(self) -> str: return self.firstName+" "+self.lastName

    def isEmployee(self, param: bool) -> bool: return param

    def metaInformation(self): print(dir(person))

person_1 = person("Burak", "Yılmaz")
person_1.metaInformation()
# yukarıdaki method ile "person sınıfının" bilgilerini ekrana bastık
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'getFullName', 'isEmployee', 'metaInformation'],
# yukarıda ki çıktı incelendiğinde bizim oluşturmadığımız bir çok yapı görüyoruz. Bu yapılar, Python içerisinde gömülü olarak bulunan ve diğer bütün sınıflara kalıtım veren "object" sınıfından gelmektedi.
print(person_1.getFullName())
print(person_1.isEmployee(True))

# burada employee sınıfımız "person" sınıfından kalıtım yoluyla person sınıfının tüm özelliklerini aldı.
class employee(person):
    pass

employee_1 = employee("Hakan", "Yılmaz")
print(employee_1.getFullName())
print(employee_1.isEmployee(False))
employee_1.metaInformation()
# 33, 34 ve 35. satırlarda person sınıfında tanımladığımız özellikleri kullanabildik. bunu yapabilmemizin arkasındaki mantık kalıtımdır.

"""


# Employee sınıfı oluştıralım. bu sınıfın özellikleri first_name, last_name, salary, departmant object attribute'leri olsun. birde show_information methodu yani yeteneği olsun.
# human_resource adında bir sınıf oluşturalım. employee sınıfından kalıtım alsın. change_departmant yeteneği olsun.
# manager sınıfı olsun. bu sınıfta employee'den kalıtım alsın. additional_salary ve cut_salary yetenekleri olsun.


class employee:
    def __init__(self, first_name, last_name, salary, department):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.department = department

    def show_information(self):
        print(f"""
        Informaiton
        -----------
        First Name: {self.first_name}
        Last Name: {self.last_name}
        Salary: {self.salary}
        Department: {self.department}
        """)


class human_resource(employee):
    def change_department(self, new_department):
        self.department = new_department


class manager(employee):
    def additional_salary(self, amount):
        self.salary += amount

    def cut_salary(self, amount):
        self.salary -= amount


calisan = employee("Burak", "Yılmaz", 1000, "ARGE")
ik = human_resource("İpek", "Yılmaz", 2000, "IK")
yonetici = manager("Hakan", "Yılmaz", 3000, "Müdür")

calisan.show_information()
yonetici.additional_salary(100)
yonetici.show_information()
ik.change_department("ARGE")
ik.show_information()

# Enums
# Uygulamada ki sabitlerimizi tanımladığımız bir yapıdır. Listelere benzete biliriz. Kendi index mekanizması vardır. Yani bir enum'daki ifadelere bir değer vermezsek otomatik olarak sıfırdan başlayarak değer atar.

import enum, datetime, uuid


class status(enum.Enum):
    Active = 1
    Modified = 2
    Passive = 3

# uygulamalarda base, core, kernel olarak isimlendirilen sınıflar ata sınıftır yani uygulamada ki bütün sınıflar bu sınıftan kalıtım alır.
class base_entity:
    def __init__(self, id, name, create_date, condition):
        self.id = id
        self.name = name
        self.create_date = create_date
        self.condition = condition

    def show_information(self):
        print(f"""
        Information
        -----------
        Id: {self.id}
        Name: {self.name}
        Create Date: {self.create_date}
        Condition: {self.condition}
        """)


class product(base_entity):
    def __init__(self, id, name, create_date, condition, price, stock):
        super().__init__(id, name, create_date, condition)
        self.price = price
        self.stock = stock

    def show_information(self):
        super().show_information()
        print(f"""
        Price: {self.price}
        Stock: {self.stock}
        """)

urun = product(uuid.uuid4(), "Boxing Gloves", datetime.datetime.now(), status.Active.name, 10, 34)
urun.show_information()

# BasePhone sınıfımız olsun, phone_id, brand, model, price. show_information ve phone_ring_sound fonksiyon olsun. phone_ring_sound() fonksiyonu genel telefon sesi return edecek
# Nokia, Samsung, Iphone alt sınıfları basephone'dan kalıtım alsın.
# Nokia sınıfında phone_ring_sound() fonksiyonu nokai telefon sesi return edecek
# Samsung sınıfında phone_ring_sound() fonksiyonu samsung telefon sesi return edecek
# Iphone sınıfında phone_ring_sound() fonksiyonu iphone telefon sesi return edecek
# show_information fonksiyonu ise her bir alt sınıfta ekstara yeni bir bilgi ekrana yazdırsın

class basephone:
    def __init__(self, phone_id, brand, model, price):
        self.phone_id = phone_id
        self.model = model
        self.brand = brand
        self.price = price

    def show_information(self):
        return f"Id: {self.phone_id}\nModel: {self.model}\nBrand: {self.brand}\nPrice: {self.price}"

    def phone_ring_sound(self):
        return "Genel telefon sesi..!"

class samsung(basephone):
    def __init__(self, operating_system, phone_id, brand, model, price):
        super(samsung, self).__init__(phone_id, brand, model, price)
        self.operating_system = operating_system

    def phone_ring_sound(self):
        return f"Samsung telefon sesi..!"

    def show_information(self):
        return f"{super().show_information()}\nOperating System: {self.operating_system}"

samsung = samsung("Vodofone", uuid.uuid4(), "Samsung", "S10", 130)
print(samsung.show_information())
print(samsung.phone_ring_sound())

class nokia(basephone):
    def __init__(self, anten, phone_id, brand, model, price):
        super(nokia, self).__init__(phone_id, brand, model, price)
        self.anten = anten

    def show_information(self):
        return f"{super().show_information()}\nAnten: {self.anten}"

    def phone_ring_sound(self):
        return "Nokia telefon sesi..!"

nokia = nokia(True, uuid.uuid4(),"Nokia","3310",10)
print(nokia.show_information())
print(nokia.phone_ring_sound())


# Çok minnak fatura ödeme uygulaması
# Fatura_Adi, kullanım_bedeli, kdv
# fatura_hesapla fonksiyonu
# su faturası mill paramtre
# elektrik faturasında kw
# dogal gaz'da m3

class BaseBill:
    def __init__(self, adi, bedel, kdv=20):
        self.adi = adi
        self.bedel = bedel
        self.kdv = kdv

    def hesapla(self):
        return self.bedel * self.kdv

class ElektrikFaturasi(BaseBill):
    def __init__(self, kw, adi, bedel, kdv):
        super(ElektrikFaturasi, self).__init__(adi, bedel, kdv)
        self.kw = kw

    def hesapla(self):
        return super(ElektrikFaturasi, self).hesapla() * self.kw

class SuFaturasi(BaseBill):
    def __init__(self, mill, adi, bedel, kdv):
        super(SuFaturasi, self).__init__(adi, bedel, kdv)
        self.mill = mill

    def hesapla(self):
        return super(SuFaturasi, self).hesapla() * self.mill

class DogalGaz(BaseBill):
    def __init__(self, m3, adi, bedel):
        super(DogalGaz, self).__init__(adi, bedel)
        self.m3 = m3

    def hesapla(self):
        return super(DogalGaz, self).hesapla() * self.m3

# Base sınıfta kdv değerine default değer verdik. doğal gaz faturasında bu defult değeri kullanmasını istediğimizden doğal gaz faturasında kdv argümanını init methodundan sildik ve aşağıda değer vermedik
dogalgaz = DogalGaz(10, "İgdaş", 30,)
print("Sonuç: ",dogalgaz.hesapla())

# burada default kdv yerine farklı bir kdv değeri kullanmak istediğimizden init methodunda kdv değerini silmedik ve aşağıda değer gönderdik.
su = SuFaturasi(10, "İski", 20, 20)
print("Sonuç: ", su.hesapla())