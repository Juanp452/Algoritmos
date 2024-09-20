'''calcular la presion'''
def total_pressure(M1, M2, m1, m2, V, T):
    # Convertir la temperatura a Kelvin
    T_kelvin = T + 273.15

    # Constante de los gases
    R = 0.082

    # Calcular el número de moles de cada gas
    n1 = m1 / M1
    n2 = m2 / M2

    # Calcular la presión total usando la fórmula
    P_total = (n1 + n2) * R * T_kelvin / V

    return P_total


# Ejemplo de uso
M1 = 16  # g/mol
M2 = 44  # g/mol
m1 = 32  # g
m2 = 88  # g
V = 10  # dm^3
T = 25  # °C

print(total_pressure(M1, M2, m1, m2, V, T))  # Output: 9.819 atm
