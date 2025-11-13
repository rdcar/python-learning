def decimal_para_binario_manual(numero_decimal):
    """
    Converte um número inteiro decimal (base 10) para uma string binária (base 2)
    usando o método de divisões sucessivas.
    """
    if numero_decimal == 0:
        return "0"

    resultado_binario = ""  # Inicializamos como uma string vazia
    quociente = numero_decimal
    
    # O loop continua enquanto houver um quociente para dividir
    while quociente > 0:
        
        # Passo 1: Obter o resto (o bit menos significativo atual)
        resto = quociente % 2
        
        # Passo 2: Adicionar o resto ao INÍCIO da string binária
        # Aqui invertemos a ordem como o algoritmo exige
        resultado_binario = str(resto) + resultado_binario
        
        # Passo 3: Obter o novo quociente (a parte inteira da divisão)
        quociente = quociente // 2
        
    return resultado_binario

# Testes de Exemplo
num1 = 45
num2 = 13
num3 = 0

print(f"Decimal {num1} -> Binário: {decimal_para_binario_manual(num1)}")
print(f"Decimal {num2} -> Binário: {decimal_para_binario_manual(num2)}")
print(f"Decimal {num3} -> Binário: {decimal_para_binario_manual(num3)}")

def binario_para_decimal_manual(numero_binario_str):
    """
    Converte uma string binária (base 2) para um número inteiro decimal (base 10)
    usando o método da expansão posicional.
    """
    if not numero_binario_str:
        return 0
        
    # Inicializa o acumulador decimal e o expoente (peso)
    resultado_decimal = 0
    posicao_expoente = 0 
    
    # Itera sobre a string binária de TRÁS PARA FRENTE.
    # Ex: Para "101101", a iteração será: '1', '0', '1', '1', '0', '1'
    for bit_str in reversed(numero_binario_str):
        
        # O bit_str é uma string ('0' ou '1'). Converte para inteiro.
        bit_int = int(bit_str)
        
        # Passo 1: Calcula o peso (2 elevado à posição)
        peso_posicional = 2 ** posicao_expoente
        
        # Passo 2: Adiciona o valor à soma total: (bit * peso)
        # Se o bit for 0, o produto é 0. Se for 1, o produto é o peso.
        resultado_decimal += bit_int * peso_posicional
        
        # Passo 3: Incrementa o expoente para o próximo bit à esquerda
        posicao_expoente += 1
        
    return resultado_decimal

# Testes de Exemplo
bin1 = "101101" # Esperamos 45
bin2 = "1101"   # Esperamos 13
bin3 = "0"      # Esperamos 0

print(f"Binário {bin1} -> Decimal: {binario_para_decimal_manual(bin1)}")
print(f"Binário {bin2} -> Decimal: {binario_para_decimal_manual(bin2)}")
print(f"Binário {bin3} -> Decimal: {binario_para_decimal_manual(bin3)}")
