'''programa que calcula el pago de
la oferta de los mangos
'''
def mangoes_cost(quantity, price_per_mango):
    # Calcular cuántos mangos se pagan de acuerdo a la oferta
    groups_of_three = quantity // 3
    remaining_mangoes = quantity % 3
    total_paid_mangoes = (groups_of_three * 2) + remaining_mangoes
    return total_paid_mangoes * price_per_mango

# Ejemplo de uso
print(mangoes_cost(9, 5))   # Output: 30
print(mangoes_cost(5, 3))   # Output: 12
