calor = int(input("Digite a temperatura do sensor"))

if calor > 80:
    print ("PERIGO! Desligando servidor por superaquecimento!")
elif calor >= 50:
    print ("Alerta: Ventoinhas ligadas no máximo!")
elif calor < 50:
    print ("Temperatura estável. Sistema operando normalmente")

    

