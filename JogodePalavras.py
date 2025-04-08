import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0


while True:
  
    letra_digitada = input('Digite uma letra:')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    print(letra_digitada)

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palava_formada += letra_secreta
        else:
            palavra_formada += '*'
    print ('Palavra formada: ', palava_formada)

    if palava_formada == palavra_secreta:
        os.system('clear')
        print('Você ganhou!')
        print('A palavra era: ', palavra_secreta)
