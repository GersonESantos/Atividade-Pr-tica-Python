# Solicita o nome do aluno e as duas notas
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média aritmética das duas notas
media = (nota1 + nota2) / 2

# Verifica a situação do aluno com base na média
if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

# Exibe o resultado final
print(f"\nAluno: {nome}")
print(f"Média: {media:.1f}")
print(f"Situação: {situacao}")

