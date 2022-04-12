number = int(input("Insira um nuúmero menor que 1000: "))

hundreds = number // 100
number -= hundreds * 100

dozens = number // 10
number -= dozens * 10

unities = number

print(
    f"A quantidade de dezenas, centenas e unidades respectivamente é: {hundreds}, {dozens} e {unities}")
