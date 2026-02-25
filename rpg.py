dano =int(input("Qual é o seu dano? "))
boss =int(input("Quantos de vida tem o boss? "))
damage = boss - dano

print (dano)
print (boss)
print ("O dano causado no boss foi ", damage)

if dano < 1:
    print ("Voce não causou nenhum damage")

elif dano >= 1:
    print ("Voce deu dano no boss")
 