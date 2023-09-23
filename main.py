# Location class that holds a list of keywords
class Location:
    def __init__(self, name):
        self.name = name
        self.keywords = []
    def add_keyword(self, keyword):
        self.keywords.append(keyword)
    def get_name(self):
        return self.name
    def get_keywords(self):
        return self.keywords

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
        else:
            tempWord = tempWord + scriptChars[char]
    return scriptwords
    #Tests reading in from .txt file
    #for word in range(len(keywords)):
    #    print(keywords[word])

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
        else:
            tempWord = tempWord + locationChars[char]
    return locations
    # Tests reading in from .txt file
    #for location in range(len(locations)):
    #    print(locations[location].get_name())
    #    for keyword in range(len(locations[location].get_keywords())):
    #        print(locations[location].get_keywords()[keyword])





if __name__ == "__main__":
    wordsinscript = getScript()
    locationlist = getLocations()