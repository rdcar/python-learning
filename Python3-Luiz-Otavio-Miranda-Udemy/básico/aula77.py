"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = "perfume"
letras_acertadas = ""
tentativas = 0

while True:
    letra_digitada = input("Digite uma letra: ")
    if len(letra_digitada) > 1:
        print("Digite apenas uma letra!")
        continue
    
    tentativas += 1
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ""

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    print("Número de tentativas: ", tentativas)

    if palavra_formada == palavra_secreta:
        os.system("clear") #não funciona no enviroment conda
        print(5*"*" + "Parabéns, você adivinhou!" + 5*"*")
        print("A palavra secreta é: ", palavra_secreta)
        print("Total de tentativas: ", tentativas)
        tentativas = 0
        letras_acertadas = ""

    print("Palavra formatada: ",palavra_formada)


