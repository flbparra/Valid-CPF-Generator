import sys

def choice_service():

    while True:
        print('Escolha uma das opções: ')
        print("1 - Gerar Novo CPF")
        print('2 - Verificar se o CPF é Válido')

        try:
            escolha = int(input('Digite a opção desejada: '))
            if escolha in (1,2):
                return escolha
            else:
                print('Digite 1 ou 2 (para escolher o serviço)')
                continue 

        except ValueError as error:
            print(error.__class__.__name__ ,'- Digite 1 ou 2 (para escolher o serviço)')
            continue

        if escolha in (1, 2):
            return escolha
        
        else:
            print('Digite uma opção válida: 1 ou 2')
            sys.system('clear')
            continue