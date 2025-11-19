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