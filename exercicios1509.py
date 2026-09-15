# def busca_sequencial(vetor, numero):
#     for i in range(10):
#         if vetor[i] == numero:
#             return i
#     return -1


# vetor = [5, 12, 8, 20, 3, 15, 7, 10, 25, 1]

# numero = int(input("Digite o número que deseja buscar: "))

# indice = busca_sequencial(vetor, numero)

# if indice != -1:
#     print("Número encontrado no índice:", indice)
# else:
#     print("Número não encontrado.")



# def contar_ocorrencias(lista, valor):
#     contador = 0

#     for item in lista:
#         if item == valor:
#             contador += 1

#     return contador


# lista = [5, 2, 8, 2, 10, 2, 7, 3, 2, 6]

# valor = int(input("Digite o valor que deseja buscar: "))

# quantidade = contar_ocorrencias(lista, valor)

# print("O valor aparece", quantidade, "vezes na lista.")


# def maior_e_posicao(vetor):
#     maior = vetor[0]
#     posicao = 0

#     for i in range(1, len(vetor)):
#         if vetor[i] > maior:
#             maior = vetor[i]
#             posicao = i

#     return maior, posicao


# vetor = [10, 25, 7, 42, 18, 30, 5, 15, 35, 20]

# maior, posicao = maior_e_posicao(vetor)

# print("Maior número:", maior)
# print("Posição:", posicao)


# def buscar_aluno(alunos, nome):
#     for aluno in alunos:
#         if aluno == nome:
#             return True
#     return False


# alunos = ["Ana", "Carlos", "João", "Maria", "Pedro"]

# nome = input("Digite o nome do aluno: ")

# if buscar_aluno(alunos, nome):
#     print("Aluno encontrado!")
# else:
#     print("Aluno não encontrado.")



# def buscar_posicoes(vetor, numero):
#     primeira = -1
#     ultima = -1

#     for i in range(len(vetor)):
#         if vetor[i] == numero:
#             if primeira == -1:
#                 primeira = i
#             ultima = i

#     return primeira, ultima


# vetor = [5, 2, 8, 2, 10, 2, 7, 3, 2, 6]

# numero = int(input("Digite o número: "))

# primeira, ultima = buscar_posicoes(vetor, numero)

# if primeira != -1:
#     print("Primeira posição:", primeira)
#     print("Última posição:", ultima)
# else:
#     print("Número não encontrado.")


