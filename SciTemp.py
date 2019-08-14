# Purpose of this function is to convert Fahrenheit to Celsius



def fahrenheit_to_celsius(F):
    c = (F-32)*(5/9)
    
    print("The temperature of " + str(F) + " degrees Fahrenheit in Celsius is " + str(c))
    return c

fahrenheit_to_celsius(77.9)



