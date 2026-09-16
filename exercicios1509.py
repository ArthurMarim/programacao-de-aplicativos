# 1- def busca_sequencial(vetor, numero):
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



# 2- def contar_ocorrencias(lista, valor):
#     contador = 0

#     for item in lista:
#         if item == valor:
#             contador += 1

#     return contador


# lista = [5, 2, 8, 2, 10, 2, 7, 3, 2, 6]

# valor = int(input("Digite o valor que deseja buscar: "))

# quantidade = contar_ocorrencias(lista, valor)

# print("O valor aparece", quantidade, "vezes na lista.")


# 3- def maior_e_posicao(vetor):
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


# 4- def buscar_aluno(alunos, nome):
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



# 5- def buscar_posicoes(vetor, numero):
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

# 6- def busca_binaria(vetor, alvo):
#     inicio = 0
#     fim = len(vetor) - 1

#     while inicio <= fim:
#         meio = (inicio + fim) // 2

#         if vetor[meio] == alvo:
#             return meio
#         elif vetor[meio] < alvo:
#             inicio = meio + 1
#         else:
#             fim = meio - 1

#     return -1

# 7 - def busca_binaria_palavra(palavras, palavra):
#     inicio = 0
#     fim = len(palavras) - 1

#     while inicio <= fim:
#         meio = (inicio + fim) // 2

#         if palavras[meio] == palavra:
#             return meio
#         elif palavras[meio] < palavra:
#             inicio = meio + 1
#         else:
#             fim = meio - 1

#     return -1


# 8- def busca_binaria(vetor, alvo):
#     inicio = 0
#     fim = len(vetor) - 1
#     comparacoes = 0

#     while inicio <= fim:
#         meio = (inicio + fim) // 2
#         comparacoes += 1

#         if vetor[meio] == alvo:
#             return meio, comparacoes
#         elif vetor[meio] < alvo:
#             inicio = meio + 1
#         else:
#             fim = meio - 1

#     return -1, comparacoes

# 9- def posicao_insercao(vetor, numero):
#     inicio = 0
#     fim = len(vetor)

#     while inicio < fim:
#         meio = (inicio + fim) // 2

#         if vetor[meio] < numero:
#             inicio = meio + 1
#         else:
#             fim = meio

#     return inicio



# 10- def busca_sequencial(vetor, alvo):
#     comparacoes = 0

#     for i in range(len(vetor)):
#         comparacoes += 1

#         if vetor[i] == alvo:
#             return i, comparacoes

#     return -1, comparacoes


# def busca_binaria(vetor, alvo):
#     inicio = 0
#     fim = len(vetor) - 1
#     comparacoes = 0

#     while inicio <= fim:
#         meio = (inicio + fim) // 2
#         comparacoes += 1

#         if vetor[meio] == alvo:
#             return meio, comparacoes
#         elif vetor[meio] < alvo:
#             inicio = meio + 1
#         else:
#             fim = meio - 1

#     return -1, comparacoes

# vetor = list(range(1, 101))

# valores = [1, 50, 100]

# for valor in valores:
#     indice_seq, comp_seq = busca_sequencial(vetor, valor)
#     indice_bin, comp_bin = busca_binaria(vetor, valor)

#     print(f"Valor: {valor}")
#     print(f"  Sequencial: índice {indice_seq}, {comp_seq} comparações")
#     print(f"  Binária:    índice {indice_bin}, {comp_bin} comparações")
#     print()


