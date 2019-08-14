
def babylonian_sqrt(n):
    if n > 0:
        x = n/2
        counter = 15

        for i in range (1,counter):
            x = 0.5 * ( x + n/x)
    elif n == 0:
        x = 0
    else:
        x = "undefined"
    return x

print(babylonian_sqrt(0))