def ProgramaHelloVetor():
    vetor = []

    for i in range(5):
        numero = int(input(f"Digite o número {i+1}: "))
        vetor.append(numero)

    print("Os números digitados foram:", vetor);

ProgramaHelloVetor()

