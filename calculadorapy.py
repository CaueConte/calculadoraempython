
__doc__ = "Esse modulo tem objetivo ser uma calculadora rodada no"


import os

soma = 0
subtracao = 0
multiplicacao = 0
divisao = 0
numeroa = 0
numerob = 0
print("1-Soma")
print("2-subtracao")
print("3-Multiplicacao")
print("4-Divisao")

while True:
    try:
        escolha = int(input("Escolha operacao: "))
        numeroa = int(input("Digite o numero a: "))
        numerob = int(input("Digite o numero b: "))
        #print("1-Soma")
        #print("2-subtracao")
        #print("3-Multiplicacao")
       #print("4-Divisao")
        if escolha == 1:
            print(numeroa + numerob)
        elif escolha == 2:
            print(numeroa - numerob)
        elif escolha == 3:
            print(numeroa * numerob)
        elif escolha == 4:
            print(numeroa / numerob)
        else:
            pass
    except:
        print()
        