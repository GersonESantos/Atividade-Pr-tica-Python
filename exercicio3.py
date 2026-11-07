# Solicita um número inteiro ao usuário e converte com int()
numero = int(input("Digite um número inteiro: "))

# Verifica se o resto da divisão por 2 é igual a 0 usando o operador módulo (%)
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

