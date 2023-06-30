entrada = input('Você quer entrar ou sair?\n')

entrar = entrada == 'entrar'
sair = entrada == 'sair'

if entrar:
    print('Bem-vindo ao sistema!')
elif sair:
    print('Até a próxima!')
