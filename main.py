from datetime import date


class Person:

    def __init__(self, name, birthday):
        self.name = name
        self.birthdate = birthday

    @property
    def birthdate(self):
        return self._birthdate

    @birthdate.setter
    def birthdate(self, new_birthday):
        """
        Tato metoda nám pomohá zachovat soulad mezi birthday, age a is_adult.
        """
        self._birthdate = new_birthday
        self.__age = self.calculate_age()
        self.__is_adult = self.__age >= 18

    @birthdate.deleter
    def birthdate(self):
        """
        Tato metoda nám pomohá zachovat soulad mezi birthdate, age a is_adult.
        """
        del self._birthdate
        del self.__age
        del self.__is_adult

    def calculate_age(self):
        """
        Tato metoda vypočítá věk osoby na základě data narození.
        """
        diff = date.today() - self._birthdate
        return round(diff.days / 365, 1)

    def choose_beverage(self):
        """
        Tato metoda rozhodne, co bude daná osoba pít na základě vypočítáného věku
        """
        return "You'll get a glass of good wine!" if self.__is_adult else "You'll get some fresh water!"