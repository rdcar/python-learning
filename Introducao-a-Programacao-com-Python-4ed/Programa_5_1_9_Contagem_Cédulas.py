# Modificação para aceitar cédulas de R$100 e moedas.
valor_reais = float(input("Digite o valor a pagar:"))

# Converte o valor total para centavos, multiplicando por 100
apagar = int(valor_reais * 100) 
cédulas = 0
atual = 10000 # R$100 em centavos

while True:
    if atual <= apagar:
        apagar -= atual
        cédulas += 1
    else:
        # Imprime o valor da cédula/moeda dividindo por 100.0 para formatar em Reais
        print(f"{cédulas} cédula(s)/moeda(s) de R${atual / 100.0:.2f}")

        if apagar == 0:
            break
        # Lembre-se: as denominações abaixo estão em centavos
        elif atual == 10000: # R$100
            atual = 5000     # R$50
        elif atual == 5000:
            atual = 2000
        elif atual == 2000:
            atual = 1000
        elif atual == 1000:
            atual = 500
        elif atual == 500:
            atual = 100      # R$1
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 2
        elif atual == 2:
            atual = 1
        cédulas = 0
    
    
        
