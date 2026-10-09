for geladeira in range(1, 4):
    temp = float(input(f"Digite a temperatura da geladeira {geladeira} (°C): "))

    if temp >= 2 and temp <= 8:
        print(f"Geladeira {geladeira}: OK! Temperatura segura.\n")
    else:
        print(f"Geladeira {geladeira}: ATENÇÃO! Temperatura fora do padrão!\n)
