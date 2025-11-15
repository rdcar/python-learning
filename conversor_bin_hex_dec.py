# =================================================================
# CALCULADORA PARA CONVERSÃO DE BASE
# =================================================================

def decimal_para_binario(numero_decimal):
    """
    Função: Converte um número inteiro decimal (base 10) para uma string binária (base 2).
    Método: Divisões Sucessivas por 2.
    """
    if not isinstance(numero_decimal, int) or numero_decimal < 0:
        return "Erro: Entrada inválida. Espera-se um inteiro não negativo."
        
    if numero_decimal == 0:
        return "0"

    resultado_binario = ""
    quociente = numero_decimal
    
    # Loop continua enquanto o quociente for maior que zero
    while quociente > 0:
        # O resto da divisão por 2 é o bit (0 ou 1)
        resto = quociente % 2
        
        # Adiciona o resto ao INÍCIO da string (inversão da ordem)
        resultado_binario = str(resto) + resultado_binario
        
        # Atualiza o quociente para a próxima iteração (divisão inteira)
        quociente = quociente // 2
        
    return resultado_binario


def binario_para_decimal(numero_binario_str):
    """
    Função: Converte uma string binária (base 2) para um número inteiro decimal (base 10).
    Método: Expansão Posicional (Soma dos produtos do bit pela potência de 2).
    """
    # Validação básica para garantir que só há '0's e '1's
    if not all(c in '01' for c in numero_binario_str):
         return "Erro: A string binária deve conter apenas '0' e '1'."
         
    resultado_decimal = 0
    posicao_expoente = 0 
    
    # Itera sobre a string binária de TRÁS PARA FRENTE (do bit menos significativo)
    for bit_str in reversed(numero_binario_str):
        
        bit_int = int(bit_str)
        
        # Aumenta o acumulador decimal: bit * (2 elevado à posição)
        resultado_decimal += bit_int * (2 ** posicao_expoente)
        
        # Incrementa o expoente (o peso posicional)
        posicao_expoente += 1
        
    return resultado_decimal


def decimal_para_hexadecimal(numero_decimal):
    """
    Função: Converte um número inteiro decimal (base 10) para uma string hexadecimal (base 16).
    Método: Divisões Sucessivas por 16.
    """
    if not isinstance(numero_decimal, int) or numero_decimal < 0:
        return "Erro: Entrada inválida. Espera-se um inteiro não negativo."
        
    if numero_decimal == 0:
        return "0"
    
    # Mapeamento para os dígitos hexadecimais (A=10, B=11, ..., F=15)
    mapa_hex = "0123456789ABCDEF"
    resultado_hex = ""
    quociente = numero_decimal
    
    # Loop continua enquanto o quociente for maior que zero
    while quociente > 0:
        # O resto da divisão por 16 é o dígito hexadecimal atual
        resto = quociente % 16
        
        # Pega o caractere correspondente no mapa_hex
        digito_hex = mapa_hex[resto]
        
        # Adiciona o dígito ao INÍCIO da string (inversão da ordem)
        resultado_hex = digito_hex + resultado_hex
        
        # Atualiza o quociente para a próxima iteração
        quociente = quociente // 16
        
    return resultado_hex


def hexadecimal_para_decimal(numero_hex_str):
    """
    Função: Converte uma string hexadecimal (base 16) para um número inteiro decimal (base 10).
    Método: Expansão Posicional (Soma dos produtos do dígito pela potência de 16).
    """
    # Remove prefixos comuns (0x) e converte para maiúsculas para facilitar o processamento
    numero_hex_str = numero_hex_str.upper().replace('0X', '')
    
    # Mapeamento dos caracteres hexadecimais para seus valores decimais
    mapa_valores = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                    '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    
    # Validação dos caracteres
    if not all(c in mapa_valores for c in numero_hex_str):
        return "Erro: A string hexadecimal contém caracteres inválidos."

    resultado_decimal = 0
    posicao_expoente = 0 
    
    # Itera sobre a string hexadecimal de TRÁS PARA FRENTE (do dígito menos significativo)
    for digito_hex in reversed(numero_hex_str):
        
        # Obtém o valor decimal do dígito
        valor_decimal_digito = mapa_valores[digito_hex]
        
        # Adiciona o valor à soma total: dígito * (16 elevado à posição)
        resultado_decimal += valor_decimal_digito * (16 ** posicao_expoente)
        
        # Incrementa o expoente (o peso posicional)
        posicao_expoente += 1
        
    return resultado_decimal

# =================================================================
# FUNÇÃO PRINCIPAL E MENU
# =================================================================

def main_conversor():
    """
    Função principal que gerencia o menu de interação com o usuário.
    """
    print("---  Conversor de Bases Numéricas (Decimal, Binário e Hexadecimal) ---")
    
    while True:
        print("\nEscolha uma opção de conversão:")
        print("1: Decimal --> Binário")
        print("2: Binário --> Decimal")
        print("3: Decimal --> Hexadecimal")
        print("4: Hexadecimal --> Decimal")
        print("5: Sair")

        escolha = input("Digite o a função que deseja executar (1-5): ")

        if escolha == '5':
            print("Encerrando o programa. Até a próxima!")
            break

        try:
            if escolha == '1':
                valor = int(input("Digite o número DECIMAL que deseja converter: "))
                resultado = decimal_para_binario(valor)
                print(f"\n Resultado: {valor} (Decimal) --> {resultado} (Binário)")
                
            elif escolha == '2':
                valor = input("Digite a string BINÁRIA que deseja converter: ")
                resultado = binario_para_decimal(valor)
                print(f"\n Resultado: {valor} (Binário) --> {resultado} (Decimal)")

            elif escolha == '3':
                valor = int(input("Digite o número DECIMAL que deseja converter: "))
                resultado = decimal_para_hexadecimal(valor)
                print(f"\n Resultado: {valor} (Decimal) --> {resultado} (Hexadecimal)")

            elif escolha == '4':
                valor = input("Digite a string HEXADECIMAL que deseja converter: ")
                resultado = hexadecimal_para_decimal(valor)
                print(f"\n Resultado: {valor} (Hexadecimal) --> {resultado} (Decimal)")

            else:
                print("Opção inválida. Por favor, escolha um número de 1 a 5.")
        
        except ValueError:
            print("Erro de entrada. Certifique-se de digitar números inteiros para as conversões decimais.")
        
        print("\n" + "="*50)

# O ponto de entrada da aplicação
if __name__ == "__main__":
    main_conversor()
