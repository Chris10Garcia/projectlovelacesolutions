from statistics import mean, pstdev
from math import sqrt


def temperature_statistics(T):
        #new_T = list(map(float, T))
        T_ave = mean(T)
        T_std = pstdev(T)
    # Your code goes here!
        return T_ave, T_std

for n in temperature_statistics([4.4, 4.2, 7.0, 12.9, 18.5, 23.5, 26.4, 26.3, 22.5, 16.6, 11.2, 7.3]):
        print(n)

