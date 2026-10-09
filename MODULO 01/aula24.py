for lote in range(1, 5):
    dias = int(input(f"Digite os dias para vencer o {lote}º lote: "))

    if dias < 5:
        print(f"Lote {lote}: ALERTA! Colocar em promoção (Validade próxima)")
    else:
        print(f"Lote {lote}: Produto em estado normal.\n")