from random import shuffle, randint


def sorteia_palavra(tema):
    cidades = {
        "f": [
            "lages",
            "criciúma",
            "urubici",
            "macaé",
            "natal",
            "cotia",
            "majé",
            "itú",
            "sinóp",
        ],
        "m": [
            "calcaia",
            "taubaté",
            "moçoró",
            "sumaré",
            "jaraguá",
            "brusque",
            "palhoça",
            "curitiba",
        ],
        "d": [
            "florianópolis",
            "joinville",
            "ituporanga",
            "ressaquinha",
            "petrópolis",
            "uberlândia",
            "ananindeua",
            "carapicuíba",
            "itaquaquecetuba",
            "parnamirim",
        ],
    }

    objetos = {
        "f": [
            "garfo",
            "maiô",
            "óculos",
            "jeans",
            "copo",
            "harpa",
            "funil",
            "pote",
            "faca",
        ],
        "m": [
            "picareta",
            "bigorna",
            "pendulo",
            "manomêtro",
            "zabumba",
            "notebook",
            "pinico",
            "cadeira",
        ],
        "d": [
            "estetoscopio",
            "zarabatana",
            "quinticlave",
            "sombrinha",
            "nebulizador",
            "namômetro",
            "lantejoula",
            "velocípede",
        ],
    }

    paises = {
        "f": [
            "suíça",
            "itália",
            "chipre",
            "suécia",
            "rússia",
            "china",
            "chile",
            "sudão",
            "irã",
        ],
        "m": [
            "monaco",
            "austria",
            "austrália",
            "equador",
            "noruega",
            "albânia",
            "romênia",
            "georgia",
            "turquia",
            "iraque",
        ],
        "d": [
            "eslovênia",
            "somália",
            "guatemala",
            "nicarágua",
            "filipinas",
            "mogólia",
            "cingapura",
            "nigéria",
            "camarões",
            "uzbequistão",
            "azerbaijão",
        ],
    }

    verbos = {
        "f": [
            "falar",
            "correr",
            "pular",
            "andar",
            "sonhar",
            "piscar",
            "nadar",
            "sentar",
        ],
        "m": [
            "hibernar",
            "trafegar",
            "manipular",
            "evacuar",
            "capturar",
            "caminhar",
            "desfilar",
            "reclamar",
        ],
        "d": [
            "desfibrilar",
            "tergivisar",
            "perambular",
            "interpelar",
            "radicalizar",
            "auscutar",
            "impermebealizar",
            "diagnosticar",
        ],
    }

    temas = {1: cidades, 2: objetos, 3: paises, 4: verbos}

    dificuldades = ["fácil", "médio", "difícil"]
    dificuldade_sorteada = dificuldades[randint(0, len(dificuldades))]

    lista_palavras = temas[tema][dificuldade_sorteada[0]]

    palavra_sorteada = lista_palavras[randint(0, len(lista_palavras) - 1)]
    return (palavra_sorteada, dificuldade_sorteada)


def embaralhada_palavra(palavra, palavra_anterior=""):
    palavra_anterior = palavra
    palavra = list(palavra)
    shuffle(palavra)
    palavra = "".join(palavra)

    if palavra == palavra_anterior:
        return embaralhada_palavra(palavra, palavra_anterior)
    return palavra


def frases_motivacional():
    frases_motivacionais = [
        "Vamos lá, você consegue!",
        "Não se desespere, você consegue!",
        "Positividade!",
        "Quase! Vamos lá, tente novamente!",
        "Não desista!",
    ]

    frase_sorteada = frases_motivacionais[randint(0, len(frases_motivacionais) - 1)]
    return frase_sorteada


def main(tema):
    tentativa = 0
    palavra_sorteada, dificuldade = sorteia_palavra(tema)
    palavra_embaralhada = embaralhada_palavra(palavra_sorteada)

    while True:
        frase_sorteada = frases_motivacional()

        print("A palavra embaralhada é", palavra_embaralhada)
        print("A dificuldade é:", dificuldade)
        print("Você ganha se acerta em, no máximo, 5 tentativas")

        palpite = input("Qual é a palavra? \n> ")
        tentativa += 1

        if palpite.lower() == palavra_sorteada.lower():

            print(
                f"Você ganhou! \nForam {tentativa} {'tentativas' if tentativa > 1 else 'tentativa'}"
            ) if tentativa <= 5 else print(
                f"Você perdeu :( \nForam {tentativa} {'tentativas' if tentativa > 1 else 'tentativa'}"
            )
            break
        print(f"\n{frase_sorteada}")


if __name__ == "__main__":
    while True:
        tema = int(
            input(
                """
    Escolha um dos temas a seguir (digite o número do tema):
        1 = cidade
        2 = objetos
        3 = paises
        4 = verbos
        
        >> """
            )
        )
        if tema > 4 or tema < 1:
            print("--------- Escolha um tema válido! ---------")
        else:
            break

    main(tema)
