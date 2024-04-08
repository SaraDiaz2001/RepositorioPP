#Nota: Self mas adelante hara referencia a lo que es el objeto
#La programacion orientada a objetos es una abstracion de la vida real a código.

#Ejemplo 1: creacion clase persona
#La encapsulación es otro concepto de la programación orientada a objetos que consiste en ocultar los detalles internos de 
#una clase y exponer solo lo que es necesario para interactuar con ella. En tu código, los atributos nombre de los objetos 
#Gato y Perro están encapsulados dentro de la clase Animal. Estos atributos son accesibles mediante el método de 
#inicialización __init__(), pero están ocultos fuera de la clase, lo que significa que no pueden ser modificados directamente 
#desde fuera de la clase.
class Persona: 
    
    def __init__(self,nombre: str,edad: int, pelicula_favorita: str) -> None:
        #Esto se le conoce como el constructor de clase
        self.nombre = nombre
        self.edad = edad
        self.pelicula_favorita = pelicula_favorita

    def presentarse(self):
        #Un metodo es una funcion que esta dentro de una clase.
        print(f"Buenas, que bonito es saludar y ser saludado, mi nombre es {self.nombre} tengo {self.edad} y mi pelicula favorita es {self.pelicula_favorita}")

sara = Persona('Sara', edad= 22, pelicula_favorita= 'El viaje de chijiro')
santiago = Persona('Santiago', edad=20, pelicula_favorita='La La Land')

print(santiago.presentarse())

#sintaxis atributo = atributo.
#sintaxis metodo = .metodo()

#EJEMPLO 2: Creacion clase animal
#En este ejercicio poodemos ver la caracteristica de Herencia de POO. Ya que Perro y Gato son subclases de Animal.
#Por tanto va a heredar sus atributos y metodos de la clase Animal.
class Animal:

    def __init__(self,nombre) -> None:
        self.nombre = nombre
        
    def hacer_sonido(self):
        pass

class Perro(Animal):

    def hacer_sonido(self):
        return'GUAUUU'
    
class Gato(Animal):

    def hacer_sonido(self):
        return'MIAUUU'
    
gato = Gato('Doraemon')
perro = Perro('Ayudante de Santa')

print(f"mi gato se llama {gato.nombre} y hace {gato.hacer_sonido()}")
print(f"mi perro se llama {perro.nombre} y hace {perro.hacer_sonido()}")
