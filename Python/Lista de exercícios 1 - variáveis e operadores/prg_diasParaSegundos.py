days_in_seconds = int(input("Insira a quantidade de dias: ")) * 24 * 60 * 60
hours_in_seconds = int(input("Insira a quantidade de horas: ")) * 60 * 60
minutes_in_seconds = int(input("Insira a quantidade de minutos: ")) * 60
seconds = int(input("Insira a quantidade de segundos: "))

total_amount = days_in_seconds + hours_in_seconds + minutes_in_seconds + seconds

print(f"A quantidade de segundos é: {total_amount}")
