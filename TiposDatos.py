#EJERCICIOS CLASE 
#Ejercicio 1 : Dada la lista_con_dup =[1,1,2,2,3,4,5,6,6,6] contruir una lista con los mismos valoresde la lista
#pero sin valores duplicados. Sugerencia: use la funcion list y set.

lista_con_dup =[1,1,2,2,3,4,5,6,6,6]
lista = list(set(lista_con_dup))
print(lista)

#Ejercicio 2: Formas de iterar diccionarios

diccionarios = {
    'nombre' : 'Sara',
    'apellido' : 'Diaz',
    'profesion' : 'Estadistico',
    'Ocupasion' : 'Estudiante'
}

for key,value in diccionarios.items():
    print(key+' '+value)
for value in diccionarios.values():
    print(value)
for key in diccionarios.keys():
    print(key)

for i in diccionarios:
    print(i)

#EJERCICIOS APRENDE CON ALF
#Ejercicio 1 : Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print('¡Hola Mundo!')

#Ejercicio 2 :Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
m = '¡Hola Mundo!'
print(m)

#Ejercicio 3 : Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
nombre = input('Ingrese su nombre: ')
print('Hola '+nombre)

#Ejercicio 4 : Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética 
print(((3+2)/(2*5))**2)

#Ejercicio 5 : Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
horas = float(input('ingrese el número de horas trabajó: '))
costo = float(input('¿Qué valor tiene cada hora?: '))
print(f"La paga correspondiente es ${horas*costo}")

#Ejercicio 6 : Escribir un programa que lea un entero positivo, n introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 
# n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma: suma = (n(n+1))/2
n = int(input('Ingrese un número entero: '))
suma = n * (n + 1) / 2
print(f"La suma de los primeros números desde el a hasta el {n} es {suma}")

#Ejercicio 7 : Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
peso = float(input('Ingrese su peso en kilogramos: '))
altura = float(input('Ingrese su altura en metros: '))
print(f"su IMC es {peso/(altura**2)}") 

 


