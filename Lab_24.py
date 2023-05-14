

from abc import ABC, abstractmethod
# region First Example

# region Entityies (Varlıklar)
# Bu minik örnekte ki varlıklarımızı tanımlıyoruz. Entity'ler sadece class ve object attribute'leri barındırırlar. Yani fonksiyon ve method barındırmazlar. Bu bir best practice'dir.


class BaseMuzikAleti:
    def __init__(self, model, brand):
        self.brand = brand
        self.model = model


class Gitar(BaseMuzikAleti):
    def __init__(self, model, brand):
        super(Gitar, self).__init__(model, brand)


class Keman(BaseMuzikAleti):
    def __init__(self, model, brand):
        super(Keman, self).__init__(model, brand)


class Muzisyen:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.caldigi_enstruman = []
# endregion

# abstraction (soyutlama)
class BaseRepository(ABC): # BaseRepository isimli sınıfımız artık soyut bir sınıftır. Bunun sebebi ise ABC metaclass'ından kalıtım almasıdır.

    @abstractmethod
    def call_sound(self) -> str:
        pass
    # abstract sınıflar içerisinde ki abstract methodlar gövde barındırmazlar. Yani ata sınıfta bu method ne iş yaptığını bilmez.
    # Abstract sınıf içerisinde tanımlanmış abstact methodların burada gövde verilmemesinin sebebi, bu methodların alt sınıflarda farkllı yeteneklerde kullanılacak olmasıdır. Yani override edip farkı yetenekler vereceğiz. Burada yetenek verseydik habire var olan yeteneğini ezerek ona yeni yetenek vermekle uğraşacaktık.

    def hello_eveyone(self):
        print("Hi..!")
    # Abstract ata sınıflar içerisinde abstract olmayan methodlar tanımlayabiliriz. Buradaki mantık. abstract işaretlenmemiş methodların her bir alt sınıfta override edilmeyerek var olan ham yeteneği ile kullanılması ve gerekli görülen yerlerde override edilerek alt sınıfta yetenek kazandırılmasıdır.


# TypeError: Can't instantiate abstract class BaseRepository with abstract method call_sound
# abstract sınıflardan örneklem çıkartılamaz
# repo = BaseRepository()


class KemanRepository(BaseRepository):

    def call_sound(self) -> str:
        return "Keman sesi..!"

    @staticmethod
    def harmonize():
        print("Keman akord edildi..!")


class GitarRepository(BaseRepository):

    def call_sound(self) -> str:
        return "Gitar sesi..!"

# 1. Adımda KemanRepository()'den instance aldık: TypeError: Can't instantiate abstract class KemanRepository with abstract method call_sound hatası verdi.
# 2. Adımda aldığımız hatayı düzeltmek için call_sound() methodunu KemanRepository sınıfı içerisine implement ettik
# kemanRepo = KemanRepository()
# print(kemanRepo.call_sound())
# endregion

def main():
    gitar_repo = GitarRepository()
    keman_repo = KemanRepository()

    keman = Keman("Stromberg", "Black Full Set")
    gitar = Gitar("Gonzales", "Ohri Clasical Gitar")

    muzisyen = Muzisyen("Burak", "Saksafoncu")
    muzisyen.caldigi_enstruman.append(keman)
    muzisyen.caldigi_enstruman.append(gitar)

    print(f'Adı: {muzisyen.firstName}\n'
          f'Soyadı: {muzisyen.lastName}\n'
          f'Çaldığı Enstrümanın Adı: {muzisyen.caldigi_enstruman[0].model}\n'
          f'Çaldığı Enstrümanın Modeli: {muzisyen.caldigi_enstruman[0].brand}\n'
          f'Çaldığı Enstrümanın Sesi: {keman_repo.call_sound()}')

    print(f'Adı: {muzisyen.firstName}\n'
          f'Soyadı: {muzisyen.lastName}\n'
          f'Çaldığı Enstrümanın Adı: {muzisyen.caldigi_enstruman[1].model}\n'
          f'Çaldığı Enstrümanın Modeli: {muzisyen.caldigi_enstruman[1].brand}\n'
          f'Çaldığı Enstrümanın Sesi: {gitar_repo.call_sound()}')

    KemanRepository.harmonize()

main()