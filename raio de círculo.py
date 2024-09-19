#Essa é a Atvidade de Python que o objetivo e que ele peça o raio do círculo, calcule e mostre a sua área e o comprimento.#
import math 

def calcular_area_e_comprimento(raio):
     """Calcula a área e o comprimento de um círculo."""
     area = math.pi * raio**2
     comprimento = 2 * math.pi * raio
     return area, comprimento

# Exemplo de Uso:
raio = float(input("Digite o raio do cículo: "))
area, comprimento = calcular_area_e_comprimento(raio)
print("A área do comprimento é:", area)
print("O comprimento do círculo é:", comprimento)