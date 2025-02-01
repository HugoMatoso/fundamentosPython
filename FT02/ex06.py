# Escreve um programa que solicite a temperatura em Fahrenheit (F), ao utilizador, e a converta para grau Celsius (C), devolvendo o resultado da conversão

f = float(input("Digite a temperatura em Fahrenheit: "))

c = 5 * ((f - 32) / 9)

print(f"A temperatura em Celsius é {c:.1f}")