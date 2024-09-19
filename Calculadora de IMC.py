#ATVDD de Calcular o valor de imc
def cal_imc(massa, altura):
    """Calcular IMC."""
    imc = massa / (altura**2)
    return imc
# Exemplo de Uso
massa = float(input("Digite sua Massa em KG:"))
altura = float(input("Digite sua Altura em Metros: "))
resultado = calcular_imc(massa, altura)
print("seu imc é:", resultado)