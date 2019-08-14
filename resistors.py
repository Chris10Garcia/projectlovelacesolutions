digits = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

multiplier = {
    'pink': 0.001,
    'silver': 0.01,
    'gold': 0.1,
    'black': 1,
    'brown': 10,
    'red': 100,
    'orange': 10 ** 3,
    'yellow': 10 ** 4,
    'green': 10 ** 5,
    'blue': 10 ** 6,
    'violet': 10 ** 7,
    'grey': 10 ** 8,
    'white': 10 ** 9
}

tolerance = {
    'none': 0.2,
    'silver': 0.1,
    'gold': 0.05,
    'brown': 0.01,
    'red': 0.02,
    'green': 0.005,
    'blue': 0.0025,
    'violet': 0.001,
    'grey': 0.0005
}


def resistance(band_colors):
    n_bands = len(band_colors)
    answers = []

    nom_R = 0
    min_R = 0
    max_R = 0
        
    # function for one band resistor
    def one_band(band_colors):
        
        nom_R = digits[band_colors[0]]
        min_R = nom_R * (1 - 0.2)
        max_R = nom_R * (1 + 0.2)

        return nom_R, min_R, max_R

    #function for 4 band resistor
    def four_band(band_colors):

        nom_R = nominal_R(band_colors)

        min_R = minimum_R(band_colors)

        max_R = maximum_R(band_colors)


        return nom_R, min_R, max_R

    #function for 5 band resistor
    def five_band(band_colors):

        nom_R = nominal_R(band_colors)

        min_R = minimum_R(band_colors)

        max_R = maximum_R(band_colors)

        return nom_R, min_R, max_R   

    #function to determine nominal resistance 
    def nominal_R(band_colors):
        nom = []
        for n in range(0,n_bands-2):    # from 0 to band# -2, so 0 to 2 or 0 to 3 where n is position and the last number is omitted
            nom.append(digits[band_colors[n]])

        nom = int(''.join(map(str,nom)))

        nom = nom * multiplier[band_colors[n_bands-2]]

        return nom

    def minimum_R(band_colors):
        nom = nominal_R(band_colors)

        tol = tolerance[band_colors[n_bands-1]]

        tol_min = nom * (1 - tol)

        return tol_min

    def maximum_R(band_colors):

        nom = nominal_R(band_colors)

        tol = tolerance[band_colors[n_bands-1]]

        tol_max = nom * (1 + tol)

        return tol_max
    

    #dictionary of functions based on the number of bands


    band_chart = {
        1 : one_band,
        4 : four_band,
        5 : five_band,
    }

    answers = band_chart[n_bands]   

    answers = answers(band_colors)

    nom_R = answers[0]
    min_R = answers[1]
    max_R = answers[2]
    
    return nom_R, min_R, max_R


print(resistance(["red", "orange", "violet", "black", "brown"]))