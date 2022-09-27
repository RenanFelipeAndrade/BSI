import json
from pathlib import Path
from random import randint


def sorteia_palavra(tema, dificuldade):
    BASE_DIR = Path(__file__).resolve().parent
    with open(f"{BASE_DIR}/palavras.json") as arquivo:
        json_data = json.load(arquivo)
    cidades = json_data["cidades"]
    objetos = json_data["objetos"]
    paises = json_data["paises"]
    verbos = json_data["verbos"]

    temas = {1: cidades, 2: objetos, 3: paises, 4: verbos}

    dificuldades = ["fácil", "médio", "difícil"]
    dificuldade_sorteada = dificuldades[dificuldade-1]

    lista_palavras = temas[tema][dificuldade_sorteada[0]]

    palavra_sorteada = lista_palavras[randint(0, len(lista_palavras) - 1)]
    return (palavra_sorteada, dificuldade_sorteada)
