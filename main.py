# Location class that holds a list of keywords
class Location:
    def __init__(self, name):
        self.name = name
        self.keywords = []
        self.keywordValue = 0
    def add_keyword(self, keyword):
        self.keywords.append(keyword)
    def get_name(self):
        return self.name
    def get_keywords(self):
        return self.keywords
    def get_value(self):
        return self.keywordValue
    def add_value(self):
        self.keywordValue = self.keywordValue + 1

# Reads in the script and stores each word
def getScript():
    #Reads in script
    script = open("Test script.txt")
    scriptwords = []
    scriptChars = script.read()
    tempWord = ""
    for char in range(len(scriptChars)):
        #print(scriptChars[char])
        if scriptChars[char] == "\n" or scriptChars[char] == "\t" or scriptChars[char] == " ":
            scriptwords.append(tempWord)
            tempWord = ""
        elif scriptChars[char] == "":
            tempWord = tempWord + scriptChars[char]
        else:
            tempWord = tempWord + scriptChars[char]
    return scriptwords
    #Tests reading in from .txt file
    #for word in range(len(keywords)):
    #    print(keywords[word])

# Reads in locations and their keywords
def getLocations():
    locationstxt = open("Test location+keywords.txt")
    locations = []
    locationChars = locationstxt.read()
    tempWord = ""
    locationPos = -1
    for char in range(len(locationChars)):
        if locationChars[char] == ":":
            tempLoc = Location(tempWord)
            locations.append(tempLoc)
            tempWord = ""
            locationPos = locationPos + 1
        elif locationChars[char] == "," or locationChars[char] == "\n":
            locations[locationPos].add_keyword(tempWord)
            tempWord = ""
        elif locationChars[char] == "":
            tempWord = tempWord + locationChars[char]
        else:
            tempWord = tempWord + locationChars[char]
    return locations
    # Tests reading in from .txt file
    #for location in range(len(locations)):
    #    print(locations[location].get_name())
    #    for keyword in range(len(locations[location].get_keywords())):
    #        print(locations[location].get_keywords()[keyword])

# Takes in the list of script words and list of locations and compares the words to the keywords to find which location matches more
def find_ideal_locations(script, location):
    for word in range(len(script)):
        for place in range(len(location)):
            for keyword in range(len(location[place].get_keywords())):
                if script[word] == location[place].get_keywords()[keyword]:
                    location[place].add_value()
    bestloc = ""
    topscore = 0
    for place in range(len(location)):
        if location[place].get_value() >= topscore:
            topscore = location[place].get_value()
            bestloc = location[place].get_name()
    print(bestloc)



if __name__ == "__main__":
    wordsinscript = getScript()
    locationlist = getLocations()
    find_ideal_locations(wordsinscript, locationlist)