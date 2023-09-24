import requests
import secrets

# Location class that holds a list of keywords
class Location:
    def __init__(self, name):
        self.name = name
        self.keywords = []
        self.keywordValue = 0
        self.matchingKeywords = []
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
    def get_matchKey(self):
        return self.matchingKeywords
    def add_matchKey(self, matchKey):
        self.matchingKeywords.append(matchKey)

# Reads in the script and stores each word
def getScript():
    #Reads in script
    script = open("Test script.txt")
    scriptwords = []
    scriptChars = script.read()
    tempWord = ""
    for char in range(len(scriptChars)):
        #print(scriptChars[char])
        if scriptChars[char] == "\n" or scriptChars[char] == "\t" or scriptChars[char] == " " or scriptChars[char] == "":
            scriptwords.append(tempWord)
            tempWord = ""
        else:
            tempWord = tempWord + scriptChars[char]
    # Tests reading in from .txt file
    #for word in range(len(scriptwords)):
    #    print(scriptwords[word])
    return scriptwords


# Reads in locations and their keywords
def getLocations():
    locationstxt = open("Locations+keywords.txt")
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

# Takes in the list of script words and list of locations and compares the words to the keywords to find which location matches more
def find_ideal_locations(script, locations):
    for place in range(len(locations)):
        for keyword in range(len(locations[place].get_keywords())):
            syn_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(locations[place].get_keywords()[keyword])
            response = requests.get(syn_url, headers={'X-Api-Key': secrets.token_urlsafe(16)})
            in_word = False
            tempWord = ""
            synonyms = [locations[place].get_keywords()[keyword]]
            char = 0
            while response.text[char] != "]":
                if response.text[char] == "[":
                    in_word = True
                elif response.text[char] == '\"' and in_word is True:
                    synonyms.append(tempWord)
                    tempWord = ""
                elif response.text[char] != "," and response.text[char] != " ":
                    tempWord = tempWord + response.text[char]
                char = char + 1
            for word in range(len(script)):
                for syn in range(len(synonyms)):
                    if synonyms[syn] == script[word]:
                        #print(locations[place].get_keywords()[keyword])
                        locations[place].add_matchKey(locations[place].get_keywords()[keyword])
                        locations[place].add_value()
    bestloc = ""
    topscore = 0
    bestlocindex = 0
    for place in range(len(locations)):
        if locations[place].get_value() > topscore:
            topscore = locations[place].get_value()
            bestloc = locations[place].get_name()
            bestlocindex = place
    print("The most ideal location is " + bestloc + " because of the following properties:")
    for matchKey in range(len(locations[bestlocindex].get_matchKey())):
        print(locations[bestlocindex].get_matchKey()[matchKey])



if __name__ == "__main__":
    wordsinscript = getScript()
    locationlist = getLocations()
    find_ideal_locations(wordsinscript, locationlist)