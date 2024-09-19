# aQUI E A ATVDD DE PYTHON COM O OBJETIVO DE FAZER UMA CALCULADORA DE Z
def calcular_z(x, y):
    """Calcula o valor de Z."""
    z = ((x**2 + y**2) / (x - y))
    return round(z, 3) #Arredonda para 3 casas decimais

#Exemplo de uso:
x = int(input("Digite o Valor de x: "))
y = int(input("Digite o Valor de y: "))
resultado = calcular_z(x, y)
print("O valor de z e:", resultado)