def check(cpf, contador, teste):   
    psum = 0

    for digito in cpf:     
         psum += int(digito) * contador
         contador -= 1

    digito = (psum * 10) % 11
    digito = digito if digito <= 9 else 0

    return str(digito) == teste

def triagem_check(cpf):

    digito1 = cpf[-2]
    digito2 = cpf[-1]
    cpf = cpf[:9]

    #Check primeiro digito
    check_digit = check(cpf, len(cpf) + 1, digito1)

    if check_digit:
        
        #Check segundo digito
        cpf += digito1
        check_digit = check(cpf, len(cpf) + 1, digito2)

        if check_digit:
            return True
        
        return False

    return False


