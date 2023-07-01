nome = input('Digite seu nome: \n')
idade = input('Digite sua idade: \n')
nome_invertido = nome[::-1]
quantidade_letras = len(nome)

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
    if ' ' in nome:
        print(f'Seu contém espaçoes')
    print(f'Seu nome tem {quantidade_letras} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
elif nome and idade:
    print('Você deixou o campo nome vazio')
else:
    print('Você deixou o campo idade vazio')
