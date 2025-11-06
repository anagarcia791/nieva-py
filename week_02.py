# region Comparison operators ------------------------
'''Ejercicio 1
Pide al usuario su edad y verifica si es mayor o igual a 18. Imprime el resultado con un mensaje.'''

age = 28
is_adult = age >= 18
print("Is the person an adult?", is_adult)

'''Ejercicio 2
Compara dos números y determina si son iguales o no. Imprime el resultado.'''

number_1 = 10
number_2 = 20
are_equal = number_1 == number_2
print("Are the two numbers equal?", are_equal)

'''Ejercicio 3
Verifica si la palabra "Python" es igual a "python". Imprime el resultado.'''
word_1 = "Python"
word_2 = "python"
are_words_equal = word_1 == word_2
print("Are the two words equal?", are_words_equal)

'''Ejercicio 4
Verifica si una variable nota = 85 está en el rango de 60 a 100 (usando comparación encadenada). imprime el resultado.'''
nota = 85
is_in_range = 60 <= nota <= 100
print("Is the grade in the range of 60 to 100?", is_in_range)


'''Ejercicio 5
Pregunta un número al usuario y revisa si es diferente de 0. Imprime el resultado.'''
number_3 = 5
is_different = number_3 != 0
print("Is the number different from 0?", is_different)

'''Ejercicio 6
Compara si True es mayor que False. Imprime el resultado.'''
is_true_greater = True > False
print("Is True greater than False?", is_true_greater)
# endregion

# region Logic operators ------------------------
'''Ejercicio 1
Verifica si un número está entre 10 y 20 usando and.'''
num = 15
if num >= 10 and num <= 20:
    print("The number is between 10 and 20.")
else:
    print("The number is not between 10 and 20.")

'''Ejercicio 2
Verifica si un estudiante aprueba con nota mayor o igual a 60 o si tiene un proyecto especial.'''
grade = 55
has_special_project = True
if grade >= 60 or has_special_project:
    print("The student passes.")
else:
    print("The student does not pass.")

'''Ejercicio 3
Usa not para invertir el resultado de una condición que verifica si un número es positivo.'''
number_4 = -10
is_positive = number_4 > 0
print("Is the number not positive?", not is_positive)

'''Ejercicio 4
Escribe una condición que devuelve True si un usuario tiene más de 18 años y cuenta con permiso de sus padres.'''
user_age = 20
has_parental_permission = False
if user_age > 18 and has_parental_permission:
    print("The user is allowed.")
else:
    print("The user is not allowed.")

'''Ejercicio 5
Verifica si una persona puede acceder a un concierto: Tiene boleto o está en lista VIP, Debe ser mayor de 12 años'''
has_ticket = False
is_vip = True
person_age = 15
if (has_ticket or is_vip) and person_age > 12:
    print("The person can access the concert.")
else:
    print("The person cannot access the concert.")
# endregion    

# region short-circuit evaluation ------------------------
'''Ejercicio 1
Usa and para que una variable solo muestre "Acceso permitido" si el valor de clave no está vacío.'''
key = "secret"
granted_access = key and "Access granted."
print(granted_access)

'''Ejercicio 2
Usa or para que si la variable nombre está vacía, se muestre "Invitado".'''
name = ""
guest = name or "guest"
print(guest)

'''Ejercicio 3
Crea una expresión con and que tome el valor de x y y, pero se detenga en x si es cero.'''
x = 0
y = 10
result_and = x and y
print("Result of and operation:", result_and)

'''Ejercicio 4
Usa or para que una variable resultado tome el primer valor verdadero entre 0, "", y 100.'''
result = 0 or "" or 100
print("Result of or operation:", result)

'''Ejercicio 5
Muestra "Mayor de edad" solo si la variable edad es mayor que 18, usando corto circuito.'''
new_age = 20
message = new_age > 18 and "Adult"
print(message)
# endregion

# region Chain comparisons ------------------------
'''Ejercicio 1
Con edad = 64, evalúa si está en el rango [18, 65).'''
new_age_2 = 64
is_in_range = 18 <= new_age_2 < 65
print("Is age in the range [18, 65)?", is_in_range)

'''Ejercicio 2
Convierte x > a and x < b a una cadena de comparadores.'''
x = 15
a = 10
b = 20
is_between = a < x < b
print("Is x between a and b?", is_between)

'''Ejercicio 3
¿Qué imprime print(3 < 5 < 2)? Agrega un comentario para explicar qué ocurre.'''
print("(3 < 5 < 2) is false due 5 is not less than 2", (3 < 5 < 2))

'''Ejercicio 4
Evalúa print(9 == 9 == 9) y print(9 == 10 == 9).'''
print("9 == 9 == 9 is true:", 9 == 9 == 9)
print("9 == 10 == 9 is false:", 9 == 10 == 9)

'''Ejercicio 5
Con a=2, b=4, c=4, evalúa a < b <= c.'''
a = 2
b = 4
c = 4
is_chain_true = a < b <= c
print("Is a < b <= c true?", is_chain_true)

'''Ejercicio 6
Con a=3, b=8, c=5, evalúa si b es mayor que a y c con cadena.'''
a = 3
b = 8
c = 5
is_b_greater = a < b > c
print("Is b greater than a and c?", is_b_greater)

'''Ejercicio 7
Con a=2, b=1, c=3, escribe una cadena que sea True solo si b es menor que a y c.'''
a = 2
b = 1
c = 3
is_b_smallest = b < a and b < c
print("Is b the smallest?", is_b_smallest)

'''Ejercicio 8
¿Qué imprime print("Ana" < "ana" < "casa")? Agrega un comentario para explicar qué ocurre.'''
print('"Ana" < "ana" < "casa" is ' \
'true because uppercase letters have lower ASCII values than lowercase letters:', "Ana" < "ana" < "casa")

'''Ejercicio 9
Con x=14, evalúa 2*3 < x <= 15.'''
x = 14
is_expression_true = 2 * 3 < x <= 15
print("Is 2*3 < x <= 15 true?", is_expression_true)

'''Ejercicio 10
Convierte 0 < temp < 100 en su forma con and.'''
temp = 50
is_temp_valid = 0 < temp and temp < 100
print("Is temperature between 0 and 100?", is_temp_valid)
# endregion

# region Conditionals ------------------------
'''Ejercicio 1
Pide al usuario su edad y di si es mayor de edad o no.'''
age_input = 20
if age_input >= 18:
    print("The user is an adult.")
else:
    print("The user is a minor.")

'''Ejercicio 2
Pide un número e imprime si es positivo, negativo o cero.'''
number_input = -5
if number_input > 0:
    print("The number is positive.")
elif number_input < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

'''Ejercicio 3
Dado un número del 1 al 7, imprime el día de la semana correspondiente (1 = lunes, 7 = domingo).'''
day_number = 3

if day_number == 1:    
    print("Lunes")
elif day_number == 2:
    print("Martes")
elif day_number == 3:
    print("Miércoles")
elif day_number == 4:
    print("Jueves")
elif day_number == 5:
    print("Viernes")
elif day_number == 6:
    print("Sábado")
elif day_number == 7:
    print("Domingo")
else:
    print("Número inválido.")

days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
for day in days:
    if day_number == days.index(day) + 1:
        print(day)    

'''Ejercicio 4
Pide una calificación (0 a 100) e imprime:
“Excelente” si es ≥ 90
“Aprobado” si es ≥ 60 y < 90
“Reprobado” en otro caso''' 

grade_input = 85
if grade_input >= 90:
    print("Excelente")
elif grade_input >= 60:
    print("Aprobado")
else:
    print("Reprobado")

'''Ejercicio 5
Pide un número e imprime si es par y positivo, par y negativo, impar y positivo o impar y negativo.'''
number_input_2 = -8
if number_input_2 % 2 == 0:
    if number_input_2 > 0:
        print("The number is even and positive.")
    else:
        print("The number is even and negative.")
else:
    if number_input_2 > 0:
        print("The number is odd and positive.")
    else:
        print("The number is odd and negative.")    
# endregion

# region Ternary operators ------------------------
'''Ejercicio 1
Pide un número e imprime "Positivo" si es mayor a 0, o "No positivo" en otro caso.'''
number_input_3 = -10
result = "Positive" if number_input_3 > 0 else "Not positive"
print(result)

'''Ejercicio 2
Pide la edad e imprime "Mayor de edad" si es ≥ 18, de lo contrario "Menor de edad".'''
age_input_2 = 16
status = "Adult" if age_input_2 >= 18 else "Minor"
print(status)

'''Ejercicio 3
Pide un número e imprime "Par" si lo es, de lo contrario "Impar".'''
number_input_4 = 5
paridad = "Even" if number_input_4 % 2 == 0 else "Odd"
print(paridad)

'''Ejercicio 4
Dada una variable es_admin = False, imprime "Acceso permitido" si es True, de lo contrario "Acceso denegado".'''
is_admin = False
access_message = "Access granted" if is_admin else "Access denied"
print(access_message)

'''Ejercicio 5
Pide una calificación (0–100). Imprime "Excelente" si es ≥ 90, "Aprobado" 
si es ≥ 60, y "Reprobado" en otro caso (usando un ternario anidado).'''
grade_input_5 = 85
result = "Excellent" if grade_input_5 >= 90 else "Approved" if grade_input_5 >= 60 else "Failed"
print(result)
# endregion

# region for/while ------------------------
'''Ejercicio 1
Muestra cada letra de la palabra "Python" usando un for.'''
word = ""
for letter in "Python":
    word += letter
print(word)

'''Ejercicio 2
Muestra los números del 1 al 5 usando while.'''
count = 1
count_array = []
while count <= 5:
    count_array.append(count)
    count += 1
print(count_array)

'''Ejercicio 3
Usa un for para contar cuántas vocales tiene la palabra "programa".'''
vowel_count = 0
for char in "programa":
    if char.lower() in "aeiou":
        vowel_count += 1
print("Number of vowels in 'programa':", vowel_count)     

'''Ejercicio 4
Usa while para sumar los números del 1 al 3 y mostrar el resultado.'''
total = 0
num = 1
while num <= 3:
    total += num
    num += 1
print("Total sum:", total)

'''Ejercicio 5
Crea un programa que pida una contraseña al usuario y solo termine cuando escriba "python".'''
# password = ""
# while password != "python":
#     password = input("Introduce la contraseña: ")
# print("Contraseña correcta.")
# endregion

# region range ------------------------

'''Ejercicio 1
Imprime los números del 0 al 9 con range().'''
int_array = []
for i in range(10):
    int_array.append(i)
print(int_array)

'''Ejercicio 2
Imprime los números del 3 al 7.'''    
int_array_2 = []
for i in range(3, 8):
    int_array_2.append(i)
print(int_array_2)

'''Ejercicio 3
Imprime los números pares entre 2 y 10.'''
int_array_3 = []
for i in range(2, 11, 2):
    int_array_3.append(i)
print(int_array_3)

'''Ejercicio 4
Haz un conteo regresivo del 5 al 1.'''
countdown = []
for i in range(5, 0, -1):
    countdown.append(i)
print(countdown)

'''Ejercicio 5
Muestra la palabra "Hola" 4 veces usando range().'''
greetings = []
for _ in range(4):
    greetings.append("Hola")
print(greetings)
# endregion

# region Break, continue, pass ------------------------
'''Ejercicio 1
Usa un for de 1 a 10 e imprime los números, pero detente cuando llegues al 6.'''
break_array = []
for i in range(1, 11):
    if i == 6:
        break
    break_array.append(i)
print(break_array)

'''Ejercicio 2
Usa un for de 0 a 5 e imprime todos los números excepto el 3'''
continue_array = []
for i in range(6):
    if i == 3:
        continue
    continue_array.append(i)
print(continue_array)

'''Ejercicio 3
Escribe un for de 0 a 4 donde, si el número es 2, no hagas nada (usa pass), pero imprime los demás.'''
pass_array = []
for i in range(5):
    if i == 2:
        pass
    pass_array.append(i)
print(pass_array)

'''Ejercicio 4
Usa un for de 0 a 10:

Si el número es par, sáltalo con continue.
Si el número es mayor que 7, rompe el ciclo.
Muestra solo los impares menores o iguales a 7.'''
filtered_array = []
for i in range(11):
    if i % 2 == 0:
        continue
    if i > 7:
        break
    filtered_array.append(i)
print(filtered_array)
# endregion

# region For/else ------------------------
'''Ejercicio 1
Crea un for que recorra los números del 0 al 4.

Si aparece el número 3, usa break.
Agrega un else que diga "Ciclo completado sin interrupciones".'''
for_else_array = []
for i in range(5):
    if i == 3:
        break
    for_else_array.append(i)
else:
    print("Ciclo completado sin interrupciones.")

print(for_else_array)    

'''Ejercicio 2
Busca la letra "a" en el string "python".

Si se encuentra, imprime "Encontrada".
Si no, imprime "No encontrada".'''
for char in "python":
    if char == "a":
        print("Encontrada")
        break
else:
    print("No encontrada")

'''Ejercicio 3
Recorre los números del 1 al 5.

Si aparece el 6, usa break (no debería aparecer).
Si no aparece, al final imprime "Todo se recorrió sin encontrar el 6".'''
for_range_array = []
for i in range(1, 6):
    if i == 6:
        break
    for_range_array.append(i)
else:
    print("Todo se recorrió sin encontrar el 6.")
# endregion

# region Infinity loops ------------------------
'''Ejercicios 1
Crea un ciclo while que cuente de 1 a 5 y se detenga correctamente.'''
count = 1
count_array = []
while True:
    count_array.append(count)
    if count == 5:
        break
    count += 1
print(count_array)

'''Ejercicios 2
Haz un ciclo while True que pida al usuario escribir "ok" para terminar.'''
# while True:
#     user_input = input("Escribe 'ok' para terminar: ")
#     if user_input == "ok":
#         break
# print("Programa terminado.")

'''Ejercicios 3
Corrige el siguiente código para que no sea un ciclo infinito:
x = 1
while x < 5:
    print(x)
'''
count_array_2 = []
x = 1
while x < 5:
    count_array_2.append(x)
    x += 1
print(count_array_2)    
# endregion

# region Nested loops ------------------------
'''Ejercicio 1
Crea un doble for que imprima las combinaciones de i de 0 a 2 y j de 0 a 1.'''        
for i in range(3):
    for j in range(2):
        print(i, j)

'''Ejercicio 2
Usa un ciclo anidado para dibujar un cuadrado de # de 4x4.'''        
for i in range(4):
    for j in range(4):
        print("#", end=" ")
    print()

'''Ejercicio 3
Con un for dentro de otro, imprime todas las combinaciones de letras en "ab" y números en "12".'''
for letter in "ab":
    for number in "12":
        print(letter + number)   

'''Ejercicio 4
Crea un bucle anidado que simule una tabla de multiplicar del 1 al 3.'''        
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()
# endregion