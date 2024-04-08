#EJERCICIO DE CLASE 
def sum(num_1: float,num_2: float) -> float:
    """_summary_

    Args:
        num_1 (float): _description_
        num_2 (float): _description_

    Returns:
        float: _description_
    """
    valor_suma: float = num_1 + num_2
    return valor_suma

#EJERCICIO APRENDE CON alf
#Ejercicio 5 : Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
import math
def area_circulo(radio:float):
    """area_circulo: esta funcíon solicita el radio de una circunferencia y retorna el área de la circunferencia.

    Args:
        radio (float): radio de la circunferencia.

    Returns:
        area(float): área de la circunferencia  
    """
    area:float = radio * 3.14
    return area

def volumen_cilindro(radio:float,altura:float):
    """volumen_cilindro: esta función solicita el radio y la altura de un cilindro y retorna el volumen de este

    Args:
        radio (float): radio de la circunferencia.
        altura (float): altura de la circunferencia.

    Returns:
        volumen(float): volumen del cilindro
    """
    volumen:float = area_circulo(radio) * altura
    return volumen 


