square_meters = float(
    input("Insira a quantidade a ser pintada, em metros quadrados (m^2): "))

can_capacity = 3 * 18
paint_cans = int(1 +
                 square_meters // (can_capacity) if square_meters % (
                     can_capacity) > 0 else square_meters // (can_capacity))

print(f"A quantidade de latas necessárias é: {paint_cans}")
