speed = float(input("Insira a velocidade (km/h): "))
distance = float(input("Insira a distância a ser percorrida (km): "))

hours_spent = round(distance / speed, 2)


print(
    f"O tempo gasto para percorrer {distance} km a {speed} km/h é: {hours_spent} horas"
)
