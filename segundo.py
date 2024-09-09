frase = input("Digite uma frase ou palavra: ")

frase = frase.lower()

cont = 0
for i in range(len(frase)):
    if "a" == frase[i]:
        cont += 1

if cont == 1:
    print(f"A letra 'a' aparece {cont} vez na palavra/frase.")
elif cont == 0:
    print(f"A letra 'a' aparece {cont} vezes na palavra/frase.")
else:
    print(f"A letra 'a' aparece {cont} vezes na palavra/frase.")