import datetime


nome = "Gabriel"
sobrenome = "Zirondi"
idade = datetime.datetime.now().year - 2003
ano_nascimento = datetime.datetime.now().year - idade
maior_idade = idade > 18
altura_metros = float(1.70)

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('Maior de idade?', maior_idade)
print('Altura em metros:', altura_metros)
