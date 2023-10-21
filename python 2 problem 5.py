POUNDS_PER_TALENT = 20
LOTS_PER_POUND = 32
GRAMS_PER_LOT = 13.3
talents = float(input("Enter the mass in talents: "))
pounds = float(input("Enter the mass in pounds: "))
lots = float(input("Enter the mass in lots: "))
total_lots = (talents * POUNDS_PER_TALENT + pounds) * LOTS_PER_POUND + lots
kilograms = total_lots // 1000
grams = total_lots % 1000
print(f"The mass is equivalent to {kilograms} kilograms and {grams} grams.")