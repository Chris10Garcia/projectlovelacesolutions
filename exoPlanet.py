from math import sqrt



def habitable_exoplanet(lum, dist):

    r_inner = sqrt(lum/1.1)
    r_outer = sqrt(lum/0.54)

    if r_inner < dist < r_outer:
        statement = "just right"

    else:
        if r_inner > dist:
            statement = "too hot"
        else:
            statement = "too cold"     

    return statement

print (habitable_exoplanet(1.5,2.5))