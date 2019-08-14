
def almost_pi(N):
    pieSum = 0
    

    for i in range (0,N):
        pie = 4 * (((-1) ** i)/(2*i + 1))
        pieSum = pie + pieSum

    return pieSum 


print (almost_pi(25))