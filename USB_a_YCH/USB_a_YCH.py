def usd_to_cny(usd):
    conversion_rate = 6.75  # Puedes ajustar esta tasa de conversión
    cny = usd * conversion_rate
    return f"{cny:.2f} Chinese Yuan"

# Ejemplo de uso
usd_amount = 100
print(usd_to_cny(usd_amount))  # "675.00 Chinese Yuan"
print(type(usd_amount))
