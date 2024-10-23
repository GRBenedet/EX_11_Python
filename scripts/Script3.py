#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

jogador = v = 0

choice = ' '



while True:
    mach = random.randint(0 , 10)
    choice = ' '

    while choice not in 'PI':
        choice = str(input('PAR ou IMPAR? ')).strip().upper() [0]

    jogador = int(input('escolha de um numero: '))
    s = mach + jogador
    print(f'{jogador} + {mach} = {s}')

    if s % 2 != 0 and choice == 'I':
        print('Vitoria!!!')
        v += 1

    elif s % 2 == 0 and choice == 'P':
        print('Vitoria!!!')
        v += 1

    elif s % 2 != 0 and choice != 'I':
        print('Derrota!!!')
        break

    elif s % 2 == 0 and choice != 'P':
        print('Derrota!!!')
        break

print(f'parabens você teve um total de {v} vitorias!!!')