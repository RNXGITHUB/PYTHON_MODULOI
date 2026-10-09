alunos = ["Ana", "Bruno", "Carla", "Daniel"]

# O enumerate retorna o índice (pos) e o conteúdo (aluno)
for pos, aluno in enumerate(alunos):
    print(f"{pos + 1}º Aluno: {aluno}")