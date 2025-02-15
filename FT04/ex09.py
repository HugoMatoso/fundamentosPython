#Reescreve o programa anterior de forma a apresentar a tabuada de qualquer número introduzido pelo utilizador.

tab = int(input("Digite um número para saber sua tabuada: "))

i = 1
while i <= 10:
    print(f"{tab} x {i} = {tab * i}")
    i += 1