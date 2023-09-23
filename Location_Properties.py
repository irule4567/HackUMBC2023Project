class Location:
    Temperatures = {'Very Cold': [], 'Cold': [], 'Cool': [], 'Warm': [], 'Hot': [], 'Very Hot': []}
    Sky_Types = {'Snowy': [], 'Rainy': [], 'Cloudy': [], 'Sunny': [], 'Stormy': []}
    Populations = {'Deserted': [], 'Abandoned': [], 'Inhabited': [], 'Heavily inhabited': [], 'Overpopulated': []}
    Precipitations = {'Never': [], 'Rarely': [], 'Sometimes': [], 'Often': [], 'Almost Always': []}
    Walkabilities = {'Intraversable': [], 'Difficult': [], 'Walkable': [], 'Easily Traversed': [], "Wide open": []}
    Humidities = {'Dry': [], 'Average': [], 'Humid': []}
    Wind_Levels = {'Still': [], 'Breezy': [], 'Windy': [], 'Very Widy': [], 'Hurricane': []}
    Nature = {'Wilderness':[], }

class City(Location):
    Populations = {'Heavily inhabited': [], 'Overpopulated': []}
    Walkabilities = {'Difficult': [], 'Walkable': [], 'Easily Traversed': []}
