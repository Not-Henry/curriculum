# Este programa foi criado com a ajuda de vídeos do YouTube e um forum no stackoverflow
# This program was created with the help of YouTube videos and a forum on stackoverflow

### Vídeo do youtube/youtube video: https://www.youtube.com/watch?v=NV8QcOcZGeI
### Forum stackoverflow: https://pt.stackoverflow.com/questions/64608/como-validar-e-calcular-o-dígito-de-controle-de-um-cpf


from random import randint

# Validar CPF


def cpf_validar(numbers):
    #  Toma os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]

    #  Testifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Certifica-se de que todos os números do CPF não possuem o mesmo número. Exemplo: 888.888.888-88
    if cpf == cpf[::-1]:
        return False

    #  Valida os dígitos verificadores
    for i in range(9, 11):
        valor = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digito = ((valor * 10) % 11) % 10
        if digito != cpf[i]:
            return False
    return True

# Criar CPF


def cpf_gerar():
    #  Cria os primeiros nove números (e certifica-se de que não são todos iguais)
    while True:
        cpf = [randint(0, 9) for k in range(9)]
        if cpf != cpf[::-1]:
            break

    #  Gera os dígitos verificadores
    for i in range(9, 11):
        valor = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digito = ((valor * 10) % 11) % 10
        cpf.append(digito)

    #  Retorna o CPF como string
    resultado = ''.join(map(str, cpf))
    return resultado


opcao = int(input('''[1] Validar um CPF
[2] Gerar um CPF válido
Opção: '''))
if opcao == 1:
    cpf = input('Digite o CPF: ')
    if cpf_validar(cpf):
        print('CPF válido.')
    else:
        print('CPF inválido.')
elif opcao == 2:
    cpf = cpf_gerar()
    if cpf_validar(cpf):
        print(f'CPF gerado: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')
else:
    print('Inválido.')
