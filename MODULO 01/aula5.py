#Cenário: O sistema de uma escola precisa calcular a média aritmética final de um estudante do ensino técnico com base em suas 3 notas bimestrais.
#Enunciado: Escreva um programa em Python que:
#Solicite o nome do aluno.
#Leia 3 notas bimestrais (valores decimais/float).
#Calcule a média aritmética simples das três notas.
#Exiba o nome do aluno e a média final formatada com 2 casas decimais.


# Entrada de dados
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))

# Processamento (Cálculo da média)
media = (nota1 + nota2 + nota3) / 3

# Saída de dados formatada
print(f"Aluno(a): {nome}")
print(f"Média Final: {media:.2f}")