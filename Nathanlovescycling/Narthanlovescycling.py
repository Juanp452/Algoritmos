'''programa donde calcula cuantos litros
agua toma '''
import math
def litres(time):
    return math.floor(time * 0.5)

# Ejemplo de uso:
print(litres(3))     # Output: 1
print(litres(6.7))   # Output: 3
