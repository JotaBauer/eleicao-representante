e=0
i = 0
ana=0
bruno=0
carlos=0
votos=0
votos_brancos=0
while e == 0:
    print('===ELEIÇÃO PARA REPRESENTANTE===')

    print('1 - Votar em Ana')
    print('2 - Votar em Bruno')
    print('3 - Votar em Carlos')
    print('4 - Votar em branco')
    print('5 - Consultar resultado parcial')
    print('6 - Encerrar votação')

    i = int(input('Escolha uma opção: '))

    if i == 1:
        print('Você votou na Ana')
        ana+=1
        votos+=1

    elif i == 2:
        print('Você votou no Bruno')
        bruno +=1
        votos += 1

    elif i == 3:
        print('Você votou no Carlos')
        carlos +=1
        votos += 1

    elif i == 4:
        print('Você votou em branco')
        votos_brancos +=1
        votos += 1

    elif i == 5:
        print('Resultado Parcial')
        print(f' Ana    : {ana}')
        print(f' Bruno  : {bruno}')
        print(f' Carlos : {carlos}')
        print(f' Branco : {votos_brancos}')
        print(f' Total  : {votos}')

    elif i == 6:
        print('===RESULTADO FINAL DA ELEIÇÃO===')

        print(f'A Ana recebeu {ana} votos')
        print(f'O Bruno recebeu {bruno} votos')
        print(f'O Carlos recebeu {carlos} votos')

        print(f'Houveram {votos_brancos} votos brancos')
        print(f'Houveram {votos} votos')


        if ana > bruno and ana > carlos:
            print(f'A Ana foi a vencedora com {ana} votos')

        elif bruno > ana and bruno > carlos:
            print(f'O Bruno foi o vencedor com {bruno} votos')

        elif carlos > ana and carlos > bruno:
            print(f'O Carlos foi o vencedor com {carlos} votos')

        elif ana == bruno:
            if ana == carlos:
                print('Houve um empate triplo')

        else:
            print('Houve um empate')
        break

