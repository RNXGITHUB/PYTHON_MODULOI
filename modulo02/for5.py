# O laço roda para 5 pessoas (de 1 a 5)
for i in range(1, 6):
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    
    # Estrutura condicional dentro do loop
    if idade >= 18:
        print(f"Pessoa {i}: Acesso LIBERADO! Bom filme.\n")
    else:
        print(f"Pessoa {i}: Acesso NEGADO! Apenas para maiores de 18 anos.\n")