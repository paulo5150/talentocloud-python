def calculadora(num1, num2, selecao):
	if selecao == 1:
		return num1 + num2
	elif selecao == 2:
		return num1 - num2
	elif selecao == 3:
		return num1 * num2
	elif selecao == 4:
		if num2 == 0:
			return "Operação Inválida"
		else: 
			return num1 / num2
	else:
		return 0

num1 = int(input("Primeiro numero: "))
num2 = int(input("Segundo numero : "))
selecao = int(input("Operação (soma:1, subtração:2, multiplicação:3, divisão:4): "))

res = calculadora(num1, num2, selecao)
print("Resultado = " + str(res))