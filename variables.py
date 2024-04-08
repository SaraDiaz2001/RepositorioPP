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