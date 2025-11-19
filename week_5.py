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

# region Encapsulation ------------------------
'''Ejercicio 1
Implementa una clase CuentaBancaria con un atributo privado __saldo. 
Debe exponer una propiedad solo lectura saldo, y métodos depositar(monto) y 
retirar(monto) con validaciones (monto > 0 y no permitir sobregiro).'''
class BankAccount:
    def __init__(self):
        self.__saldo = 0

    @property
    def saldo(self):
        return self.__saldo

    def deposit(self, amount):
        if amount > 0:
            self.__saldo += amount
        else:
            print("El monto a depositar debe ser mayor que cero.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__saldo:
                self.__saldo -= amount
            else:
                print("Fondos insuficientes para retirar.")
        else:
            print("El monto a retirar debe ser mayor que cero.")

savings = BankAccount()
savings.deposit(500)
print("amount after deposit:", savings.saldo)
savings.withdraw(200)
print("amount after withdrawal:", savings.saldo)
print("trying to withdraw 400:") # Fondos insuficientes            
savings.withdraw(400)

'''Ejercicio 2
Crea la clase Usuario con atributos públicos username y protegido _email. 
Expón email como propiedad con validación simple (debe contener “@” y un “.” después). Evita guardar un email inválido.'''
class UserWithEmail:
    def __init__(self, username, email):
        self.username = username
        self._email = None
        self.email = email  # Usar el setter para validar

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" in value and "." in value.split("@")[-1]:
            self._email = value
        else:
            print("Email inválido. No se actualizó.")

u = UserWithEmail("pao", "pao@ejemplo.com")
print("username and email:", u.username, u.email)
u.email = "malformato"  # ValueError   
print("email after invalid update attempt:", u.email)  # should still be pao@ejemplo.com

'''Ejercicio 3
Define Producto con atributo de clase IVA = 0.16, atributo privado __precio y propiedad precio con setter que no permita valores negativos.
Expón propiedad de solo lectura precio_final (precio * (1 + IVA)).'''
class ProductWithIVA:
    IVA = 0.16

    def __init__(self, name, price):
        self.__name = name
        self.__price = 0
        self.price = price  # Usar el setter para validar

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = float(value)
        else:
            print("El precio no puede ser negativo. No se actualizó.")

    @property
    def precio_final(self):
        return self.__price * (1 + ProductWithIVA.IVA)
    
apple = ProductWithIVA("Apple", 500)
print("Initial price for:", apple.name, apple.price)
print("Final price with IVA:", apple.precio_final)
apple.price = -50  # No se actualiza
print("Price after invalid update attempt:", apple.price)  # should still be 500    


'''Ejercicio 4
Crea Vehiculo con odómetro privado __odometro.
Implementa propiedad odometro con setter que no permita disminuir el valor (solo aumentar o igualar).
Agrega método recorrer(km) que incremente el odómetro validando km > 0.'''
class Vehicle:
    def __init__(self):
        self.__odometro = 0

    @property
    def odometro(self):
        return self.__odometro

    @odometro.setter
    def odometro(self, value):
        if value >= self.__odometro:
            self.__odometro = value
        else:
            print("No se puede disminuir el odómetro. No se actualizó.")

    def travel(self, km):
        if km > 0:
            self.__odometro += km
        else:
            print("Los kilómetros recorridos deben ser mayores que cero.")

tucson = Vehicle()
tucson.travel(150)
print("Odometer after traveling 150 km:", tucson.odometro)
tucson.odometro = 100  # No se actualiza
print("Odometer after invalid update attempt:", tucson.odometro)  # should still be 150
tucson.odometro = 200
print("Odometer after valid update to 200:", tucson.odometro)

'''Ejercicio 5
Implementa RegistroTemperatura con lista interna privada __mediciones. Expón:
agregar(valor) para añadir mediciones (float).
Propiedad de solo lectura promedio.
Propiedad mediciones que devuelva una tupla (copia segura) para no permitir modificaciones externas.'''
class TemperatureRecord:
    def __init__(self):
        self.__measurements = []

    def add(self, value):
        self.__measurements.append(float(value))

    @property
    def average(self):
        if self.__measurements:
            return sum(self.__measurements) / len(self.__measurements)
        return 0.0

    @property
    def measurements(self):
        return tuple(self.__measurements)
    
records = TemperatureRecord()
records.add(22.5)
records.add(24.0)
records.add(23.5)
print("Measurements:", records.measurements)
print("Average temperature:", records.average)   


'''Ejercicio 6 (opcional)
Crea Carrito con diccionario privado__items que mapea sku -> {"precio": float, "cantidad": int}.
Expón métodos:
agregar(sku, precio, cantidad=1) (validar precio > 0, cantidad > 0, acumular cantidades si ya existe).
quitar(sku, cantidad=1) (si llega a 0, eliminar el sku).
Propiedad total (suma de precio * cantidad).
Propiedad items (devuelve copia segura: dict superficial del contenido actual).
'''
class Cart:
    def __init__(self):
        self.__items = {}

    def add(self, sku, price, quantity=1):
        if price <= 0 or quantity <= 0:
            print("Precio y cantidad deben ser mayores que cero.")
            return
        if sku in self.__items:
            self.__items[sku]["cantidad"] += quantity
        else:
            self.__items[sku] = {"precio": float(price), "cantidad": int(quantity)}

    def remove(self, sku, quantity=1):
        if sku in self.__items:
            if quantity >= self.__items[sku]["cantidad"]:
                del self.__items[sku]
            else:
                self.__items[sku]["cantidad"] -= quantity
        else:
            print("El SKU no existe en el carrito.")

    @property
    def total(self):
        return sum(item["precio"] * item["cantidad"] for item in self.__items.values())

    @property
    def items(self):
        return {sku: item.copy() for sku, item in self.__items.items()}
    
chevron = Cart()
chevron.add("A001", 100, 2)
chevron.add("A002", 50)
print("Cart items:", chevron.items)
print("Cart total:", chevron.total)
chevron.remove("A001", 3)
print("Cart items after removing 3 A001:", chevron.items)
print("Cart total after removal:", chevron.total)    

# endregion