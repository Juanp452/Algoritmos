"""programa que calcula los angulos de un triangulo
restantes para los 180 """
def find_third_angle(angle1, angle2):
    return 180 - (angle1 + angle2)

# Ejemplo de uso:
print(find_third_angle(90, 10))
