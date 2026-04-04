"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

entrada = input("Digite um número: ")

if entrada.isdigit():
    entrada = int(entrada)

    if entrada % 2 == 0:
        print(f"{entrada} é um número PAR")
    else:
        print(f"{entrada} é um número ÍMPAR")
        
else:
    print(f"{entrada} NÃO é um número!")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input("Digite a hora: ")
try:
    hora_int = int(entrada)
    if hora_int >= 0 and hora_int <= 11:
        print("Bom dia!")
    elif hora_int >= 12 and hora_int <= 17:
        print("Boa tarde!")
    elif hora_int >=18 and hora_int <= 23:
        print("Boa noite!")
    else:
        print(f"A hora precisa ser um número entre 0 e 23.  Você digitou {hora_int}.")
except:
    print(f"Você não digitou um número inteiro. '{entrada}' é uma string.")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu nome: ")

if nome.isdigit():
    print("Entrada inválida! Digite um NOME (string)")

else:
    if len(nome) <= 4:
        print(f"Seu nome '{nome}' é muito curto")
    elif len(nome) >= 5 and len(nome) <= 6:
        print(f"Seu nome '{nome}' é normal")
    else:
        print(f"Seu nome '{nome}' é muito grande")