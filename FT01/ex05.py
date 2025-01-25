# Sejam a e b os catetos de um triângulo retângulo, faz um programa que devolva o valor da hipotenusa
import math
a = float(input("Digite o valor do cateto a: "))
b = float(input("Digite o valor do cateto b: "))

hipotenusa = math.sqrt(a**2 + b**2)

print(f"A hipotenusa do triângulo retângulo é {round(hipotenusa,2)}")