def calculaIMC(altura, peso):
    dobroAltura = altura * altura
    totalIMC = peso/dobroAltura
    if totalIMC < 18.5:
        resultado = "Você está abaixo do peso!"
    elif totalIMC >= 18.5 and totalIMC <= 24.9:
        resultado = "Você está com o peso ideal!"
    elif totalIMC > 25 and totalIMC <= 29.9:
        resultado = "Você está acima do peso!"
    else: 
	    resultado = "Você está obeso!"
    return resultado