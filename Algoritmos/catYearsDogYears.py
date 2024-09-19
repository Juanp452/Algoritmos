def calculate_pet_years_dict(human_years):
    # Calcula los años de gato y perro
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4
        dog_years = 15 + 9 + (human_years - 2) * 5

    # Regresa el resultado como diccionario
    return {
        "humanYears": human_years,
        "catYears": cat_years,
        "dogYears": dog_years
    }


# Prueba con 5 años humanos
print(calculate_pet_years_dict(8))
print(type(calculate_pet_years_dict(5)))

