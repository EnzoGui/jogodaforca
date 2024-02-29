import random, os



palavras_comida = [' banana', ' abacate', ' arroz', ' frango', ' batata', ' feijoada', ' lasanha']
palavras_objetos =[' tesoura', ' lápis', ' borracha', ' parafuso', ' vassoura']
letras_acertadas = ' '
chances = 8


while True:
    iniciar = input('você quer jogar?[S] ou [N]:').upper() #Início do jogo.
    
    if iniciar == 'S':
        print('As regras são simples: tente acertar todas as letras antes que suas chances acabem.')
        pass
    elif iniciar == 'N':
        break
    else:
        print('Digite uma das opções')
        continue
        
    print('comida opção[1]') #O jogador escolhe qual o tipo de palavra que quer jogar.
    print('objetos opção[2]')
    
    try:
       select = int(input(('Selecione a categoria da palavra que você quer:'))) 
    except:
        print('Digite uma opção válida')
        continue
    
    if select == 1:  
        palavra_secreta = random.choice(palavras_comida)  #Estrutura que vai escolher aleatoriamente uma palavra contida na lista selecionada pelo jogador.
    elif select == 2:
        palavra_secreta = random.choice(palavras_objetos)
    else:
        print('Digite uma uma opção válida')
        continue
    
    print(f'Sua palavra tem {len(palavra_secreta)} letras')
    
    while True:
        print(f'você atualmente tem {chances} tentativas') #Inserir a letra desejada mostrar quantas chances o jogador tem.
        letra_insert = input('Digite uma letra: ').lower()
        if len(letra_insert) > 1:
            print('Digite apenas uma letra')
            continue
        chances -= 1
        
        if letra_insert in palavra_secreta: #Verificação da letra inserida, se for um acerto, o sistema vai contabilizar.
            letras_acertadas += letra_insert
            
        palavra_formada = ''
        for letra in palavra_secreta: #Para cada indice em palavra secreta, será feita a verificação se houve alguma letra acertada.
            if letra in letras_acertadas:
                palavra_formada += letra
            else:
                palavra_formada += '*'
    
        print(f'palavra formada:{palavra_formada}')
        
        if palavra_formada == palavra_secreta: #Vence o jogo se acertou tudo.
            os.system('clear')
            print('parabéns você venceu o jogo')
            chances = 8
            letras_acertadas = ' '
            break
        elif chances == 0: #Se suas chances acabarem antes de completar o jogo, você perde.
            os.system('clear')
            print('Você perdeu o jogo!')
            chances = 8
            letras_acertadas = ' '
            break
