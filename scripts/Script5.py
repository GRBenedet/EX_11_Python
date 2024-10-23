#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

nomep = ''
menorv = ''
menorp = float('inf') 
contm = cont = totalc = preco = 0

while True:
    nomep = str(input('Qual o nome do produto? '))
    preco = float(input('Valor desse produto: R$ '))
    
    totalc += preco 
    
    if preco > 1000:
        contm += 1  

    if preco < menorp:
        menorv = nomep
        menorp = preco
    cont += 1  
    
    op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break

print(f'O número de produtos é {cont}, o valor total é R${totalc:.2f}, e o produto mais barato é {menorv} custando R${menorp:.2f}')