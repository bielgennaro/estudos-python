nome = input("Digite seu nome: ")
letras = len(nome)

if letras > 1:
    if letras <= 4:
        print('Seu nome é mto curto')
    elif letras >= 5 and letras <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais uma letra')
