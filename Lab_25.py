# DÜnyanın farklı lokosyonlarından kahve çekirdeği ithal etmek istiyoruz.
# 4-11 ayları arasında africa'dan ithal edilecek.
# 1 yada 2 yada 12. ayda columbia'dan ithal edilecek
# 3. ayda ise dünyada hasat olmadığı için herhangi bir itahalat işlemi olmayacak.

from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    def ship_from(self) -> str: pass


class FromAfricaRepository(BaseRepository):
    def ship_from(self) -> str:
        return 'from South Africa'


class FromColumbiaRepository(BaseRepository):
    def ship_from(self) -> str:
        return 'from Columbia'


class FromSumatraRepository(BaseRepository):
    def ship_from(self) -> str:
        return 'from Sumatra'


class DefaultRepository(BaseRepository):
    def ship_from(self) -> str:
        return 'not avaliable'


class Shipment:
    @staticmethod
    def shipment_method(month) -> BaseRepository:
        if 4 <= month <= 7:
            return FromAfricaRepository()
        elif 8 <= month <= 11:
            return FromSumatraRepository()
        else:
            if month == 1 or month == 2 or month == 12:
                return FromColumbiaRepository()
            else:
                return DefaultRepository()


def main():
    for month in range(1, 13):
        product_shipment = Shipment.shipment_method(month)
        print(f'Coffee beans shipment {product_shipment.ship_from()}')


main()
