# Solicita dois números ao usuário e converte a entrada para ponto flutuante (float)
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza as operações matemáticas básicas
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Exibe os resultados de soma, subtração e multiplicação
print(f"\nSoma: {num1} + {num2} = {soma}")
print(f"Subtração: {num1} - {num2} = {subtracao}")
print(f"Multiplicação: {num1} * {num2} = {multiplicacao}")

# Desafio: Verifica se o segundo número é zero antes de realizar a divisão
if num2 == 0:
    print("Divisão: Erro! Não é possível dividir por zero.")
else:
    divisao = num1 / num2
    print(f"Divisão: {num1} / {num2} = {divisao}")

