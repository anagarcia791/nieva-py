# ------------------------ Comments ------------------------
# This is the way to do a comment in Python
"""
Multi-line comment in Python
"""

# ------------------------ Prints ------------------------
print(33)
print("i love", "python")
print("3 + 5 =", 3 + 5, "the last value should be:", 8)

# ------------------------ Inputs ------------------------
#color = input("What is your favorite color? ")
#print("Your favorite color is", color)

#age = input("How old are you? ")
#print("You are", age, "years old")

#movie, song = input("What is your favorite movie and song? ").split(", ")
#print("Your favorite movie is", movie)
#print("Your favorite song is", song)

# ------------------------ Variables ------------------------
city = "Bogota"
print("The variable city is", city)
name = "Ana"
last_name = "Garcia"
age = 28
print("mi name is", name, last_name, "i'm", age, "years old")

#2apellido = "Martínez"
apellido = "Martínez"

#nombre usuario = "Pedro"
nombre_usuario = "Pedro"

curso = "Python Básico"
Curso = "Python Avanzado"
print("curso contains:", curso, "and Curso:", Curso)

nombre_completo_usuario = nombre_usuario + " " + apellido
print("El nombre completo del usuario es:", nombre_completo_usuario)

#precio_venta = 150
precio_venta = 150

# ------------------------ Primitive Data Types ------------------------
country = "Colombia"
print("The variable country is of type:", type(country))

# ------------------------ Plain text ------------------------
name_2 = "Liz"
print("The variable name_2 is :", name_2)
last_name_2 = 'Lopez'
complete_name_2 = name_2 + " " + last_name_2
print("The complete name is:", complete_name_2)

quoted_text = 'She said: "Hello!"'
print("The variable quoted_text is:", quoted_text)

# frase = "El lenguaje Python es "genial""
frase = 'El lenguaje Python es "genial"'

# ------------------------ Int and Float ------------------------
age_2 = 30
print("The variable age_2 is an int:", age_2)
pi = 3.1416
print("The variable pi is a float:", pi)
price = 19.99
quantity = 1000
print("The price is", price, "and quantity is:", quantity)

# ------------------------ Bool ------------------------
is_student = True
print("The variable is_student is of type:", type(is_student), "and its value is:", is_student)
has_graduated = False
print("The variable has_graduated is of type:", type(has_graduated), "and its value is:", has_graduated)

# ------------------------ Basic Operations ------------------------
print("Addition: 8 + 7 =", 8 + 7)
print("Subtraction: 15 - 7 =", 15 - 7)
print("Multiplication: 6 * 8 =", 6 * 8)
print("Division: 45 / 9 =", 45 / 9)
print("Integer Division: 23 // 5 =", 23 // 5)
print("Modulus: 23 % 5 =", 23 % 5)
print("Exponentiation: 2 ** 5 =", 2 ** 5)

# ------------------------ Precedence of Operators ------------------------
# Calcula: 2 + 3 * 4
result_1 = 2 + 3 * 4
print("Result of 2 + 3 * 4 is:", result_1)
# Calcula: (2 + 3) * 4
result_2 = (2 + 3) * 4
print("Result of (2 + 3) * 4 is:", result_2)
# Calcula: 10 - 6 / 3
result_3 = 10 - 6 / 3
print("Result of 10 - 6 / 3 is:", result_3)
# Calcula: 2 + 3 * 4 ** 2
result_4 = 2 + 3 * 4 ** 2
print("Result of 2 + 3 * 4 ** 2 is:", result_4)
# Calcula: (2 + 3) * 4 ** 2
result_5 = (2 + 3) * 4 ** 2
print("Result of (2 + 3) * 4 ** 2 is:", result_5)
# Calcula: 100 / 5 * 2
result_6 = 100 / 5 * 2
print("Result of 100 / 5 * 2 is:", result_6)
# Calcula: 7 + 8 // 3
result_7 = 7 + 8 // 3
print("Result of 7 + 8 // 3 is:", result_7)
# Calcula: 7 + 8 % 3 * 2
result_8 = 7 + 8 % 3 * 2
print("Result of 7 + 8 % 3 * 2 is:", result_8)
# Calcula: (17 // 4) * 2 + (17 % 4)
result_9 = (17 // 4) * 2 + (17 % 4)
print("Result of (17 // 4) * 2 + (17 % 4) is:", result_9)

# ------------------------ Type Conversion ------------------------
int_1 = 10
print("The variable int_1 in float is:", float(int_1))
print("Convert 3.99 to int gives:", int(3.99))
text = "2025"
print("Convert text '2025' to int and add 5 gives:", (int(text)+5))
int_2 = 150
print("Convert int_2 to string gives:", str(int_2))
text_2 = "50.5"
float_1 = float(text_2)
print("Type of text_2 is: ", type(text_2), "and after conversion to float is:", type(float_1), "the value is:", float_1)

# ------------------------ String Formatting ------------------------
name_3 = "Margarita"
age_3 = 25
print(f"{name_3}. is {age_3} years old.")
print("{} has {:.2f} apples.".format("Juan", 3.1416))
print(f"El resultado es X {5*7}")
print(f"          {49.99}")
print("{pi_2:.4f} formatted.".format(pi_2=3.141592))