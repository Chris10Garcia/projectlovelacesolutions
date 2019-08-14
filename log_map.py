

def logistic_map(r):

    x = 0.50
    chaos_map =[x]

    for i in range (1,51):
        x = r * x * (1-x)

        chaos_map.append(x)
    
#    logmap = list(chaos_map)
#    return logmap
    return chaos_map

print(logistic_map(3.88))

