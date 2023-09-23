def without(dict,keys):
    for key in keys:
        del dict[key]
    return dict

class Location:
    def __init__(self):
        pass

    Temperatures = {'Very Cold': [], 'Cold': [], 'Cool': [], 'Warm': [], 'Hot': [], 'Very Hot': []}
    Sky_Types = {'Snowy': [], 'Rainy': [], 'Cloudy': [], 'Sunny': [], 'Stormy': []}
    Populations = {'Deserted': [], 'Abandoned': [], 'Inhabited': [], 'Heavily inhabited': [], 'Overpopulated': []}
    Precipitations = {'Never': [], 'Rarely': [], 'Sometimes': [], 'Often': [], 'Almost Always': []}
    Walkabilities = {'Intraversable': [], 'Difficult': [], 'Walkable': [], 'Easily Traversed': [], "Wide open": []}
    Humidities = {'Dry': [], 'Average': [], 'Humid': []}
    Wind_Levels = {'Still': [], 'Breezy': [], 'Windy': [], 'Very Widy': [], 'Hurricane': []}
    Nature = {'Wilderness': [], "Heavy Vegetation": [], 'Light Vegetation': [], 'Sparse Vegetation': [], 'Ecologically Barren'}

class City(Location):
    def __init__(self):
        pass

    Populations = without(Location.Populations, ['Deserted', 'Abandoned', 'Inhabited'])
    Walkabilities = without(Location.Walkabilities, ["Intraversible", "Wide open"])
    Wind_Levels = without(Location.Wind_Levels, ['Very Windy', "Hurricane"])
    Nature = without(Location.Nature, ['Wilderness', 'Heavy Vegetation'])

class Mountains(Location):
    def __init__(self):
        pass

    Populations = without(Location.Populations, ["Heavily Inhabited", "Overpopulated"])

