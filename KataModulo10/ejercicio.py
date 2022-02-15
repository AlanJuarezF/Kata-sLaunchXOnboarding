def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    return f"El total de agua que queda después de {days_left} días es: {total_water_left} litros"
print(water_left(5, 100, 2))

def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(
            f"No hay suficiente agua para los {astronauts} astronautas después de {days_left} días!")
    return f"El total de agua que queda después de {days_left} días es: {total_water_left} litros"

water_left(5, 100, 2)

try:
    water_left(5, 100, 2)
except RuntimeError as err:
    print(err)

water_left("3", "200", None)

def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # Si el argumento es un int, la siguiente operación funcionará
            argument / 10
        except TypeError:
            # Sólo se producirá un TypError si no es el tipo correcto
            # Lanzar la misma excepción pero con un mejor mensaje de error
            raise TypeError(
                f"Todos los argumentos deben ser de tipo int, pero se reciben: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(
            f"No hay suficiente agua para los {astronauts} astronautas después de {days_left} días!")
    return f"El total de agua que queda después de {days_left} días es: {total_water_left} litros"
water_left("3", "200", None)