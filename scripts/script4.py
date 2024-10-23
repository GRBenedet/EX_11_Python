#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

cont = h = gc = fc = i = 0
g = ' '


while True:
    g = str(input('qual o genero? [M/F]')).strip().upper() [0]
    i = int(input('qual a idade dessa pessoa? '))

    if g == 'F':
        if i < 20:
            fc += 1
            if i > 18:
                gc += 1
        else: 
            gc += 1

    else:
        h += 1

        if i > 18:
            gc += 1
    cont += 1
    val = str(input('deseja continuar? [S/N] ')).strip().upper() [0]
    if val in 'N':
        break

print(f'o total de pessoas registradas foi {cont}, tendo {gc} maiores de 18, {fc} mulheres com menos de 20 anos e {h} homens.')