from collections import Counter


def main():
    with open("./Python/Poetry/Arquivos/Richard_Dawkins_O_Gene_Egoista.txt") as arquivo:
        texto = arquivo.read().lower()
    letras = [character for character in texto if character.isalpha()]
    frequencia_letras = Counter(letras)

    print(frequencia_letras.most_common())


if __name__ == "__main__":
    main()
