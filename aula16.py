nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja buscar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
elif encontrar not in nome:
    print(f'{encontrar} não esta em {nome}')
