from random import randint


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
