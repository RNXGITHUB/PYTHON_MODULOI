media = float(input("Digite a média final do aluno (0 a 10): "))

if media >= 7.0:
    print("Situação: Aprovado (Conceito A)")
elif media >= 5.0:
    print("Situação: Em Recuperação (Conceito B)")
else:
    print("Situação: Reprovado (Conceito C)")
