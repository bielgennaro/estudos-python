"""
Interpolação básica de strings
s - string
d e i -  int
f - float
x e X - Hexadecimal
"""


nome = 'Gabriel'
preco = 1000.495598309

variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08x' % (1500, 1000))
