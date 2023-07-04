hora = int(input("Digite a hora (formato de 24 horas): "))

if hora < 0 or hora > 23:
    print("Hora inválida!")
elif hora < 12:
    print("Bom dia!")
elif hora < 18:
    print("Boa tarde!")
else:
    print("Boa noite!")
