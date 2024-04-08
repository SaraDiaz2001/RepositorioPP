#Nota: Self mas adelante hara referencia a lo que es el objeto
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