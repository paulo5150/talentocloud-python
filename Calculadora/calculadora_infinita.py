#Implementação da calculadora com entrada e saída de dados para o usuário
def calculadora(num1, num2, selecao):
	if selecao == 1:
		return num1 + num2
	elif selecao == 2:
		return num1 - num2
	elif selecao == 3:
		return num1 * num2
	elif selecao == 4:
		if num2 == 0:
			return "Não existe divisão por 0"
		else: 
			return num1 / num2
print("\n==============Primeira Calculadora 'Infinita' em Python==============")
selecao = 5
while True:
    selecao = int(input("Escolha uma operação (soma: 1, subtração: 2, multiplicação: 3, divisão: 4, sair: 0): "))
    if selecao > 4 or selecao < 0:
        print("Esta opção não existe")
        continue
    elif selecao == 0:
        print("Fim")
        break
    else:
        num1 = int(input("Primeiro numero: "))
        num2 = int(input("Segundo numero : "))
        res = calculadora(num1, num2, selecao)
        print("Resultado = " + str(res))
