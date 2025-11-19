# region Inheritance ------------------------
'''Ejercicio 1
Crea una clase base Transporte con atributos capacidad y velocidad.
Crea dos subclases: Avion y Barco.
Ambas deben tener un método info() que muestre la información adaptada a cada tipo de transporte.'''

class Transport:
    def __init__(self, capacidad, velocidad):
        self.capacity = capacidad
        self.speed = velocidad

class Airplane(Transport):
    def info(self):
        return f"Avión con capacidad para {self.capacity} pasajeros y velocidad de {self.speed} km/h."

class Boat(Transport):
    def info(self):
        return f"Barco con capacidad para {self.capacity} pasajeros y velocidad de {self.speed} km/h."
    
airplane_1 = Airplane(180, 900)
boat_1 = Boat(300, 40)
print("airplane:", airplane_1.info())
print("boat:", boat_1.info())    

'''Ejercicio 2
Crea una clase Producto con atributos nombre y precio.
Crea dos subclases: Alimento (con atributo caducidad) y Electrodomestico (con atributo garantia).
Haz un método detalle() en cada clase.'''

class Product:
    def __init__(self, nombre, precio):
        self.name = nombre
        self.price = precio

class Food(Product):
    def __init__(self, nombre, precio, caducidad):
        super().__init__(nombre, precio)
        self.expiry_date = caducidad

    def detalle(self):
        return f"Alimento: {self.name}, Precio: {self.price}, Caducidad: {self.expiry_date}"

class Appliance(Product):
    def __init__(self, nombre, precio, garantia):
        super().__init__(nombre, precio)
        self.warranty = garantia

    def detalle(self):
        return f"Electrodoméstico: {self.name}, Precio: {self.price}, Garantía: {self.warranty}"
    
food_1 = Food("Leche", 1.5, "2024-12-31")
appliance_1 = Appliance("Lavadora", 300, "2 años")

print("food", food_1.detalle())
print("appliance", appliance_1.detalle())

'''Ejercicio 3
Crea una clase Persona con nombre y edad.
Crea dos subclases: Profesor (con atributo materia) y Estudiante (con atributo carrera).
Haz que ambos tengan un método presentarse() con mensajes distintos.'''

class Person:
    def __init__(self, nombre, edad):
        self.name = nombre
        self.age = edad

class Teacher(Person):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.subject = materia

    def introduce(self):
        return f"Hola, soy {self.name}, tengo {self.age} años y enseño {self.subject}."
    
class Student(Person):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.major = carrera

    def introduce(self):
        return f"Hola, soy {self.name}, tengo {self.age} años y estudio {self.major}."
    
teacher_1 = Teacher("Juan", 40, "Matemáticas")
student_1 = Student("Ana", 20, "Ingeniería")

print("teacher", teacher_1.introduce())
print("student", student_1.introduce())
# endregion

# region Polymorphism ------------------------
'''Ejercicio 1
Crea una clase Perro y una clase Gato.
Cada una debe tener un método hablar().
Luego recorre una lista de ambos animales e imprime lo que dicen.'''

class Dog:
    def hablar(self):
        return "Guau!"

class Cat:
    def hablar(self):
        return "Miau!"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.hablar())


'''Ejercicio 2
Implementa las clases TarjetaCredito, Paypal y Efectivo, cada una con un método pagar(monto).'''
class CreditCard:
    def pay(self, monto):
        return f"Pagando {monto} con Tarjeta de Crédito."
    
class Paypal:
    def pay(self, monto):
        return f"Pagando {monto} con PayPal."
    
class Cash:
    def pay(self, monto):
        return f"Pagando {monto} en efectivo."   

payment_methods = [CreditCard(), Paypal(), Cash()]
for method in payment_methods:
    print(method.pay(500))     


'''Ejercicio 3
Crea una clase Figura con un método area().
Luego define Rectangulo y Circulo que sobrescriban area().
Recorre una lista con diferentes figuras y muestra su área.'''

import math
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)
    
shapes = [Rectangle(4, 5), Circle(5.5)]

for shape in shapes:
    print(f"Área: {shape.area()}")

'''Ejercicio 4
Crea una clase Pato con un método sonido() y otra clase Persona que también tenga sonido().
Crea una función hacer_sonido(obj) que ejecute obj.sonido().
Prueba la función con ambas clases.'''
class Duck:
    def sonido(self):
        return "I'm a duck Cua Cua!"
class PersonSound:
    def sonido(self):
        return "Hi i'm a person!"    
    
def make_sound(obj):
    print(obj.sonido())

make_sound(Duck())
make_sound(PersonSound())

'''Ejercicio 5
Crea clases Gerente y Programador, ambas con un método reportar().
Haz una lista de empleados y llama a reportar() en cada uno.'''

class Manager:
    def report(self):
        return "El gerente está reportando el progreso del proyecto."
class Programmer:
    def report(self):
        return "El programador está reportando el código desarrollado."
employees = [Manager(), Programmer()]
for employee in employees:
    print(employee.report())    
# endregion
