# Lista de exercícios - Condições
from math import sqrt


def maior3(a, b, c):
    """Recebe três valores, e retorna o maior dos três.

    Argumentos:
        a (float): primeiro valor;
        b (float): segundo valor;
        c (float): terceiro valor;

    Retorna:
        float: o maior entre os três valores.
    """
    numeros = [a, b, c]
    numeros.sort()
    return numeros[2]


def menor3(a, b, c):
    """Recebe três valores, e retorna o menor dos três.

    Argumentos:
        a (float): primeiro valor;
        b (float): segundo valor;
        c (float): terceiro valor;

    Retorna:
        float: o menor entre os três valores.
    """
    numeros = [a, b, c]
    numeros.sort()
    # max(numeros) é uma alternativa
    return numeros[0]


def testa_lados(a, b, c):
    """Receba os três lados de um triângulo. Informe se os valores
    podem ser um triângulo. Indique, caso os lados formem um triângulo,
    se o mesmo é: equilátero, isósceles ou escaleno.

    Argumentos:
        a (float): primeiro lado;
        b (float): segundo lado;
        c (float): terceiro lado;

    Retorna:
        string: um texto indicando o resultado,
                conforme aparece nos testes no final desse arquivo.
    """
    # se a soma de 2 lados não é igual ou maior que o lado restante
    if not (a + b >= c and b + c >= a and a + c >= b):
        return "Não forma um triângulo"

    tipo_triangulo = ""
    # se os 3 lados são diferentes
    if a != b and a != c and c != b:
        tipo_triangulo = "Triângulo escaleno"
    # se os 2 lados são diferentes
    elif (
        (a == b and a != c and c != b)
        or (c == b and a != b and a != c)
        or (c != b and a != b and a == c)
    ):
        tipo_triangulo = "Triângulo isósceles"
    else:
        tipo_triangulo = "Triângulo equilátero"
    return tipo_triangulo


def ano_bissexto(ano):
    """Determine se um ano é bissexto ou não.

    Argumento:
        ano (int): um ano, no formato de 4 dígitos.

    Retorna:
        bool: True ou False (verdadeiro ou falso), caso a ano seja ou não bissexto.

    """
    # se o ano é divisível por 400 ou por 4 e não por 100
    return ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)


def maior_dia_do_mes(mes, ano):
    """Retorna o último dia do mês para um determinado ano e mês.
        Os valores possíveis são: 28, 29, 30 ou 31.
        Devem ser considerados os anos bissextos.
        Uma função separada para determinar se um ano é bissexto
        poderia ser utilizada.

    Argumentos:
        mes (int): um mês no formato de dois dígitos;
        ano (int): um ano, no fomato de 4 dígitos;

    Retorna:
        int: um inteiro indicando o último dia válido para aquele mês e ano.
    """
    meses = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    if ano_bissexto(ano) and mes == 2:
        return meses[2] + 1
    return meses[mes]


def data_valida(data):
    """Recebe uma string no formato dd/mm/aaaa e informa
        um valor lógico indicando se a data é válida ou não.
        Verifica se ano é bissexto e outros detalhes.
        Confira os testes no final do arquivo para mais detalhes.

    Argumentos:
        data (string): data no formato "dd/mm/aaaa".

    Retorna:
        bool: True ou False, indicando se a datá é válida ou não.
    """
    meses = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    data_separada = data.split("/")
    dia = int(data_separada[0])
    mes = int(data_separada[1])
    ano = int(data_separada[2])

    if not mes in meses or ano == 0:
        return False
    elif mes == 2 and ano_bissexto(ano):
        return dia <= meses[mes] + 1 and dia > 0
    elif dia > meses[mes] or dia < 1:
        return False
    else:
        return True


def baskara(a, b, c):
    """Calcule as raízes de uma equação do segundo grau, na forma
    ax2 + bx + c. A função recebe a, b e c e faz as consistências,
    informando ao usuário nas seguintes situações:
    - Se o usuário informar o valor de A igual a zero é uma equaçao do 1o grau.
    - Se o delta calculado for negativo, a equação não possui raizes reais.
    Devolva uma tupla vazia.
    - Se o delta calculado for igual a zero a equação possui apenas uma
    raiz real. Devolva uma tupla com um único valor.
    - Se o delta for positivo, a equação possui duas raiz reais.
    Devolva uma tupla com dois elementos.

    Argumentos:
        a (float): valor a da equação;
        b (float): valor b da equação;
        c (float): valor c da equação;

    Retorna:
        tupla de floats: uma tupla, contando os valores das raízes, sendo
        uma raiz, duas raízes ou uma tupla vazia caso não existam raízes.
    """
    if a == 0:
        return (-c / b,)

    delta = b**2 - 4 * a * c
    if delta < 0:
        return ()
    elif delta == 0:
        return ((-b + sqrt(delta)) / 2,)
    else:
        return ((-b + sqrt(delta)) / 2, (-b - sqrt(delta)) / 2)


def acrescimo_nota_bb(nota_sozinho, nota_com_ajuda):
    """Recebe a nota do litle brother antes de receber ajuda, e a nota
    depois que o big brother ajudou, e retorna o acrecimo que o big
     brother recebera em sua nota pela ajuda.
     O acréscimo é de 1/4 da diferença das notas, se for positivo.

    Argumentos:
        nota_sozinho (float): a nota que o aluno tirou sem ajuda.
        nota_com_ajuda (float): a nota que o aluno tirou após ter sido ajudado.

    Retorna:
        float: o acréscimo na nota obtido pelo aluno que ajudou seu colega.
    """
    if nota_com_ajuda < 0 or nota_com_ajuda <= nota_sozinho:
        return 0.0
    else:
        return round((nota_com_ajuda - nota_sozinho) * (0.25), 1)


# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = "\033[31m%s" % ("Falhou")
    else:
        prefixo = "\033[32m%s" % ("Passou")
        acertos += 1
    print(
        "%s Esperado: %s \tObtido: %s\033[1;m" % (prefixo, repr(esperado), repr(obtido))
    )


def main():

    print("Maior de 3 valores:")
    test(maior3(a=1, b=2, c=3), 3)
    test(maior3(a=1.01, b=1.1, c=1.02), 1.1)
    test(maior3(a=0, b=-1, c=-2), 0)
    test(maior3(a=-100, b=0, c=100), 100)

    print("Menor de 3 valores:")
    test(menor3(a=1, b=2, c=3), 1)
    test(menor3(1.01, 1.02, 1.1), 1.01)
    test(menor3(0, -1, -2), -2)
    test(menor3(-100, 0, 100), -100)

    print("Triângulos:")
    test(testa_lados(7, 1, 2), "Não forma um triângulo")
    test(testa_lados(7, 2, 1), "Não forma um triângulo")
    test(testa_lados(1, 7, 2), "Não forma um triângulo")
    test(testa_lados(1, 2, 7), "Não forma um triângulo")
    test(testa_lados(2, 1, 7), "Não forma um triângulo")
    test(testa_lados(2, 7, 1), "Não forma um triângulo")
    test(testa_lados(2, 2, 2), "Triângulo equilátero")
    test(testa_lados(3, 3, 3), "Triângulo equilátero")
    test(testa_lados(2, 3, 4), "Triângulo escaleno")
    test(testa_lados(2, 4, 3), "Triângulo escaleno")
    test(testa_lados(3, 4, 2), "Triângulo escaleno")
    test(testa_lados(3, 2, 4), "Triângulo escaleno")
    test(testa_lados(2, 3, 3), "Triângulo isósceles")
    test(testa_lados(3, 2, 2), "Triângulo isósceles")
    test(testa_lados(3, 3, 2), "Triângulo isósceles")
    test(testa_lados(3, 2, 3), "Triângulo isósceles")

    print("Ano bissexto:")
    test(ano_bissexto(ano=1000), False)
    test(ano_bissexto(ano=1200), True)
    test(ano_bissexto(ano=1004), True)
    test(ano_bissexto(ano=1040), True)
    test(ano_bissexto(ano=2012), True)
    test(ano_bissexto(ano=2014), False)

    print("Maior dia do mês:")
    test(maior_dia_do_mes(mes=1, ano=2014), 31)
    test(maior_dia_do_mes(mes=3, ano=2014), 31)
    test(maior_dia_do_mes(mes=4, ano=2014), 30)
    test(maior_dia_do_mes(mes=5, ano=2014), 31)
    test(maior_dia_do_mes(mes=6, ano=2014), 30)
    test(maior_dia_do_mes(mes=7, ano=2014), 31)
    test(maior_dia_do_mes(mes=9, ano=2014), 30)
    test(maior_dia_do_mes(mes=10, ano=2014), 31)
    test(maior_dia_do_mes(mes=11, ano=2014), 30)
    test(maior_dia_do_mes(mes=12, ano=2014), 31)
    test(maior_dia_do_mes(mes=2, ano=2014), 28)
    test(maior_dia_do_mes(mes=2, ano=2016), 29)

    print("Valida datas:")
    test(data_valida(data="01/01/2014"), True)
    test(data_valida(data="31/01/2014"), True)
    test(data_valida(data="00/00/0000"), False)
    test(data_valida(data="30/04/2014"), True)
    test(data_valida(data="31/04/2014"), False)
    test(data_valida(data="30/09/2014"), True)
    test(data_valida(data="31/09/2014"), False)
    test(data_valida(data="30/06/2014"), True)
    test(data_valida(data="31/06/2014"), False)
    test(data_valida(data="30/11/2014"), True)
    test(data_valida(data="31/11/2014"), False)
    test(data_valida(data="32/01/2014"), False)
    test(data_valida(data="01/01/0000"), False)
    test(data_valida(data="01/13/2014"), False)
    test(data_valida(data="01/00/2014"), False)
    test(data_valida(data="29/02/2014"), False)
    test(data_valida(data="29/02/2016"), True)

    print("Báskara:")
    test(baskara(1, 4, 4), (-2.0,))
    test(baskara(1, 5, 4), (-1.0, -4.0))
    test(baskara(0, 4, 2), (-0.5,))
    test(baskara(4, 4, 4), ())

    print("Acréscimo BB:")
    test(acrescimo_nota_bb(1, 10), 2.2)
    test(acrescimo_nota_bb(7, 6), 0.0)
    test(acrescimo_nota_bb(0, 10), 2.5)
    test(acrescimo_nota_bb(6.9, 7.1), 0.0)


if __name__ == "__main__":
    main()
    print(
        "\n%d Testes, %d Ok, %d Falhas: Nota %.1f"
        % (total, acertos, total - acertos, float(acertos * 10) / total)
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
