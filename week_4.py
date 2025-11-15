# region Functions ------------------------
'''Ejercicio 1
Crea una función bienvenida() que imprima “¡Hola, estudiante!”.'''
def welcome():
    print("¡Hi, student!")
welcome()

'''Ejercicio 2
Crea una función presentacion(nombre) que reciba un nombre y muestre un saludo personalizado.'''
def presentation(name):
    print(f"¡Hi, {name}!")
presentation("Ana")

'''Ejercicio 3
Crea una función multiplicar(a, b) que devuelva la multiplicación de dos números (usa return).'''
def multiply(a, b):
    return a * b
print("result multiply:", multiply(4, 5))

'''Ejercicio 4
Explica con código la diferencia entre return y print en una función.'''
def return_vs_print(a, b):
    print("This will print the sum:", a + b)  # This prints the sum but does not return it
    return a * b  # This returns the sum to the caller
print("The returned is a multiplication:", return_vs_print(3, 4))

'''Ejercicio 5
Crea una variable global curso = "Python" y una función que defina otra variable local curso = "Java" y muestre ambas en consola.'''
course = "Python"
def mostrar_cursos():
    course = "Java"
    print("var local:", course)
mostrar_cursos()

print("var global:", course)
# endregion

# region Advance parameters ------------------------
'''Ejercicio 1
Escribe una función listar_personas que reciba cualquier número de nombres (*args) y los imprima en una lista.'''
def list_people(*names):
    for name in names:
        print(name)
list_people("Ana", "Luis", "Carlos")


'''Ejercicio 2
Crea una función promedio que use *args para calcular el promedio de los números que reciba.'''
def average(*numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count if count > 0 else 0
print("Promedio:", average(4, 5, 6))

'''Ejercicio 3
Crea una función registrar_producto que reciba un id obligatorio y cualquier cantidad de datos extra con **kwargs.'''
def register_product(id, **extra_data):
    print("Product ID:", id)
    for key, value in extra_data.items():
        print(f"{key}: {value}")
register_product(101, name="Laptop", price=1200, stock=30)

'''Ejercicio 4
Escribe una función crear_reporte que reciba dos parámetros fijos, una lista de notas (*args) y datos extra (**kwargs).'''
def create_report(name, subject, *grades, **extra_info):
    print(f"Report for {name} in {subject}")
    print("Grades mean:", sum(grades) / len(grades) if grades else 0)
    for key, value in extra_info.items():
        print(f"{key}: {value}")
create_report("Ana", "Math", 85, 90, 78, age=20, city="Madrid")

'''Ejercicio 5
Define una función llamada presentar(nombre, edad, ciudad) que imprima un mensaje con esos datos.
Después:
Llama a la función pasando una lista con los valores y usa * para desempaquetarla.
Llama a la función pasando un diccionario con los valores y usa ** para desempaquetarlo.'''

def introduce(name, age, city):
    print(f"My name is {name}, I'm {age} years old and I live in {city}.")

introduce(*["Ana", 25, "Madrid"])
introduce(**{"name": "Luis", "age": 30, "city": "Barcelona"})
# endregion

# region Lambda functions ------------------------
'''Ejercicio 1
Crea una lambda que reciba dos números y devuelva su suma.'''
sum_lambda = lambda x, y: x + y
print("Sum:", sum_lambda(9, 4))

'''Ejercicio 2
Crea una lambda que reciba un número y devuelva "Par" si lo es, o "Impar" en caso contrario.'''
parity_lambda = lambda x: "Even" if x % 2 == 0 else "Odd"
print("Parity:", parity_lambda(9))

'''Ejercicio 3
Crea una lambda que reciba un número y devuelva su cuadrado.'''
square_lambda = lambda x: x ** 2
print("Square:", square_lambda(6))

'''Ejercicio 4
Crea una lambda que reciba un string y lo devuelva al revés.'''
reverse_lambda = lambda s: s[::-1]
print("Reverse:", reverse_lambda("hello"))

'''Ejercicio 5
Crea una lambda que reciba dos números y devuelva el mayor de ellos.'''
max_lambda = lambda x, y: x if x > y else y
print("Max:", max_lambda(7, 10))

'''Ejercicio 6
Crea una lambda que reciba un string y devuelva su longitud.'''
length_lambda = lambda s: len(s)
print("Length:", length_lambda("hello"))

'''Ejercicio 7
Crea una lambda que no reciba argumentos y devuelva siempre "Hola desde lambda".'''
hello_lambda = lambda: "Hi from lambda"
print(hello_lambda())

'''Ejercicio 8
Crea una lambda que reciba un precio y devuelva el precio con IVA del 16%.'''
iva_lambda = lambda price: price * 1.16
print("Price with IVA:", round(iva_lambda(100), 2))

'''Ejercicio 9
Crea una lambda que reciba un texto y devuelva su último carácter.'''
last_char_lambda = lambda text: text[-1] if text else ''
print("Last character:", last_char_lambda("hello"))

'''Ejercicio 10
Crea un diccionario donde cada clave sea una operación ("suma", "resta", "doble") y los valores sean lambdas que la realicen.'''
operations = {
    "sum": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "double": lambda x: x * 2
}
print("Operations:")
print("Sum:", operations["sum"](5, 3))
print("Subtract:", operations["subtract"](5, 3))
print("Double:", operations["double"](5))
# endregion

# region Functional programming ------------------------
'''Ejercicio 1
Tienes una lista de temperaturas en grados Celsius. Convierte todas a Fahrenheit.
(Fórmula: F = C * 9/5 + 32).'''
celsius_temps = [0, 20, 37, 100]
fahrenheit_temps = list(map(lambda c: c * 9/5 + 32, celsius_temps))
print("Fahrenheit temperatures:", fahrenheit_temps)

'''Ejercicio 2
Dada una lista de nombres, agrega la frase "Hola, " al inicio de cada uno.'''
names = ["Alice", "Bob", "Charlie"]
greetings = list(map(lambda name: f"Hi, {name}!", names))
print(greetings)

'''Ejercicio 3
De una lista de edades, quédate solo con las que representan adultos (18 años o más).'''
ages = [12, 17, 18, 24, 30, 15]
adults = list(filter(lambda age: age >= 18, ages))
print("Adults:", adults)

'''Ejercicio 4
De una lista de frases, quédate solo con las que tengan más de 10 caracteres.'''
phrases = ["short", "this is a long phrase", "medium length", "tiny"]
long_phrases = list(filter(lambda phrase: len(phrase) > 10, phrases))
print("Long phrases:", long_phrases)

'''Ejercicio 5
Calcula el total de una lista de precios usando reduce.'''
from functools import reduce
prices = [19.99, 5.49, 3.50, 12.00]
total_price = reduce(lambda acc, y: acc + y, prices)
print("Total price:", round(total_price, 2))

'''Ejercicio 6
Encuentra el número más grande en una lista usando reduce.'''
numbers = [3, 56, 23, 89, 12, 45]
max_number = reduce(lambda a, b: a if a > b else b, numbers)
print("Max number:", max_number)

#HERE ANOTHER USE CASE FOR REDUCE
# Caso 3: Encontrar el producto más caro en la lista
products = [
    {"nombre": "laptop", "precio": 1200},
    {"nombre": "mouse", "precio": 25},
    {"nombre": "monitor", "precio": 300}
]
most_expensive = reduce(lambda acc, p: p if p["precio"] > acc["precio"] else acc, products)
print(most_expensive)

'''Ejercicio 7
Dada una lista de palabras, quédate solo con las que empiezan con "P", y pásalas a minúsculas.'''
words = ["Python", "java", "Perl", "C++", "PHP", "Ruby"]
p_words_lower = list(map(lambda w: w.lower(), filter(lambda w: w.startswith("P"), words)))
print("Words starting with P in lowercase:", p_words_lower)

"""
IN JAVASCRIPT
const words = ["Python", "java", "Perl", "C++", "PHP", "Ruby"];
const p_words_lower = words
    .filter(w => w.startsWith("P"))
    .map(w => w.toLowerCase());
console.log("Words starting with P in lowercase:", p_words_lower);
"""

'''Ejercicio 8
De una lista de productos con precios en USD, convierte los precios a MXN (17.5) y suma el total.'''
products_usd = [
    {"name": "laptop", "price": 1200},
    {"name": "mouse", "price": 25},
    {"name": "monitor", "price": 300}
]
products_mxn = list(map(lambda p: {"name": p["name"], "price": p["price"] * 17.5}, products_usd))
total_mxn = reduce(lambda acc, p: acc + p["price"], products_mxn, 0)
print("Total price in MXN:", round(total_mxn, 2))

'''Ejercicio 9
De una lista de edades, quédate solo con las de mayores de 18 y calcula el promedio.'''
ages = [12, 17, 18, 24, 30, 15]
adult_ages = list(filter(lambda age: age > 18, ages))
average_age = reduce(lambda acc, age: acc + age, adult_ages, 0) / len(adult_ages) if adult_ages else 0
print("Average age of adults:", round(average_age, 2))

'''Ejercicio 10
De una lista de números, quédate con los pares, multiplícalos por 2 y suma el total.'''
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
doubled_evens = list(map(lambda x: x * 2, even_numbers))
total = reduce(lambda acc, x: acc + x, doubled_evens, 0)
print("Total of doubled even numbers:", total)
# endregion