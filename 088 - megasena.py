from random import randint
from time import sleep

lista_jogos = []
lista_cartela = []

cartela = int(input('Quantos jogos sortear? '))

print('=' * 22)
print(f'{"PALPITES MEGASENA":^22}')
print('=' * 22)

while len(lista_cartela) < cartela:
    while len(lista_jogos) < 6:
        numero = randint(1, 60)
        if numero not in lista_jogos:
            lista_jogos.append(numero)
    lista_jogos.sort()
    lista_cartela.append(lista_jogos[:])
    lista_jogos.clear()

cont = 1
for j in range(0, len(lista_cartela)):
    for n in lista_cartela[j]:
        if cont < 6:
            print(f'{n:02d}', end=', ')
            cont += 1
        else:
            print(f'{n:02d}')
            cont = 1
    sleep(1)
print('=' * 22)
print(f'{"BOA SORTE FDP":^22}')
print('=' * 22)