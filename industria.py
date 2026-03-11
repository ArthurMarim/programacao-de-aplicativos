id_usuario = int(input("Qual o seu ID? "))
temperatura = int(input("Digite a temperatura: "))
tempo = float(input("Digite o tempo: "))

if id_usuario % 3 == 0 and (temperatura >= 40 or tempo > 8.00):
    print = (f"Funcionário {id_usuario}, você foi escalado para a manutenção preventiva hoje.")
else:
    print = (f"Funcionario {id_usuario} sua maquina opera dentro dos padroes normais.")
