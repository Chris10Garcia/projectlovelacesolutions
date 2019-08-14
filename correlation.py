import math



def correlation_coefficient(x, y):
    r = 0

    def average(z):
        z_ave = []
        n = len(z)

        # for i, j in enumerate(z):
        for j in z:
            z_ave.append(j)
        
        z_ave = math.fsum(z_ave)/n

        return z_ave

    def std_dev(z):
        sigma = []
        n = len(z)

        for j in z:
            sigma.append((j - average(z)) ** 2)

        sigma = math.sqrt(math.fsum(sigma)/n)

        return sigma
    
    # testing testing
    def cov(z0,z1):
        z = list(zip(z0,z1))
        n = len(z)
        c = []

        for i in range(0,n):
            c.append((z[i][0] - average(z0)) * (z[i][1] - average(z1)))

        c = math.fsum(c)/n

        return c


    r = cov(x,y)/(std_dev(x) * std_dev(y))

    return r             


x = [  5427,   5688,   6198,   6462,   6635,   7336,   7248,   7491,   8161,   8578,   9000]
y = [18.079, 18.594, 19.753, 20.734, 20.831, 23.029, 23.597, 23.584, 22.525, 27.731, 29.449]

answer = correlation_coefficient(x,y)

print (answer)