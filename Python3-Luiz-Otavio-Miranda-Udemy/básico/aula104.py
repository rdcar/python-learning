import random

cpf_nove = ""
for i in range(9):
    cpf_nove += str(random.randint(0,9))

resultado_1 = 0

contador_regressivo = 10
for digito_1 in cpf_nove:
    resultado_1 += int(digito_1) * contador_regressivo
    contador_regressivo -= 1

digito_1 = (resultado_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

cpf_dez = cpf_nove + str(digito_1)

resultado_2 = 0
contador_regressivo_2 = 11

for digito_2 in cpf_dez:
    resultado_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

# Validação do CPF

cpf_gerado = f"{cpf_nove}{digito_1}{digito_2}"
print(cpf_gerado)
