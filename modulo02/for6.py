total_compra = 0

for item in range(1, 5):
    preco = float(input(f"Digite o preço do {item}º item (R$): "))
    total_compra = total_compra + preco

print(f"Total da compra: R$ {total_compra:.2f}")
