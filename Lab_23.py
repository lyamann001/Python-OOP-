
# Abstraction (Soyutlama)
# OOP prensipleri içerisinde en önemli olanıdır.
# Özelllikle web projelerinde, çok karmaşık kodlara uygulanan yazılım prensipleri (SOLID) ve tasarım desenleri içerisinde soyutlama kullanılmaktadır.
# Soyutlamadaki ana mantık ata sınıfların soyutlanmasıdır. Yani alt sınıflara method ve fonksiyon aktarmakla görevli olan ata sınıfların soyutluyoruz ki her bir alt sınıfta onları farklı biçimlerde yada özelliklerde kullanabillelim.
# Soyutlama kullanmamızda ki bir diğer neden ata sınıf ile alt sınıf arasında oluşan bağımlılıkları kırmaktır.
# Bu bağımlılıkları kırmak için DIP (Dependency Inversion Principle) ve IoC (Inversion of Control) gibi prensipler kullanılmaktadır. BU prensiplerin ilk adımı soyutlama kullanılmasıdır.


# Not: Soyutlamaya geçmeden önce bir kaç konuyu halletmemiz gerekmektedir. BUnlardan birincisi decorator ikincisi ise metaclass'tır.

# 1. Decorator
# Python'da kullanılan bir keyword'tür. Uygulamalarımızda var olan method ve fonksiyonları decore ederek onlara yeni özellikler kazandırmaya yaramaktadır.
# Python içerisinde built-in bir çok decorator bulunmaktadır. "@staticmedtod", "@abstractmethod" vb.
# Python içerisinde ihtiyaçlarımıza yönelik olarak custom decorator oluşturabiliriz.

#region Örnek -1
def uppercase_name(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper()


def get_fullname():
    return 'mike tyson'


print(uppercase_name(get_fullname))


@uppercase_name
def get_name():
    return "burak yilmaz"


print(get_name)
#endregion

# region Ornek -2
def my_decorator(func):
    def wrapper(name):
        print("Fonsiyondan önceki işlemler")
        func(name)
        print("fonksiyondan sonraki işlmeler")

    return wrapper


@my_decorator
def sayHello(name):
    print("Hello", name)


sayHello("Burak")
#endregion

# region Ornek - 3
# math modülünden pow, faktoriel, toplama işlemeleri yapılırken arada geçen süreyi ekrana yazdıracak bir decorator (calculate_time) oluşturalım
import math, time


def calculate_time(func):
    def inner_func(*args, **kwargs):
        start_process = time.time()
        time.sleep(2)
        func(*args, **kwargs)
        finish_process = time.time()
        print(f"=======================\n"
              f"Process: {func.__name__}\n"
              f"Start: {start_process}\n"
              f"End: {finish_process}")

    return inner_func


@calculate_time
def us_alma(a, b):
    print(f"Sonuç: {math.pow(a, b)}")


@calculate_time
def faktoriyel(number):
    print(f"Sonuç: {math.factorial(number)}")


@calculate_time
def toplama(x, y):
    print(f"Sonuç: {x +y}")


us_alma(3, 4)
faktoriyel(5)
toplama(2, 2)



