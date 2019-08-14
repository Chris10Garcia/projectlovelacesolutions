import math

def wind_chill(T_a, v):
    T_wc = 0

    T_wc = 13.12 + 0.6215*T_a - 11.37*math.pow(v,0.16) + 0.3965 * T_a * math.pow(v,0.16)

    print(str(T_wc))

    return T_wc


wind_chill(-10, 10)