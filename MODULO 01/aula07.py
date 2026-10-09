# 1. Entrada de dados
valor_hora = float(input("Digite quanto ganha por hora (R$): "))
horas = float(input("Digite quantas horas trabalhou no mês: "))

# 2. Processamento (Cálculo direto)
salario = valor_hora * horas

# 3. Saída de dados
print(f"O salário total a receber é: R$ {salario:.2f}")