valor_compra = float(input("Digite o valor da compra (R$): "))
if valor_compra < 100:
    desconto = 0
elif valor_compra <= 200:
    desconto = 10
else:
    desconto = 20
desconto = valor_compra * desconto/100
valor_final = valor_compra-desconto
#valor_final = valor_compra - (valor_compra * desconto)

print(f"Desconto aplicado: {desconto:.0f}%")
print(f"Valor final a pagar: R$ {valor_final:.2f}")