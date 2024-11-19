from math import cos, radians
from decimal import Decimal

print("""
_____________________________________________________
|                   Autores:                        |
|                                                   |
|   Bianca Silva Oliveira - R.A: 22.123.113-7       |
|   Felipe Brum Pereira - R.A: 22.123.112-9         |
|   Leonardo Souza de Castro - R.A: 22.123.114-5    |
|___________________________________________________|
""")

print("Este projeto tem o intuito de calcular Intensidade de luz após ela passar por polarizadores ou a luz inicial (tanto para luzes polarizadas como não polarizadas), sendo considerado casos com 2 polarizadores e 3. As informações que usaremos de entrada são a Intensidade em algum ponto do circuito e os angulos dos polarizadores e buscaremos ter como saida as demais intensidades do circuito podendo ser desde a luz inicial até a final passando por tudo, além dos pontos intermediarios.")

resposta = int(input("""
Digite qual opção você gostaria de seguir:

1 - Calculos com 2 polarizadores

2 - Calculo com 3 polarizadores

0 - Sair
"""))
while resposta != 0 :
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
                Intensidade = Decimal(input("Digite a intensidade de luz (I0) W/cm²: "))
                angulo1 = radians(float(input("Digite o angulo do primeiro polarizador (θ1°): ")))
                angulo2 = radians(float(input("Digite o angulo do segundo polarizador (θ2°): ")))

                tipo = input("""
A luz inicial é polarizada?
                  
s - Sim
n - Não

""")
            
                if tipo == "s":
                    I1 = Decimal(Intensidade*Decimal(cos(angulo1)**2))

                    I2 = Decimal(I1*Decimal(cos(angulo2)**2))
                else:
                    I1 = Decimal(Intensidade/2)

                    I2 = Decimal(I1*Decimal(cos(angulo2)**2))

                
                print(f"""
Resultados:

I1 = {I1:.2e} W/cm²

I2 = {I2:.2e} W/cm²
""")

                resposta = int(input("""
Digite qual opção você gostaria de seguir:

1 - Calculos com 2 polarizadores

2 - Calculo com 3 polarizadores

0 - Sair
"""))

            case(2):
                # Nesse caso entra os angulos a intensidade I1 e sai as instensidade I0 e I2
                Intensidade = Decimal(input("Digite a intensidade de luz (I1) W/cm²: "))
                angulo1 = radians(float(input("Digite o angulo do primeiro polarizador (θ1°): ")))
                angulo2 = radians(float(input("Digite o angulo do segundo polarizador (θ2°): ")))

                tipo = input("""
A luz inicial é polarizada?
                  
s - Sim
n - Não

""")
                
                if tipo == "s":
                    I0 = Decimal(Intensidade/Decimal(cos(angulo1)**2))

                    I2 = Decimal(Intensidade*Decimal(cos(angulo2)**2))
                else:
                    I0 = Decimal(Intensidade*2)

                    I2 = Decimal(Intensidade*Decimal(cos(angulo2)**2))

                print(f"""
Resultados:

I0 = {I0:.2e} W/cm²

I2 = {I2:.2e} W/cm²
""")

                resposta = int(input("""
Digite qual opção você gostaria de seguir:

1 - Calculos com 2 polarizadores

2 - Calculo com 3 polarizadores

0 - Sair
"""))
            case(3):
                # Nesse caso entra os angulos a intensidade I2 e sai as instensidade I0 e I1
                Intensidade = Decimal(input("Digite a intensidade de luz (I2) W/cm²: "))
                angulo2 = radians(float(input("Digite o angulo do segundo polarizador (θ2°): ")))
                angulo1 = radians(float(input("Digite o angulo do primeiro polarizador (θ1°): ")))

                tipo = input("""
A luz inicial é polarizada?
                  
s - Sim
n - Não

""")
            
                if tipo == "s":
                    I1 = Decimal(Intensidade/Decimal(cos(angulo2)**2))

                    I0 = Decimal(I1/Decimal(cos(angulo1)**2))
                else:
                    I1 = Decimal(Intensidade/Decimal(cos(angulo2)**2))
                    
                    I0 = Decimal(I1*2)

                print(f"""
Resultados:

I0 = {I0:.2e} W/cm²

I1 = {I1:.2e} W/cm²
""")

                resposta = int(input("""
Digite qual opção você gostaria de seguir:

1 - Calculos com 2 polarizadores

2 - Calculo com 3 polarizadores

0 - Sair
"""))

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
                Intensidade = Decimal(input("Digite a intensidade de luz (I0) W/cm²: "))
                angulo1 = radians(float(input("Digite o angulo do primeiro polarizador (θ1°): ")))
                angulo2 = radians(float(input("Digite o angulo do segundo polarizador (θ2°): ")))
                angulo3 = radians(float(input("Digite o angulo do terceiro polarizador (θ3°): ")))

                tipo = input("""
A luz inicial é polarizada?
                  
s - Sim
n - Não

""")
            
                if tipo == "s":
                    I1 = Decimal(Intensidade*Decimal(cos(angulo1)**2))
                    I2 = Decimal(I1*Decimal(cos(angulo2)**2))

                    I3 = Decimal(I2*Decimal(cos(angulo3)**2))
                else:

                    I1 = Decimal(Intensidade/2)
                    I2 = Decimal(I1*Decimal(cos(angulo2)**2))
                    I3 = Decimal(I2*Decimal(cos(angulo3)**2))
                print(f"""
Resultados:

I1 = {I1:.2e} W/cm²

I2 = {I2:.2e} W/cm²                  

I3 = {I3:.2e} W/cm²
""")

                resposta = int(input("""
Digite qual opção você gostaria de seguir:

1 - Calculos com 2 polarizadores

2 - Calculo com 3 polarizadores

0 - Sair
"""))                

            case(2):
                # Nesse caso entra os angulos a intensidade I1 e sai as instensidade I0, I2 e I3
                Intensidade = Decimal(input("Digite a intensidade de luz (I1) W/cm²: "))
                angulo1 = radians(float(input("Digite o angulo do primeiro polarizador (θ1°): ")))
                angulo2 = radians(float(input("Digite o angulo do segundo polarizador (θ2°): ")))
                angulo3 = radians(float(input("Digite o angulo do terceiro polarizador (θ3°): ")))

                tipo = input("""
A luz inicial é polarizada?
                  
s - Sim
n - Não

""")
            
                if tipo == "s":
                    I0 = Decimal(Intensidade/Decimal(cos(angulo1)**2))
                    I2 = Decimal(Intensidade*Decimal(cos(angulo2)**2))

                    I3 = Decimal(I2*Decimal(cos(angulo3)**2))
                else:

                    I0 = Decimal(Intensidade*2)
                    I2 = Decimal(Intensidade*Decimal(cos(angulo2)**2))
                    I3 = Decimal(I2*Decimal(cos(angulo3)**2))

                print(f"""
Resultados:

I0 = {I0:.2e} W/cm²

I2 = {I2:.2e} W/cm²                 

I3 = {I3:.2e} W/cm²
""")

                resposta = int(input("""
Digite qual opção você gostaria de seguir:

1 - Calculos com 2 polarizadores

2 - Calculo com 3 polarizadores

0 - Sair
"""))

            case(3):
                # Nesse caso entra os angulos a intensidade I2 e sai as instensidade I0, I1 e I3
                Intensidade = Decimal(input("Digite a intensidade de luz (I2) W/cm²: "))
                angulo1 = radians(float(input("Digite o angulo do primeiro polarizador (θ1°): ")))
                angulo2 = radians(float(input("Digite o angulo do segundo polarizador (θ2°): ")))
                angulo3 = radians(float(input("Digite o angulo do terceiro polarizador (θ3°): ")))

                tipo = input("""
A luz inicial é polarizada?
                  
s - Sim
n - Não

""")
                if tipo == "s":
                    I1 = Decimal(Intensidade/Decimal(cos(angulo2)**2))
                    I0 = Decimal(I1/Decimal(cos(angulo1)**2))

                    I3 = Decimal(Intensidade*Decimal(cos(angulo3)**2))
                else:

                    I1 = Decimal(Intensidade/Decimal(cos(angulo2)**2))
                    I0 = Decimal(I1*2)
                    I3 = Decimal(Intensidade*Decimal(cos(angulo3)**2))
                print(f"""
Resultados:

I0 = {I0:.2e} W/cm²

I1 = {I1:.2e} W/cm²               

I3 = {I3:.2e} W/cm²
""")

                resposta = int(input("""
Digite qual opção você gostaria de seguir:

1 - Calculos com 2 polarizadores

2 - Calculo com 3 polarizadores

0 - Sair
"""))
                
            case(4):
                # Nesse caso entra os angulos a intensidade I3 e sai as instensidade I0, I1 e I2
                Intensidade = Decimal(input("Digite a intensidade de luz (I3) W/cm²: "))
                angulo3 = radians(float(input("Digite o angulo do terceiro polarizador (θ3°): ")))
                angulo2 = radians(float(input("Digite o angulo do segundo polarizador (θ2°): ")))
                angulo1 = radians(float(input("Digite o angulo do primeiro polarizador (θ1°): ")))

                tipo = input("""
A luz inicial é polarizada?
                  
s - Sim
n - Não

""")
                if tipo == "s":
                    I2 = Decimal(Intensidade/Decimal(cos(angulo3)**2))
                    I1 = Decimal(I2/Decimal(cos(angulo2)**2))

                    I0 = Decimal(I1/Decimal(cos(angulo1)**2))
                else:

                    I2 = Decimal(Intensidade/Decimal(cos(angulo3)**2))

                    I1 = Decimal(I2/Decimal(cos(angulo2)**2))
                    
                    I0 = Decimal(I1*2)

                print(f"""
Resultados:

I0 = {I0:.2e} W/cm²

I1 = {I1:.2e} W/cm²

I2 = {I2:.2e} W/cm²                  
""")

                resposta = int(input("""
Digite qual opção você gostaria de seguir:

1 - Calculos com 2 polarizadores

2 - Calculo com 3 polarizadores

0 - Sair
"""))     