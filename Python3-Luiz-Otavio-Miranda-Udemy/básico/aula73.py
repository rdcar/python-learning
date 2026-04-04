frase = "O Python é uma linguagem de programação" \
"muito interessante. Com ela, você pode fazer várias coisas legais, apesar de não ser" \
"tão performática quanto Rust ou C. Aprenda Python!"

i = 0
maior_qtd_geral = 0
maior_qtd_atual = 0
letra_mais_vezes = ""

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == " ": # Ignora os espaços
        i += 1
        continue

    maior_qtd_atual = frase.count(letra_atual)

    if maior_qtd_geral < maior_qtd_atual:
        maior_qtd_geral = maior_qtd_atual
        letra_mais_vezes = letra_atual
    i += 1

print("A letra que apareceu mais fezes foi" \
f"a letra [{letra_mais_vezes}] tendo um total de " \
f"{maior_qtd_geral} aparições.")
