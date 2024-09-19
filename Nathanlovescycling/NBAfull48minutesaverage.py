def points_per_48(ppg, mpg):
    if mpg == 0:
        return 0
    return round(ppg * 48 / mpg, 1)

# Ejemplo de uso:
print(points_per_48(12, 24))  # Output: 24.0
print(points_per_48(20, 36))  # Output: 26.7
print(points_per_48(0, 0))    # Output: 0
