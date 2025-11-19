## REMEMBER: This example is in Python.
class GrupoMal:
    def __init__(self, nombre, miembros=[]):  # valor por defecto mutable (PELIGRO)
        self.nombre = nombre
        self.miembros = miembros

g1 = GrupoMal("A")
g2 = GrupoMal("B")
g1.miembros.append("Ana")
print(g1.miembros)  # ['Ana']
print(g2.miembros)  # ['Ana']  <- Problema. g2 quedó contaminado.


# region Constructor __init__ ------------------------
'''Ejercicio 1
Crea una clase Usuario con los atributos username, email y activo (por defecto True).
Crea dos usuarios y muestra sus datos.'''

class User:
    def __init__(self, username, email, activo=True):
        self.username = username
        self.email = email
        self.activo = activo

lola = User("lola123", "lola@example.com")
juan = User("juan456", "juan@example.com", activo=False)
print(vars(lola))
print(vars(juan))

'''Ejercicio 2
Crea una clase Producto con nombre, precio, cantidad.
Agrega un método subtotal() que calcule precio * cantidad.'''
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def subtotal(self):
        return self.price * self.quantity
laptop = Product("Laptop", 1000, 2)
print("Total laptop P*Q:", laptop.subtotal())  # 2000

'''Ejercicio 3
Crea una clase Transaccion con monto, tipo y descripcion.
El tipo debe ser "deposito" o "retiro".
Si no es válido, lanza un ValueError.'''
class Transaction:
    def __init__(self, amount, type_, description):
        if type_ not in ["deposito", "retiro"]:
            raise ValueError("Tipo inválido. Debe ser 'deposito' o 'retiro'.")
        self.amount = amount
        self.type_ = type_
        self.description = description

salary = Transaction(3000, "deposito", "Monthly salary")
print("salary:", vars(salary))      

'''Ejercicio 4
Crea una clase Proyecto con nombre, responsable y fecha_inicio.
Si no se da fecha_inicio, usa la fecha de hoy.'''
from datetime import date
class Project:
    def __init__(self, name, responsible, start_date=None):
        self.name = name
        self.responsible = responsible
        self.start_date = start_date if start_date else date.today()
project = Project("AI Development", "Lia")
print("project:", vars(project))

'''Ejercicio 5
Crea una clase Grupo con un nombre y una lista de miembros.
Agrega un método agregar() para añadir miembros.
Evita usar listas como argumento por defecto.'''
class Group:
    def __init__(self, nombre, miembros=None):
        self.nombre = nombre
        if miembros is None:
            self.miembros = []
        else:
            self.miembros = miembros

    def add(self, miembro):
        self.miembros.append(miembro)

spanish_group = Group("Spanish Speakers")
spanish_group.add("Carlos")
spanish_group.add("María")
print("Spanish Members:", spanish_group.miembros)

portuguese_group = Group("Portuguese Speakers", ["Ana", "João"])
print("Portuguese Members:", portuguese_group.miembros)

# endregion

# region Attributes and methods ------------------------
'''Ejercicio 1
Crea una clase Persona con atributos nombre y edad.
Crea dos objetos y muestra sus valores.'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice", 30)
bob = Person("Bob", 25)
print("Alice:", vars(alice))
print("Bob:", vars(bob))

'''Ejercicio 2
Crea una clase Producto con un atributo de clase impuesto = 0.16.
Cada producto tiene nombre y precio.
Muestra el precio con impuesto de dos productos distintos.'''
class ProductWithTax:
    impuesto = 0.16

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def taxed_price(self):
        return self.price * (1 + self.impuesto)

tablet = ProductWithTax("Tablet", 1000)
print("Tablet price with tax:", tablet.taxed_price())

'''Ejercicio 3
Crea una clase Rectangulo con atributos ancho y alto.
Agrega un método area() que devuelva el área del rectángulo.
Prueba el método con distintos valores.'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect1 = Rectangle(4, 5)
print("Area rect1:", rect1.area())
rect2 = Rectangle(10, 3)
print("Area rect2:", rect2.area())


'''Ejercicio 4
Crea una clase Usuario que tenga un contador de instancias.
Cada vez que se cree un nuevo usuario, el contador debe aumentar.
Agrega un método de clase total_usuarios() que muestre cuántos usuarios hay.'''
class UserWithCounter:
    contador = 0

    def __init__(self, username):
        self.username = username
        UserWithCounter.contador += 1

    @classmethod
    def total_usuarios(cls):
        return cls.contador
    
user_1 = UserWithCounter("user1")
user_2 = UserWithCounter("user2")
print("Total users:", UserWithCounter.total_usuarios())
user_3 = UserWithCounter("user3")
print("Total users after adding user3:", UserWithCounter.total_usuarios()) 

'''Ejercicio 5
Crea una clase Matematica con un método estático es_par(n) que devuelva True si el número es par y False si es impar.
Prueba con varios números.'''
class Math:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

print("Is 4 even?", Math.is_even(4))
print("Is 7 even?", Math.is_even(7))

'''Ejercicio 6
Crea una clase Libro con atributos titulo y autor.
Agrega un método especial __str__ para que al imprimir un libro aparezca:
"Título: X | Autor: Y"'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'Título: {self.title} | Autor: {self.author}'
    
book_1 = Book("1984", "George Orwell")
print(book_1)  # Título: 1984 | Autor: George Orwell    
# endregion