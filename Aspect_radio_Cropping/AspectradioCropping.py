import math

def convert_to_16_9_resolution(x, y):
    # Calcula el nuevo ancho para la relación de aspecto 16:9
    new_x = math.ceil((16 / 9) * y)
    return new_x, y

# Ejemplo de uso
x_res, y_res = 1024, 901
new_x, new_y = convert_to_16_9_resolution(x_res, y_res)
print(f"Nuevo tamaño: {new_x} × {new_y}")
