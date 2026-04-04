nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if " " in nome:
        print(f"Seu nome '{nome}' contém espaço")
    else:
        print(f"Seu nome '{nome}' não contém espaços")
    print(f"A primeira letra do seu nome é '{nome[0]}'")
    print(f"A última letra do seu nome é '{nome[-1]}'")
    print(f"Seu nome '{nome}' tem {len(nome)} letras, incluindo espaços.")
else:
    print("Desculpe, você não preencheu todos os campos!")