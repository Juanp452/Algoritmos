'''calcular edad minima y maxima
para estar con alguien'''

import math


def dating_range(age):
    if age > 14:
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor((age - 7) * 2)
    else:
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)

    return f"{min_age}-{max_age}"


# Ejemplo de uso:
print(dating_range(30))  # Output: "22-46"
print(dating_range(12))  # Output: "10-13"
