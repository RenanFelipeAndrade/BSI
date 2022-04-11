renting_days = int(input("Insira a quantia de dias alugado: "))
kilometers = float(input("Insira a distância trafegada (km): "))

total_cost = round(renting_days * 60 + kilometers * 0.15, 2)
print(f"O total a ser pago é: {total_cost}")
