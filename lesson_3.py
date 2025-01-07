""" ООП - Объектно ориентированное программирование """
" Инкапсуляция "

class PublicExample: # Публичный класс
    def __init__(self, value):
        self.value = value # Публичный атрибут
        
    def info(self):
        return self.value # Публичный метод
    
public = PublicExample("Публичный класс")
# print(public.info()) # Вызов публичного метода
# print(public.value) # Доступ к публичному атрибуту


class ProtectedExample: # Защищенный класс
    def __init__(self, value):
        self._value = value # Защищенный атрибут 
        
    def _info(self):
        return self._value # Защищенный метод

protected = ProtectedExample("Защищенный класс")

# print(protected._info()) # Это работает, но противоречит принципам инкапсуляции 
# print(protected._value) # Можно получить значение на прямую, но это не рекомендуется 


class PrivateExample: # Приватный класс
    def __init__(self, value):
        self.__value = value # Приватный атрибут 
        
    def __info(self):
        return self.__value # Приватный метод 
    
    def access_private(self):
        return self.__info()  # Публичный метод, где мы получаем доступ к приватному методу или атрибуту
    
private = PrivateExample("Приватный класс")
# Прямой вызов приватного метода вызовет ошибку
# print(private.__info())  

# Прямой вызов атрибута вызовеь ошибку
# print(private.__value)

# Доступ через публичный метод 
# print(private.access_private())

# Доступ к приватному атрибуту либо методу через name mangling
# print(private._PrivateExample__info())

import datetime

class Car: 
    def __init__(self, marka, model, year, mileage):
        self.marka = marka
        self.model = model
        self._year = year
        self.__mileage = mileage
        
    def info(self):
        return f"Марка - {self.marka}\nМодель - {self.model}"
    
    def _calculate_age(self):
        current = datetime.datetime.now().year
        return f"Возраст машины - {current - self._year}"
    
    def __update_mileage(self, mileage_update = 1000):
        self.__mileage = mileage_update
        return self.__mileage
    
    def set_mileage(self):
        return self.__update_mileage()
    
car = Car("Mazda", 'RX8', 2011, 140000)
print(car.info())
print(car._calculate_age())
print(car.set_mileage())