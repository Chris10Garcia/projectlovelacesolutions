import math

# from math import sin, cos, sqrt, asinh.radians 

def haversine_distance(a, b, c, d):
    R = 6372.1
    hav_dist = 0

    #a, b = lat_1, long_1
    #c, d = lat_2, long_2

    lat_1 = a
    lon_1 = b

    lat_2 = c
    lon_2 = d

    

    sinPart = math.sin(math.radians((lat_2-lat_1)/2))**2

    cosSinPart = math.cos(math.radians(lat_1))*math.cos(math.radians(lat_2))*(math.sin(math.radians(lon_2-lon_1)/2))**2

    sqrtPart = math.sqrt(sinPart + cosSinPart)


    hav_dist = 2*R*math.asin(sqrtPart)

    return hav_dist


print(haversine_distance(46.283,86.667,-48.877,-123.393))

