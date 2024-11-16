from math import cos, radians

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
            Intensidade = float(input("Digite a intensidade de luz (I0): "))
            angulo1 = radians(float(input("Digite o angulo do primeiro polarizador: ")))
            angulo2 = radians(float(input("Digite o angulo do segundo polarizador: ")))

            tipo = input("""
A luz inicial é polarizada?
                  
s - Sim
n - Não

""")
            
            if tipo == "s":
                I1 = Intensidade*(cos(angulo1)**2)

                I2 = I1*(cos(angulo2)**2)
            else:
                I1 = Intensidade/2
                print(cos(angulo2))
                print(cos(angulo2)**2)

                I2 = I1*(cos(angulo2)**2)

            
            print(f"""
I1 = {I1}

I2 = {I2}
""")

        case(2):
            # Nesse caso entra os angulos a intensidade I1 e sai as instensidade I0 e I2
            Intensidade = float(input("Digite a intensidade de luz (I1): "))
            angulo1 = radians(float(input("Digite o angulo do primeiro polarizador: ")))
            angulo2 = radians(float(input("Digite o angulo do segundo polarizador: ")))

            tipo = input("""
A luz inicial é polarizada?
                  
s - Sim
n - Não

""")
            
            if tipo == "s":
                I0 = Intensidade/(cos(angulo1)**2)

                I2 = Intensidade*(cos(angulo2)**2)
            else:
                I0 = Intensidade*2

                I2 = Intensidade*(cos(angulo2)**2)

            print(f"""
I0 = {I0}

I2 = {I2}
""")
        case(3):
            # Nesse caso entra os angulos a intensidade I2 e sai as instensidade I0 e I1
            Intensidade = float(input("Digite a intensidade de luz (I2): "))
            angulo2 = radians(float(input("Digite o angulo do segundo polarizador: ")))
            angulo1 = radians(float(input("Digite o angulo do primeiro polarizador: ")))

            tipo = input("""
A luz inicial é polarizada?
                  
s - Sim
n - Não

""")
            
            if tipo == "s":
                I1 = Intensidade/(cos(angulo2)**2)

                I0 = I1/(cos(angulo1)**2)
            else:
                I1 = Intensidade/(cos(angulo2)**2)
                
                I0 = I1*2

            print(f"""
I0 = {I0}

I1 = {I1}
""")

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
            Intensidade = float(input("Digite a intensidade de luz (I0): "))
            angulo1 = radians(float(input("Digite o angulo do primeiro polarizador: ")))
            angulo2 = radians(float(input("Digite o angulo do segundo polarizador: ")))
            angulo3 = radians(float(input("Digite o angulo do terceiro polarizador: ")))

            tipo = input("""
A luz inicial é polarizada?
                  
s - Sim
n - Não

""")
            
            if tipo == "s":
                I1 = Intensidade*(cos(angulo1)**2)
                I2 = I1*(cos(angulo2)**2)

                I3 = I2*(cos(angulo3)**2)
            else:

                I1 = Intensidade/2
                I2 = I1*(cos(angulo2)**2)
                I3 = I2*(cos(angulo3)**2)

                

            print(f"""
I1 = {I1}

I2 = {I2}                  

I3 = {I3}
""")
        case(2):
            # Nesse caso entra os angulos a intensidade I1 e sai as instensidade I0, I2 e I3
            Intensidade = float(input("Digite a intensidade de luz (I1): "))
            angulo1 = radians(float(input("Digite o angulo do primeiro polarizador: ")))
            angulo2 = radians(float(input("Digite o angulo do segundo polarizador: ")))
            angulo3 = radians(float(input("Digite o angulo do terceiro polarizador: ")))

            tipo = input("""
A luz inicial é polarizada?
                  
s - Sim
n - Não

""")
            
            if tipo == "s":
                I0 = Intensidade/(cos(angulo1)**2)
                I2 = Intensidade*(cos(angulo2)**2)

                I3 = I2*(cos(angulo3)**2)
            else:

                I0 = Intensidade*2
                I2 = Intensidade*(cos(angulo2)**2)
                I3 = I2*(cos(angulo3)**2)

                

            print(f"""
I0 = {I0}

I2 = {I2}                  

I3 = {I3}
""")
        case(3):
            # Nesse caso entra os angulos a intensidade I2 e sai as instensidade I0, I1 e I3
            Intensidade = float(input("Digite a intensidade de luz (I2): "))
            angulo1 = radians(float(input("Digite o angulo do primeiro polarizador: ")))
            angulo2 = radians(float(input("Digite o angulo do segundo polarizador: ")))
            angulo3 = radians(float(input("Digite o angulo do terceiro polarizador: ")))

            tipo = input("""
A luz inicial é polarizada?
                  
s - Sim
n - Não

""")
            
            if tipo == "s":
                I1 = Intensidade/(cos(angulo2)**2)
                I0 = I1/(cos(angulo1)**2)

                I3 = Intensidade*(cos(angulo3)**2)
            else:

                I1 = Intensidade/(cos(angulo2)**2)
                I0 = I1*2
                I3 = Intensidade*(cos(angulo3)**2)

                

            print(f"""
I0 = {I0}

I1 = {I1}                  

I3 = {I3}
""")
        case(4):
            # Nesse caso entra os angulos a intensidade I3 e sai as instensidade I0, I1 e I2
            Intensidade = float(input("Digite a intensidade de luz (I3): "))
            angulo3 = radians(float(input("Digite o angulo do terceiro polarizador: ")))
            angulo2 = radians(float(input("Digite o angulo do segundo polarizador: ")))
            angulo1 = radians(float(input("Digite o angulo do primeiro polarizador: ")))

            tipo = input("""
A luz inicial é polarizada?
                  
s - Sim
n - Não

""")
            
            if tipo == "s":
                I2 = Intensidade/(cos(angulo3)**2)
                I1 = I2/(cos(angulo2)**2)

                I0 = I1/(cos(angulo1)**2)
            else:

                I2 = Intensidade/(cos(angulo3)**2)

                I1 = I2/(cos(angulo2)**2)
                
                I0 = I1*2

            print(f"""
I2 = {I2}                  

I0 = {I0}

I1 = {I1}
""")