def calculadora(num1, num2, selecao):
	if selecao == 1:
		resultado = num1 + num2
		return resultado
	elif selecao == 2:
		resultado = num1 - num2
		return resultado
	elif selecao == 3:
		resultado = num1 * num2
		return resultado
	elif selecao == 4:
		if num2 == 0:
			return "Operação Inválida"
		else:
			resultado = num1 / num2
			return resultado
	else:
		return 0

num1 = 20; num2 = 100; selecao = 4

calculadora(num1, num2, selecao)