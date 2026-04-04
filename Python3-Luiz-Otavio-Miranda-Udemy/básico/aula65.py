"""
Iterando strings com while
"""
nome = 'Luiz Otávio'  # Iteráveis

indice = 0
novo_nome = ""
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f"{letra}*" #Reconstruindo nome em novo_nome só que letra a letra (iteração)
    indice += 1
print(novo_nome)