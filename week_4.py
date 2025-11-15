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