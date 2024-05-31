def ProgramaOrdenacao():
    vetor = []

    for i in range(10):
        numero = int(input(f"Digite o número {i+1}: "))
        vetor.append(numero)

    vetor.sort()

    return vetor

vetor_ordenado = ProgramaOrdenacao()

print("Os números digitados em ordem crescente são:", vetor_ordenado)