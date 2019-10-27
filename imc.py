def calculaIMC(altura, peso):
    """Função responsável por calcular o IMC"""
    dobro_altura = altura * altura
    total_imc = peso/dobro_altura

    if total_imc < 18.5:
        resultado = "Você está abaixo do peso!"
    elif total_imc >= 18.5 and total_imc <= 24.9:
        resultado = "Você está com o peso ideal!"
    elif total_imc > 25 and total_imc <= 29.9:
        resultado = "Você está acima do peso!"
    else:
        resultado = "Você está obeso!"

    return resultado


try:
    peso_em_kg = int(input("Insira seu peso: "))
    altura_em_metros = float(input("Insira sua altura em metros: "))
except:
    print("Por favor insira seus dados corretamente!")

imc = calculaIMC(altura_em_metros, peso_em_kg)
print(imc)