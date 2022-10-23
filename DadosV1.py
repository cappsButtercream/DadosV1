from time import sleep
import random
print('-=-'*10)
print('Dados. <-- ponto final')
print('-=-'*10)
dados = 'o'
while dados != 'n':
    dados = str(input('Quer girar os dados?[S/N]: '))
    if dados == 's'.lower():
        print('CALCULANDO...')
        sleep(2)
        print(f'O primeiro dado jogado deu o número : {random.randint(1, 6)}')
        print(f'O segundo dado jogado deu o número : {random.randint(1, 6)}')
        p1 = str(input('Quer continuar Girando?[S/N]: '))
        if p1 == 'n'.lower():
            break
print('Obrigado por jogar!')
