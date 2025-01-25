# Faz um programa que receba a distância em km e a quantidade em litros de combustível consumido por um carro num percurso. Calcula o consumo km/l e escreve uma mensagem de acordo com o resultado obtido

distancia = float(input("Digite a distância em km: "))
litros = float(input("Digite a quantidade de litros de combustível consumido: "))
consumo = distancia / litros

print(f"O carro obteve um consumo de {round(consumo,2)} km/l")