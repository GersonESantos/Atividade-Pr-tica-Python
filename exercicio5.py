# Solicita o valor original da compra
valor_original = float(input("Digite o valor da compra (R$): "))

# Define o percentual de desconto com base nas regras da loja
if valor_original > 500:
    percentual_desconto = 15
elif valor_original > 200:
    percentual_desconto = 10
else:
    percentual_desconto = 0

# Calcula o valor do desconto e o valor final da compra
valor_descontado = valor_original * (percentual_desconto / 100)
valor_final = valor_original - valor_descontado

# Exibe o resumo detalhado da compra
print(f"\nValor original: R$ {valor_original:.2f}")
print(f"Percentual de desconto: {percentual_desconto}%")
print(f"Valor descontado: R$ {valor_descontado:.2f}")
print(f"Valor final da compra: R$ {valor_final:.2f}")

