#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo...

nombre = input("Por favor, ingresa tu nombre: ")
print(f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados
nombre = input ("Ingresa tu nombre: ")
apellido = input ("Ingresa tu apellido: ")
edad = input ("Ingresa tu edad: ")
resindencia = input ("Ingres tu residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {resindencia}.")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro con comando math
import math
radio = float (input("Ingresa el radio del circulo: "))
area = math.pi * radio
perimetro = 2 * math.pi * radio
print(f"El area del circulo es: {area:.2f}")
print(f"El perimetro del circulo es: {perimetro: .2f}")

#4) sin comando math
radio = float(input("Ingresa el radio del circulo: "))
pi = 3.141592653589793
area = pi * radio ** 2
perimetro = 2 * pi * radio

print(f"Area: {area: .2f}")
print(f"Perimetro: {perimetro: .2f}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = float(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas.")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero = int(input("Ingrese un numero par mostrar su tabla de multiplicar: "))
print(f"\nTabla de multiplicar del {numero}: ")
for i in range(1, 11): 
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print("Ingrese dos numeros enteros distintos de cero")
num1 = int(input("Primer numero: "))
num2 = int(input("Segundo numero: "))
while num1 == 0 or num2 == 0:
    print("ERROR: Ambos numeros deben ser distintos de cero")
    num1 = int(input("Primer numero: "))
    num2 = int(input("Segundo numero: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print("\nResultados: ")
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multipliacion: {num1} x {num2} = {multiplicacion}")
print(f"Division: {num1} / {num2} = {division}")

#8) Calculo de IMC
print("Calculadora de Indice de Masa Corporal (IMC)")
peso = float(input("Ingrese su peso en Kilogramos (kg): ")) 
altura = float(input("Inghrese su altura en metros (m): "))
imc= peso / (altura ** 2) 
print(f"\nSu Indice de Masa Corporal es: {imc: .2f}")
print("\nClasificacion segun OMS: ") 
if imc < 18.5:
    print("Bajo peso") 
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")

#9) Conversion de grados celsius a farenheit
print("Conversor de Celsius a Fahrenheit")
celsius = float(input("Ingrese la temperatura en grados Celsius (ºC): "))
fahrenheit = (celsius * 9/5) + 32
print(f"\n{celsius} ºC equivalen a {fahrenheit: .1f}ºF")

#10) Promedio de 3 numeros
print("Calculadora de promedio de tres números")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"\nEl promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")

#Usando lista
numeros = [float (input(f"Ingrese el numero {i+1}: ")) for i in range(3)]
promedio = sum(numeros)/len(numeros)
print(f"\nEl promedio es: {promedio: .2f}")
