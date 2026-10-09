# Entrada de dados
valor_hora = float(input("Digite o valor recebido por hora trabalhada (R$): "))
horas_trabalhadas = float(input("Digite o total de horas trabalhadas no mês: "))

# Processamento
salario_bruto = valor_hora * horas_trabalhadas
desconto_inss = salario_bruto * 0.08
salario_liquido = salario_bruto - desconto_inss

# Saída de dados formatada
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto INSS (8%): R$ {desconto_inss:.2f}")
print(f"Salário Líquido a receber: R$ {salario_liquido:.2f}")