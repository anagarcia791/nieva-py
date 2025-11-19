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

    def agregar(self, miembro):
        self.miembros.append(miembro)

spanish_group = Group("Spanish Speakers")
spanish_group.agregar("Carlos")
spanish_group.agregar("María")
print("Spanish Members:", spanish_group.miembros)

portuguese_group = Group("Portuguese Speakers", ["Ana", "João"])
print("Portuguese Members:", portuguese_group.miembros)

# endregion