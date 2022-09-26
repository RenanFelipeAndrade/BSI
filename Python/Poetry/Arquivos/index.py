from collections import Counter
import os
from pathlib import Path
from utils import calcular_frequencia_letras, mostra_grafico


def main():
    BASE_DIR = Path(__file__).resolve().parent
    arquivos = os.listdir(BASE_DIR)
    arquivos_txt = [arquivo for arquivo in arquivos if arquivo.endswith(".txt")]

    livro = {}
    linguas = ["portugues", "espanhol", "frances"]  # magic array
    for index, arquivo in enumerate(arquivos_txt):
        with open(f"{BASE_DIR}/{arquivo}") as livro_arquivo:
            livro[linguas[index]] = livro_arquivo.read().lower()

    frequencia_letras = {}
    for lingua in livro:
        lista_letras = calcular_frequencia_letras(livro[lingua])
        frequencia_letras[lingua] = Counter(lista_letras)

    mostra_grafico(frequencia_letras, linguas)


if __name__ == "__main__":
    main()
