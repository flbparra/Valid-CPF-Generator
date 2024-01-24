import re, time, sys

from cpf_package.check_cpf import triagem_check, check

def input_cpf():

    while True:

        cpf = input('Digite o CPF aqui: ')

        cpf = re.sub( r'[^0-9]', '', cpf)

        if len(cpf) != 11:
            print(f'Digite um cpf válido, tem {len(cpf)} digitos. O correto é ter 11 digitos númerico.')
            print('Aguarde um instante...')
            time.sleep(2)
            sys.system('clear')
            continue

        else:

            valid_check = triagem_check(cpf)
            if valid_check:
                return 'CPF válido!'
            
            else:
                return 'CPF inválido!'

