# Matriz 3x3 representando o estande da padaria
estande = [
    ["Bolo de Cenoura", "Sonho", "Torta"],       # Linha 0: Doces
    ["Pão de Queijo", "Coxinha", "Empada"],      # Linha 1: Salgados
    ["Café", "Suco", "Leite"]                    # Linha 2: Bebidas
]

#1. Acessar o "Pão de Queijo" (Linha 1, Coluna 0)
print(f"Item selecionado: {estande[1][0]}")

#2. Exibir o número de prateleiras (linhas) e itens por prateleira (colunas)
print(f"Total de prateleiras: {len(estande)}")
print(f"Itens por prateleira: {len(estande[0])}")


#3. Imprimir toda a matriz formatada em formato de tabela
print("\n--- CATALOGO COMPLETO DA PADARIA ---")
for linha in range(len(estande)):
    for coluna in range(len(estande[linha])):
        print(f"[{estande[linha][coluna]}]", end=" ")
    print()  # Pula linha ao final de cada prateleira