cigarettes_per_day = int(
    input("Insira a quantidade de cigarros fumados por dia: "))
years_smoking = int(input("Insira a quantidade de anos fumando: "))

lost_days = round(((cigarettes_per_day * 10) / 60 / 24)
                  * years_smoking * 365, 2)
print(f"A quantidade, em dias, de vida perdido é: {lost_days}")
