# region Collections ------------------------
'''Ejercicio 1
Únicamente lee y copia directamente las diferentes colecciones en tu nuevo cuaderno de Semana 3.
No hay nada más. Observa las diferencias. Prepárate para el siguiente contenido donde abordaremos en profundidad cada una.'''

# Listas
fruits = ["manzana", "pera", "plátano"]
numbers = [10, 20, 30, 40, 50]
mixed = ["hola", 123, 4.5, True]

# Dicts
person = {"name": "Ana", "age": 25, "city": "Madrid"}
product = {"id": 101, "name": "Laptop", "price": 899.99}
empty = {}  # empty dict

# Sets
colors = {"rojo", "verde", "azul"}
unique_numbers = {1, 2, 3, 3, 2, 1}  # duplicates will be removed
languages = {"Python", "Java", "C++"}

# Tuples
coordinates = (10, 20)
point3D = (5, -3, 7)
data = ("Mike", 30, "México")
# endregion

# region Lists ------------------------
'''Ejercicio 1
Crear una lista llamada países con 4 países. Muestra el primero y el último elemento usando índices.'''

countries = ["España", "Francia", "Alemania", "Italia"]
print(countries[0], countries[-1])  # First and last country

'''Ejercicio 2
Crea una lista de 5 números. Muestra el último y el penúltimo usando índices negativos.'''

numbers = [10, 20, 30, 40, 50]
print(numbers[-2:])  # Last two numbers

'''Ejercicio 3
Crea una lista colores = ["rojo", "verde", "azul"] y cambia el valor "verde" por "amarillo".'''

colors_2 = ["rojo", "verde", "azul"]
colors_2[1] = "amarillo"
print(colors_2)

'''Ejercicio 4
Dada la lista letras = ["a","b","c","d","e","f"], imprime:
Los tres primeros elementos.
Los tres últimos.
Desde la posición 2 hasta la 4 (sin incluir la 4).'''

letters = ["a", "b", "c", "d", "e", "f"]
print(letters[:3])  # First three elements
print(letters[-3:])  # Last three elements
print(letters[2:4])  # From position 2 to 4 (excluding 4)

'''Ejercicio 5
Usa nums = [0,1,2,3,4,5,6,7,8,9] para:
Obtener todos los números pares.
Obtener todos los números impares.
Mostrar la lista en orden inverso.'''

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[::2])  # Even numbers
print(nums[1::2])  # Odd numbers
print(nums[::-1])  # Reverse order

'''Ejercicio 6
Con la lista animales = ["perro","gato","pez","gato"], verifica si "gato" está en la lista, cuántos elementos tiene en total, y si "loro" no está en la lista.'''

animals = ["perro", "gato", "pez", "gato"]
print("gato" in animals)  # Check if "gato" is in the list
print(len(animals))  # Total number of elements
print("loro" not in animals)  # Check if "loro" is not in the list

'''Ejercicio 7
Crea una lista nombres = ["Ana","Luis","Marta"] y recórrela con un for para imprimir cada nombre en una línea.'''
names_2 = []
names = ["Ana", "Luis", "Marta"]
for name in names:
    names_2.append(name)
print(names_2)

'''Ejercicio 8
Crea a = [1,2,3]. Luego haz b = a. Cambia b[0] = 100. Muestra a y b.'''
a = [1, 2, 3]
b = a
b[0] = 100
print(a, b, "The lists a and b are the same because b is a reference to a.")

'''Ejercicio 9
Dada lista = [1,2,2,3,2,4]:
Verifica si el número 2 está en la lista.
Cuenta cuántas veces aparece el número 2 usando un for.
Crea otra lista [2,1,2,3,2,4] y compárala con lista usando ==.'''
lista = [1, 2, 2, 3, 2, 4]
print(2 in lista)  # Check if 2 is in the list
print("2 appears", lista.count(2))  # Print how many times 2 appears
another_list = [2, 1, 2, 3, 2, 4]
print(lista == another_list)  # Compare the two lists
# endregion

# region Lists Methods ------------------------
'''Ejercicio 1
Crea una lista vacía nombres, agrega dos nombres con append, y luego inserta uno en la primera posición con insert.'''
names = []
names.append("Carlos")
names.append("Lucía")
names.insert(0, "Ana")
print(names)

'''Ejercicio 2
Crea una lista con [1,2], y extiéndela con [3,4,5].'''
numbers = [1, 2]
numbers.extend([3, 4, 5])
print(numbers)

'''Ejercicio 3
Dada colores = ["rojo","verde","azul","verde"], elimina un "verde" con remove.
Luego usa pop() para eliminar y guardar el último color.'''
colors_3 = ["rojo", "verde", "azul", "verde"]
colors_3.remove("verde")
last_color = colors_3.pop()
print(colors_3)
print("Last color removed:", last_color)

'''Ejercicio 4
Con letras = ["a","b","c","b","a","b"], muestra el índice de la primera "b".
Luego muestra cuántas veces aparece "b".'''
letters_2 = ["a", "b", "c", "b", "a", "b"]
print("First index of 'b':", letters_2.index("b"))
print("Count of 'b':", letters_2.count("b"))

'''Ejercicio 5
Con nums = [5,1,4,2,3]:
Ordena en forma ascendente.
Ordena en forma descendente.
Invierte el orden actual.'''
nums_2 = [5, 1, 4, 2, 3]
nums_2.sort()
print("Ascending:", nums_2)
nums_2.sort(reverse=True)
print("Descending:", nums_2)
nums_2.reverse()
print("Reversed:", nums_2)

'''Ejercicio 6
Crea una lista con [10,20,30], luego vacíala y muéstrala.'''
nums_3 = [10, 20, 30]
nums_3.clear()
print("List after clearing:", nums_3)
# endregion

# region Dicts ------------------------
'''Ejercicio 1
Crea un diccionario alumno con un nombre, edad y carrera. Imprime solo la carrera.'''
student = {
    "name": "Juan", "age": 21, "major": "Computer Science"
}
print("Major:", student["major"])

'''Crea un diccionario producto con "nombre":"Laptop", "precio":15000.
Cambia el precio a 14000
Agrega la clave "stock": 20'''
product = { "name": "Laptop", "price": 15000 }
product["price"] = 14000
product["stock"] = 20

print("Product:", product)

'''Ejercicio 3
De ciudad = {"nombre":"Veracruz","poblacion":600000,"pais":"México"} elimina la clave "pais".'''
city = { "name": "Veracruz", "population": 600000, "country": "México" }
del city["country"]
print("City after removing 'country':", city)

'''Ejercicio 4
Con persona = {"nombre":"Luis","edad":30}, verifica si la clave "edad" existe.
Imprime "Edad encontrada" si está, o "No existe" si no.'''
person = { "name": "Luis", "age": 30 }
if "age" in person:
    print("Edad encontrada")
else:
    print("No existe")

'''Con contacto = {"nombre":"Ana","telefono":"1234","email":"ana@mail.com"} recorre e imprime cada par en formato:
nombre → Ana'''
contact = {
    "name": "Ana", "phone": "1234", "email": "ana@mail.com"
}

for key, value in contact.items():
    print(f"{key} → {value}")

'''Ejercicio 6
Crea a = {"x":1} y luego b = a. Cambia el valor de "x" desde b y muestra ambos.
Explica qué sucedió.'''  
a = {"x": 1}
b = a
b["x"] = 100
print(a, b, "Both dictionaries are the same because b is a reference to a.")

'''Ejercicio 7
Repite el ejercicio anterior pero usando c = a.copy(). Cambia el valor de "x" en c y muestra ambos.
Explica qué sucedió.'''
a = {"x": 1}
c = a.copy()
c["x"] = 100
print(a, c, "Both dictionaries are different because c is a copy of a.")

'''Ejercicio 8
Crea datos = {"nums":[1,2,3]}. Haz copia = datos.copy().
Agrega un número a la lista desde copia.
Muestra ambos y explica por qué cambiaron.'''
data = {"nums": [1, 2, 3]}
copy = data.copy()
copy["nums"].append(4)
print(data, copy, "We are doing a copy of data but the list inside is still a reference, so both reflect the change.")

'''
Ejercicio 9
Crea un diccionario usuario con:
"nombre"
"edad"
"contacto" (otro dict con "email" y "telefono")
Accede al email dentro de contacto y muéstralo.'''
user = {
    "name": "Carlos",
    "age": 28,
    "contact": {
        "email": "carlos@mail.com",
        "phone": "1234-5678"
    }
}
print("User email:", user["contact"]["email"])

'''Ejercicio 10
Crea un diccionario agenda con 3 contactos. Cada contacto debe tener como clave su nombre, y como valor un diccionario con "telefono" y "email".
Muestra todos los contactos recorriendo el diccionario.'''
agenda = {
    "Ana": {"phone": "1111", "email": "ana@mail.com"},
    "Luis": {"phone": "2222", "email": "luis@mail.com"},
    "Marta": {"phone": "3333", "email": "marta@mail.com"}
}

for name, info in agenda.items():
    print(f"Contacto: {name}, Teléfono: {info['phone']}, Email: {info['email']}")
# endregion

# region Dict Methods ------------------------
'''Ejercicio 1
Dado usuario = {"nombre": "Luis", "pais": "MX"}, muestra el valor de "edad" usando .get() con valor por defecto 0.'''
user = {"name": "Luis", "country": "MX"}
print("Edad:", user.get("age", 0))

'''Con producto = {"nombre":"Laptop","precio":15000,"stock":10}:
a) Muestra la lista de claves.
b) Muestra la lista de valores.
c) Recorre items() e imprime clave → valor.'''
product = {"name": "Laptop", "price": 15000, "stock": 10}
print("Claves:", product.keys())
print("Valores:", product.values())
for key, value in product.items():
    print(f"{key} → {value}")

'''Ejercicio 3
Parte de perfil = {"usuario":"mike","rol":"viewer"} y actualiza con {"rol":"admin","activo":True}.'''
profile = {"user": "mike", "role": "viewer"}
profile.update({"role": "admin", "active": True})
print("Updated profile:", profile)

'''Ejercicio 4
Con cfg = {"tema":"oscuro","notificaciones":True}, elimina "tema" devolviendo su valor, y luego intenta eliminar "idioma" devolviendo "es" como valor por defecto.'''
cfg = {"theme": "dark", "notifications": True}
removed_theme = cfg.pop("theme", None)
print("Removed theme:", removed_theme)
print("Language:", cfg.pop("language", "es"))

'''Ejercicio 5
Con d = {"a":1,"b":2,"c":3}, usa popitem() dos veces e imprime lo que devuelve cada llamada y el dict restante.'''
d = {"a": 1, "b": 2, "c": 3}
item1 = d.popitem()
print("Popped item 1:", item1)
item2 = d.popitem()
print("Popped item 2:", item2)
print("Remaining dict:", d)

'''Ejercicio 6
Crea a = {"x":[1,2]}. Luego:
b = a y agrega 3 a la lista en b["x"].
c = a.copy() y agrega 4 a la lista en c["x"]. Muestra a, b, c y comenta qué pasó.'''
a = {"x": [1, 2]}
b = a
b["x"].append(3)
c = a.copy()
c["x"].append(4)
print(a, b, c, "Both a and b reflect the changes because b is a reference to a. c is also affected because the list inside is still a reference.")

'''Ejercicio 7
Con temp = {"k1":1,"k2":2}, vacía el diccionario y muéstralo.'''
temp = {"k1": 1, "k2": 2}
temp.clear()
print("Temp after clear:", temp)

'''Ejercicio 8
Crea campos = ["nombre","email","telefono"] y genera un diccionario con None en cada clave usando dict.fromkeys. Luego asigna "Ana", "ana@mail.com", "1234".'''
campos = ["nombre", "email", "telefono"]
datos = dict.fromkeys(campos, None)
datos["nombre"] = "Ana"
datos["email"] = "ana@mail.com"
datos["telefono"] = "1234"
print("Datos:", datos)

'''Ejercicio 9
Con config = {"modo":"auto"}, realiza:
update con {"modo":"manual","reintentos":3}
Usa get para leer "timeout" con defecto 30.
Elimina "reintentos" con pop devolviendo su valor.
Muestra claves y valores finales.'''
config = {"mode": "auto"}
config.update({"mode": "manual", "retries": 3})
print("Timeout:", config.get("timeout", 30))
removed_retries = config.pop("retries")
print("Removed retries:", removed_retries)
print("Final config:", config)

'''Ejercicio 10
Con persona = {"nombre":"Ana","edad":25}, imprime "Altura:" seguido del valor de "altura" usando get con defecto "No registrada". Recorre items() y muestra cada par.'''
persona = {"nombre": "Ana", "edad": 25}
print("Altura:", persona.get("altura", "No registrada"))
for clave, valor in persona.items():
    print(f"{clave} → {valor}")
# endregion

# region Sets ------------------------
'''Ejercicio 1
Crea un set vacío llamado my_data y muestra su tipo.'''
my_data = set()
print("my_data type:", type(my_data))

'''Ejercicio 2
Crea un set con los valores {1,1,2,3,3,4} y muestra el resultado.'''
my_set = {1, 1, 2, 3, 3, 4}
print("my_set:", my_set)

'''Ejercicio 3
Crea un set que contenga tu nombre, tu edad y el valor True.'''
my_info = {"Margarita", 30, True}
print("my_info:", my_info)

'''Ejercicio 4
Dado frutas = {"manzana", "pera", "uva"}, verifica si "pera" está en el set y si "naranja" no está en el set.'''
frutas = {"manzana", "pera", "uva"}
print("¿ is 'pera' in frutas?", "pera" in frutas)
print("¿'naranja' is not in frutas?", "naranja" not in frutas)

'''Ejercicio 5
Crea un set con los valores "a", "b", "c", "d". Imprímelo tres veces seguidas y observa el orden.'''
my_set = {"a", "b", "c", "d"}
print("my_set:", my_set)
print("my_set:", my_set)

'''Ejercicio 6
Dada la lista [1,1,2,3,3,4,5,5], conviértela en un set y muestra el resultado.'''
lista = [1, 1, 2, 3, 3, 4, 5, 5]
mi_set = set(lista)
print("mi_set:", mi_set)

'''Ejercicio 7
Intenta crear un set con una lista dentro: {[1,2,3], 4, 5} y observa el error que ocurre.'''
try:
    invalid_set = {[1, 2, 3], 4, 5}
except TypeError as e:
    print("set creation error:", e)
# endregion

# region Set Methods ------------------------
'''Ejercicio 1 - add
Tienes un set llamado frutas = {"manzana", "pera"}.
Agrega un nuevo elemento "uva" usando el método .add().
Al final, imprime el set para confirmar que ahora contiene tres frutas.'''
frutas = {"manzana", "pera"}
frutas.add("uva")
print("frutas:", frutas)

'''Ejercicio 2 - remove vs discard
Crea un set colores = {"rojo", "verde", "azul"}.
Primero elimina "verde" usando .remove().
Después intenta eliminar "negro" usando .discard().
Imprime el set final y observa la diferencia entre ambos métodos (uno da error si no existe, el otro no).'''
colores = {"rojo", "verde", "azul"}
colores.remove("verde")
print("Colores after remove:", colores)
colores.discard("negro")
print("Colores after discard:", colores)

'''Ejercicio 3 - pop
Crea un set letras = {"a","b","c","d"}.
Usa .pop() para quitar un elemento.
Muestra qué valor devolvió .pop() y luego imprime cómo quedó el set después de la operación.'''
letras = {"a", "b", "c", "d"}
letra_removida = letras.pop()
print("removed value:", letra_removida)
print("letras after pop:", letras)

'''Ejercicio 4 - clear
Crea un set nums = {1,2,3}.
Vacía completamente el set usando .clear().
Imprime el resultado y verifica que quedó como set() (un set vacío).'''
nums = {1, 2, 3}
nums.clear()
print("nums after clear:", nums)

'''Ejercicio 5 - update
Crea a = {1,2,3} y b = {3,4,5}.
Usa .update() para agregar los elementos de b dentro de a.
Imprime a y confirma que ahora tiene los números {1,2,3,4,5}.'''
a = {1, 2, 3}
b = {3, 4, 5}
a.update(b)
print("update a:", a)

'''Ejercicio 6 - intersection_update
Crea a = {1,2,3,4} y b = {3,4,5}.
Usa .intersection_update() para que en a solo se mantengan los elementos que están en ambos sets.'''
a = {1, 2, 3, 4}
b = {3, 4, 5}
a.intersection_update(b)
print("intersection update a:", a)

'''Ejercicio 7 - difference_update
Crea a = {1,2,3,4}.
Usa .difference_update({2,5}) para eliminar de a todos los elementos que estén en el set {2,5}.'''
a = {1, 2, 3, 4}
a.difference_update({2, 5})
print("difference update a:", a)

'''Ejercicio 8 - symmetric_difference_update
Crea a = {1,2,3} y b = {3,4}.
Usa .symmetric_difference_update(b) para que a se transforme en los elementos que están en uno u otro set, pero no en ambos al mismo tiempo.'''
a = {1, 2, 3}
b = {3, 4}
a.symmetric_difference_update(b)
print("symmetric difference update a:", a)

'''Ejercicio 9 - union
Crea x = {1,2} y y = {2,3,4}.
Genera un nuevo set u con la unión de x e y usando .union().
Luego prueba el operador | para obtener lo mismo.
Imprime el resultado en ambos casos.'''
x = {1, 2}
y = {2, 3, 4}
u = x.union(y)
print("union:", u)
print("union usando |:", x | y)

'''Ejercicio 10 - intersection
Usa los mismos sets x e y.
Crea un nuevo set i con los elementos que están en ambos usando .intersection().
Luego prueba el operador &.'''
x = {1, 2}
y = {2, 3, 4}
i = x.intersection(y)
print("intersection:", i)
print("intersection usando &:", x & y)

'''Ejercicio 11 - difference
Con los sets x e y, crea dos nuevos sets:
d1 = x - y (lo que está en x pero no en y).
d2 = y - x (lo que está en y pero no en x). Imprime ambos y observa la diferencia.'''
d1 = x - y
d2 = y - x
print("d1:", d1)
print("d2:", d2)

'''Ejercicio 12 - symmetric_difference
Con los sets x e y, crea un nuevo set sd con la diferencia simétrica, es decir, los elementos que están en uno u otro, pero no en ambos.
Prueba también con el operador ^.'''
sd = x.symmetric_difference(y)
print("symmetric difference:", sd)
print("symmetric difference usando ^:", x ^ y)

'''Ejercicio 13 - issubset y issuperset
Crea a = {1,2} y b = {1,2,3,4}.
Verifica si a es subconjunto de b usando .issubset().
Luego verifica si b es superconjunto de a usando .issuperset().'''
a = {1, 2}
b = {1, 2, 3, 4}
print("a es subconjunto de b:", a.issubset(b), "should be True, due a is contained in b")
print("b es superconjunto de a:", b.issuperset(a), "should be True, due b contains all elements of a")

'''Ejercicio 14 - isdisjoint
Crea m = {"py","js"} y n = {"html","css"}.
Verifica si son disjuntos (es decir, si no comparten nada).
Después crea p = {"js","go"} y compara m.isdisjoint(p).
Imprime los resultados y reflexiona cuándo sería útil este método.'''
m = {"py", "js"}
n = {"html", "css"}
print("m y n son disjuntos:", m.isdisjoint(n), "should be True, due m and n have no elements in common")
p = {"js", "go"}
print("m y p son disjuntos:", m.isdisjoint(p), "should be False, due m and p share 'js'")
# endregion


# region Tuples ------------------------
'''Ejercicio 1
Crea una tupla con tres colores y muestra el primer y último elemento.'''
colores = ("rojo", "verde", "azul")
print("first color:", colores[0])
print("last color:", colores[-1])

'''Ejercicio 2
Crea una tupla con los números del 1 al 5. Usa slicing para mostrar del 2 al 4.'''
numeros = (1, 2, 3, 4, 5)
print("from 2 to 4:", numeros[1:4])

'''Ejercicio 3
Crea una tupla con un solo número (ejemplo: 7).
Imprime el tipo de dato y verifica que sea tuple.'''
numero_unico = (7,)
print("data type:", type(numero_unico))
print("¿is a tuple?", isinstance(numero_unico, tuple))

'''Ejercicio 4
Concatena dos tuplas: (10, 20) y (30, 40) en una nueva tupla.
Repite la tupla resultante 2 veces.'''
tupla1 = (10, 20)
tupla2 = (30, 40)
tupla_concatenada = tupla1 + tupla2
tupla_repetida = tupla_concatenada * 2
print("Concatenated tuple:", tupla_concatenada)
print("Repeated tuple:", tupla_repetida)

'''Ejercicio 5
Dada la tupla t = (5, 10, 15, 20, 25), usa slicing para mostrarla invertida.'''
t = (5, 10, 15, 20, 25)
print("Inverted tuple:", t[::-1])

'''Ejercicio 6
Haz unpacking de la tupla fecha = (2025, 8, 28) en variables year, month, day e imprímelas en un mensaje.'''
fecha = (2025, 8, 28)
year, month, day = fecha
print(f"date: {month}/{day}//{year}")

'''Ejercicio 7
Crea una tupla anidada t = ("Ana", (10, 20, 30), "Fin").
Muestra el número 20 accediendo correctamente a los índices.'''
t = ("Ana", (10, 20, 30), "Fin")
print("num 20:", t[1][1])

'''Ejercicio 8
Crea una tupla (1, [2,3], 4).
Agrega el número 99 a la lista interna y muestra el resultado.'''
t = (1, [2, 3], 4)
t[1].append(99)
print("result:", t)

'''Ejercicio 9
Crea una tupla con coordenadas (19.43, -99.13).
Úsala como clave en un diccionario para almacenar "CDMX".'''
coordenadas = (19.43, -99.13)
ciudades = {coordenadas: "CDMX"}
print("city:", ciudades)
# endregion

# region Functions for collections ------------------------
'''Ejercicio 1
Crea una lista con cinco nombres de animales.
Muestra cuántos elementos tiene usando len().'''
animales = ["perro", "gato", "pez", "loro", "tortuga"]
print("cuantity of animals:", len(animales))

'''Ejercicio 2
Crea una lista con los números del 1 al 10.
Usa sum() para obtener la suma total.'''
numeros = list(range(1, 11))
print("total:", sum(numeros))

'''Ejercicio 3
Dada la tupla t = (5, 17, 3, 9, 21), muestra el valor mínimo y el máximo.'''
t = (5, 17, 3, 9, 21)
print("min value:", min(t))
print("max value:", max(t))

'''Ejercicio 4
Dada la lista puntos = [40, 10, 70, 20], ordénala de menor a mayor y también de mayor a menor.'''
puntos = [40, 10, 70, 20]
print("sorted from least to greatest:", sorted(puntos))
print("sorted from greatest to least:", sorted(puntos, reverse=True))

'''Ejercicio 5
Dada la cadena texto = "python", crea una lista con sus letras en orden inverso.'''
texto = "python"
lista_letras = list(reversed(texto))
print("list reversed:", lista_letras)

'''Ejercicio 6
Dado el set valores = {0, "", None, 15}, usa any() para verificar si hay al menos un valor verdadero.'''
valores = {0, "", None, 15}
print("any true value:", any(valores))

'''Ejercicio 7
Dado el diccionario checks = {"a": 1, "b": True, "c": "ok"}, aplica all() sobre checks.values() y explica el resultado.'''
checks = {"a": 1, "b": True, "c": "ok"}
print("all true values:", all(checks.values()), "All values are truthy, so all() returns True.")
# endregion