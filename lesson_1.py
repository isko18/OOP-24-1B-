""" ООП - Объектно ориентированное программирование """

helo_world = "Geeks" #Змеинный регистр

HelloGeeks = "Geeks" #Верблюжий регистр

# def material_icon(num1: int, num2: int)-> int:
#     return num1 * num2

# print(material_icon())

# def material_icon(name, age, direction='FullStack'):
#     print(f"Привет, меня зовут {name}, мне {age}, направление {direction}")
    
# material_icon('Islam', 20)

# class Car: # Шаблон или чертеж 
#     def __init__(self, wheel, motor, body): # __init__ - это конструктор
#         self.wheel = wheel
#         self.motor = motor # self - ссылка на текущий объект
#         self.body = body # атрибут класса
        
#         self.bak = 10
#         self.is_start = False
        
#     def info(self): # Функция внутри класса превращается в метод
#         print(f'Колесо - {self.wheel}, Мотор - {self.motor}, Кузов - {self.body}')
        
#     def start(self):
#         if self.bak > 0:
#             self.is_start = True
#             print("Машина заведена")
#         else:
#             print("У машины нет топлива")
            
#     def stop(self):
#         self.is_start = False
#         print("Машина заглушена")
        
#     def drive(self, city):
#         if self.is_start == True:
#             print(f"Машина едет в {city}")
#         else:
#             print("Машина не заведена")

# car = Car('R20', 'V8', 'khan') # экземпляр класса
# car.info() # вызов метода, обращаясь к экземпляру 
# # car.start()
# # car.stop()
# car.drive("Дубай")
    
    
name = ("Asko", "Isko", "Sema")
list_example = list(name)
list_example.append("Aslan")
name = tuple(list_example)
print(name)