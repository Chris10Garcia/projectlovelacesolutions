from math import exp, pow


def rocket_fuel(v_Esc):

    mass_Rocket = 250000
    v_E = 2550

    mass_Fuel = mass_Rocket * (exp(v_Esc/v_E) - 1)

    return mass_Fuel


print(rocket_fuel(500.0))