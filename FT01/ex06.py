# Faz um programa que receba três parâmetros inteiros (horas, minutos e segundos) e converta o resultado para segundos, devolvendo o output para o ecrã

hora = int(input("Insira a hora: "))
minuto = int(input("Insira o minuto: "))
segundo = int(input("Insira o segundo: "))
total_segundos = (hora * 3600) + (minuto * 60) + segundo

print("O total de segundos é:",total_segundos)