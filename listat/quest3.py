def ProgramaOrdenacao():
    vetor = []

    for i in range(10):
        numero = int(input(f"Digite o número {i+1}: "))
        if numero%2==0:
            vetor.append(numero);
        

    vetor.sort()

    return vetor

vetor_par = ProgramaOrdenacao()

print("Os números pares digitados são:", vetor_par)