import datetime

ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = datetime.datetime.now().year - ano_nascimento
cnh_true = idade > 18

if cnh_true:
    print('Você pode tirar CNH')
else:
    print('Você não pode tirar CNH')
