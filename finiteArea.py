

def area_of_rectangles(heights, width):

    area = 0

    for h in heights:
        area+= h * width
    
    return area

print(area_of_rectangles([0, 1, 2, 3, 4, 5], 1.5))