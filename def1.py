def verificar_nota(nota):
    if nota >= 9:
        return "Excelente"
    if nota >= 7:
        return "Bom"
    if nota > 5:
        return "Regular"
    else:
        return "Insuficiente"

valor_nota = int(input("Digite sua nota: "))
msg = verificar_nota(valor_nota)
print (msg)
