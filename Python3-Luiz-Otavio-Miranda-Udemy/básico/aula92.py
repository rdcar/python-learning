"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista = []

while True:
    print("Selecione uma opção")
    option = input("[I]nserir, [A]pagar, [L]istar: ")

    if option.lower() == "i":
        os.system("clear")
        item = input("Digite o item: ")
        lista.append(item)

    elif option.lower() == "a":
        os.system("clear")
        print("Apagando item...")

        try:
            item = int(input("Escolha qual item deseja apagar: "))
            del lista[item]
        except IndexError: # indice fora do range
            print(f"Este item ({item}) não existe. Escolha um item presente na lista.")
        except ValueError: # indice diferente de número
            print(f"Digite um número inteiro. '{item}' NÃO é um número inteiro.")
        except: # Qualquer outro erro
            print("Erro desconhecido.")

    elif option.lower() == "l":
        os.system("clear")
        print("Listando itens...")
        
        if len(lista) == 0:
            print("Lista vazia!")

        for i, item in enumerate(lista): #enumerete gera tupla de valores da lista
            print(f"Item {i}; Nome: {item}") # capturando indice e valor de cada tupla

    else:
        print("Opção inválida.")
        continue