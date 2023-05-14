#region OOP Introduction
"""
# Object Oriented Programming (Nesne Yönelimli Programlama)
# Python programlama dili içerisinde bulunmayan objeleri yaratmamıza olanak tanıyan bir yazılım yaklaşımıdır. Python bugüne kadar random, request, int, dictionary gibi birçok objeyi tanımıştık. Artık kendi objelerimizi yaratabileceğiz.
# OOP, birkaç tane yazılım prensibini hayatımıza sokmuştur. Bunlar:
# 1. Kalıtım (Inheritane),
# 2. Veri gizleme (Encapsulation),
# 3. Çok biçimlilik (Polymorphisim),
# 4. Soyutlanma (Abstraction)

# Yukarıda kendi objelerimizi yaratmaktan bahsettik. Bunu nasıl yapacağız?
# İlk önce yaratacağımız objenin özelliklerini temsil edecek bir sınıf (class) yani yaratılacak objenini prototype'nı oluşturacağız.
class vehicle:
    engine_size = 0
    torque = 0
    model = ""
    brand = ""
    cylinder = 0
# yukarıda bir sınıf vasıtasıyla bir prototype oluşturduk. Artık vehicle isimli sınıf vasıtasıyla istediğimiz yerde istediğimiz kadar araç nesnesi yaratabileceğiz.
car = vehicle() # vehicle sınıfından örneklem(instance) çıkardık yada aldık diyebiliriz. Böylelikle "car" objemizi yaratmış olduk.
car.brand = "Dodge"
car.model = "TRX 1500"
car.engine_size = 4.3
car.cylinder = 6
car.torque = 10
# artık istediğimiz kadar araç yaratabiliriz
car_1 = vehicle()
car_1.brand = "Honda"
car_1.model = "Civik"
car_1.engine_size = 2
car_1.cylinder = 3
car_1.torque = 2

print(f"Model: {car.model}\nBrand: {car.brand}\nEngine Size: {car.engine_size}\nCylinder: {car.cylinder}\nTorque: {car.torque}")

"""


#endregion

#region Constructor (Yapıcı Method)
# Az önce yaptığımız örnekte bir şey dikkatinizi çekmiştir. Mesela vehicle yazdığımızda yanında parantez sembolleri vardı. bunun anlama biz örneklem çıkartırken sınıfımızın içerisinde gömülü olarak bulunan yapıcı methodu çağırarak sınıfımız yaratmaya yada kullanamaya hazırlıyoruz. Aslında sınıfımızı başlatıyoruz (initialize).
"""
class person:
    # class attribute
    address = "no information"

    # constructor method
    def __init__(self, name, year): # person sınıfından örneklem alırken bizden zorunlu olarak bir name ve year bilgisi isteyecek. bu bilgiler ile sınıfı initialize edecek.
        #object attribute
        self.name = name
        self.year = year
        print("__init__ methodu bu sınıftan örneklem çıkarıldığında otomatik olarak çalışacak. çalışmak için bize sormayacak. otomatik tetiklenecektir. Otomatik tetiklendiği için içerisindeki görevleride yerine getirecektir.")

insan = person("Burak", 1989) # burada örneklem alırken __init()__ methodu otomatik olarak tetiklenmektedir.
insan.address = "Bakırköy"
print(f"Name: {insan.name}\nBirth Date: {insan.year}\nAddress: {insan.address}")

human = person(
    input("Please type name: "),
    int(input("Please type year: "))
)
print(f"Name: {human.name}\nBirth Date: {human.year}\nAddress: {human.address}")
"""
class circle:
    pi = 3.14 # class attribute

    def __init__(self, yaricap = 1):
        self.yaricap = yaricap # object attribute

    # aşağıda ki fonksiyonlara instance fonksiyon olarak isimlendiriyoruz çünkü ilgili sınıftan nesne ürettikten sonra yani ilgili sınıftan instance aldıktan sonra bu fonksiyonlara erişip kullanabiliyoruz.
    # instance fonksiyon
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap

    # instance fonksiyon
    def alan_hesapla(self):
        return self.pi * self.yaricap ** 2

c1 = circle()
print(f"Cevre: {c1.cevre_hesapla()}")
print(f"Alan: {c1.alan_hesapla()}")
print(circle.pi)

class student:
    def __init__(self, student_id, first_name, last_name):
        self.id = student_id
        self.firstName = first_name
        self.lastName = last_name

    #instane method
    def show_information(self):
        print(f"""
        Öğrenci Bilgileri
        -----------------
        No: {self.id}
        Adı: {self.firstName}
        Soyadı: {self.lastName}
        """)

student_1 = student(1, "Burak", "Yılmaz")
student_1.show_information()

class teacher:
    adi= ""
    soyadi = ""

    def assigned_value(self, first_name, last_name):
        self.adi = first_name
        self.soyadi = last_name

    def show_information(self):
        print(f"""
        Öğretmen Bilgileri
        -----------------
        Adı: {self.adi}
        Soyadı: {self.soyadi}
        """)

teacher_1 = teacher()
teacher_1.assigned_value("hakan", "yılmaz")
teacher_1.show_information()

class departmant:
    """
    class documentation
    """
    departmant_type = "Yazılım"
    person_count = 0

    def __init__(self, name, age):
        self.adi = name
        self.yas = age
        departmant.person_count += 1 # bu sınıftan her örneklem çıkarıldığında bu sınıf attribute 1 artacak
        self.show_employee_count()

    def show_employee_count(self):
        """
        Departmanda kaç kullanıcı varsa miktarını ekrana basar
        """
        print(f"Total Employee Count: {self.person_count}")

    def show_information(self):
        print(f"""
        Adı: {self.adi}
        Yaşı: {self.yas}
        Departman: {self.departmant_type}
        """)

# orneklem çıkartıyoruz (instance)
employee_1 = departmant("Burak", 33)
employee_1.departmant_type = "ARGE"
employee_1.show_information()
employee_1.show_employee_count()

employee_2 = departmant("Hakan", 36)
employee_2.departmant_type = "Amele"
employee_2.show_information()
employee_2.show_employee_count()

# software_developer adında bir sınıf oluşturalım. bu sınıfın liste tipinde developer_languge, first_name, last_name adında object attribute'leri olacak. add_new_language ve show_information adında yetenkleri
class software_developer:
    def __init__(self, first_name, last_name, language):
        self.developer_language = []
        self.first_name = first_name
        self.last_name = last_name
        self.split_to_language(language)

    def show_information(self):
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}\nLanguage: {self.developer_language}")

    def split_to_language(self, language):
        language_lst = language.split(',')
        for language in language_lst:
            self.developer_language.append(language.lstrip())

    def add_new_language(self, new_language):
        print("processing...!")
        print("New language has been added..!")
        self.split_to_language(new_language)

developer_1 = software_developer(
    input("First Name: "),
    input("Last Name: "),
    input("Language: ")
)
developer_1.show_information()
developer_1.add_new_language("RPA, Go")
developer_1.show_information()
#endregion

# character bir sınıfımız olsun. sınıfın özellikleri, name, race, role, level, weapon, armour, hp.
# saldir, korun, kaç yetenekleri olsun.
# saldırıken level + weapon
# korunurken armour + level kadar korun
class character:
    def __init__(self, name="", race="", role="", level=0, weapon=0, armour=0, hp=100):
        self.name = name
        self.race = race
        self.role = role
        self.level = level
        self.weapon = weapon
        self.armour = armour
        self.hp = hp

    def saldir(self):
        return self.level + self.weapon

    def korun(self):
        return self.level + self.armour

    def kac(self):
        print("Dövüşten kaçtı..!Korkak..!")

kara_murat = character("Kara Murat","Turk","Akıncı",10,5,10,100)
viking = character("Raider","Viking","Asker",8,50,40,100)
tur = 1

while True:
    action = input("for attack --> 'a'\nfor defend --> 'd'\nfor escape --> 'e'\nChoose your action: ")

    if action == 'e':
        viking.kac()
        break
    elif action == 'a':
        kara_murat.hp -= viking.saldir() - kara_murat.korun()
        viking.hp -= kara_murat.saldir() - viking.korun()

        print("=================")
        print(f"Tur: {tur}")
        print(f"{viking.name} verdiği hasar --> {viking.saldir() - kara_murat.korun()}")
        print(f"{kara_murat.name} verdiği hasar --> {kara_murat.saldir() - viking.korun()}")
        print("=================")
        print(f"{viking.name} kalan hp --> {viking.hp}")
        print(f"{kara_murat.name} kalan hp --> {kara_murat.hp}")

    if kara_murat.hp <= 0 and viking.hp > 0:
        print(f"{viking.name} kazandı..!")
        break
    elif kara_murat.hp > 0 and viking.hp <= 0:
        print(f"{kara_murat.name} kazandı..!")
        break
    elif kara_murat.hp <= 0 and viking.hp <= 0:
        print("Bu dünya kimseye kalmaz..! Savaşma .....")
        break
    tur += 1



