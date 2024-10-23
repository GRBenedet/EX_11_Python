#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

n = 0


while True:
    n = int(input('digite o numero: '))
    for multi in range (1 , 11):
        print(f'{n} X {multi} = {n * multi}')
    if n < 0:
        break