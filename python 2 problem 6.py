import random
code_3_digit = [random.randint(0, 9) for _ in range(3)]
code_4_digit = [random.randint(1, 6) for _ in range(4)]
print("Random 3-digit code: ", end="")
for digit in code_3_digit:
    print(digit, end="")
print()
print("Random 4-digit code: ", end="")
for digit in code_4_digit:
    print(digit, end="")
print()
