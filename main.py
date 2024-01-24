import cpf_package


"""
-> Fazer Opções para o programa rodar.
-> Gerar um cpf válido e copiar para sua área de trabalho
-> Validar um CPF, usuário digita um cpf e a gente 
"""
service = cpf_package.choice_service()

if service == 1:
    print(cpf_package.cpf_init())

else:
    print(cpf_package.input_cpf())