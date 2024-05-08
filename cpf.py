def validarcpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return 0
    d1 = (sum(int(cpf[i]) * (10 - i) for i in range(9)) * 10) % 11
    d2 = (sum(int(cpf[i]) * (11 - i) for i in range(10)) * 10) % 11
    if d1 == 10:
        d1 = 0
    if d2 == 10:
        d2 = 0
    return 1 if int(cpf[-2]) == d1 and int(cpf[-1]) == d2 else 0

cpf = input('Insira um CPF para validar: ')
resultado=validarcpf(cpf)
if resultado==1:
    print('CPF Válido')
else:
    print('CPF Inválido')