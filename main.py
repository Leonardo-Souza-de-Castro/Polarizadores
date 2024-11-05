resposta = int(input("""
Digite qual opção você gostaria de seguir:

1 - Calculos com 2 polarizadores

2 - Calculo com 3 polarizadores
"""))

if resposta == 1:
    opcao = int(input("""
Digite qual opção gostaria de seguir:
    
1 - θ1, θ2, I0

2 - θ1, θ2, I1

3 - θ1, θ2, I2
    """))

    match opcao:
        case(1):
            # Nesse caso entra os angulos a intensidade I0 e sai as instensidade I1 e I2
            angulo1 = float(input("Digite o angulo do primeiro polarizador: "))
            angulo2 = float(input("Digite o angulo do segundo polarizador: "))
            Intensidade = float(input("Digite a intensidade de luz (I0): "))
        case(2):
            # Nesse caso entra os angulos a intensidade I1 e sai as instensidade I0 e I2
            angulo1 = float(input("Digite o angulo do primeiro polarizador: "))
            angulo2 = float(input("Digite o angulo do segundo polarizador: "))
            Intensidade = float(input("Digite a intensidade de luz (I1): "))
        case(3):
            # Nesse caso entra os angulos a intensidade I2 e sai as instensidade I0 e I1
            angulo1 = float(input("Digite o angulo do primeiro polarizador: "))
            angulo2 = float(input("Digite o angulo do segundo polarizador: "))
            Intensidade = float(input("Digite a intensidade de luz (I2): "))


else:
    opcao = int(input("""
Digite qual opção gostaria de seguir:
    
1 - θ1, θ2, θ3, I0

2 - θ1, θ2, θ3, I1

3 - θ1, θ2, θ3, I2

4 - θ1, θ2, θ3, I3
    """))

    match opcao:
        case(1):
            # Nesse caso entra os angulos a intensidade I0 e sai as instensidade I1, I2 e I3
            angulo1 = float(input("Digite o angulo do primeiro polarizador: "))
            angulo2 = float(input("Digite o angulo do segundo polarizador: "))
            angulo3 = float(input("Digite o angulo do terceiro polarizador: "))
            Intensidade = float(input("Digite a intensidade de luz (I0): "))
        case(2):
            # Nesse caso entra os angulos a intensidade I1 e sai as instensidade I0, I2 e I3
            angulo1 = float(input("Digite o angulo do primeiro polarizador: "))
            angulo2 = float(input("Digite o angulo do segundo polarizador: "))
            angulo3 = float(input("Digite o angulo do terceiro polarizador: "))
            Intensidade = float(input("Digite a intensidade de luz (I1): "))
        case(3):
            # Nesse caso entra os angulos a intensidade I2 e sai as instensidade I0, I1 e I3
            angulo1 = float(input("Digite o angulo do primeiro polarizador: "))
            angulo2 = float(input("Digite o angulo do segundo polarizador: "))
            angulo3 = float(input("Digite o angulo do terceiro polarizador: "))
            Intensidade = float(input("Digite a intensidade de luz (I2): "))
        case(4):
            # Nesse caso entra os angulos a intensidade I3 e sai as instensidade I0, I1 e I2
            angulo1 = float(input("Digite o angulo do primeiro polarizador: "))
            angulo2 = float(input("Digite o angulo do segundo polarizador: "))
            angulo3 = float(input("Digite o angulo do terceiro polarizador: "))
            Intensidade = float(input("Digite a intensidade de luz (I3): "))