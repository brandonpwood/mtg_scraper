from bs4 import BeautifulSoup
import requests
import copy
r = requests.get("https://www.mtggoldfish.com/metagame/standard#paper")
# print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
#print(soup)


class meta():
    def __init__(self):
        archs = []
    def find_all_archs(self, soup):
        # Separate archetypes
        found_archetypes = soup.find_all('div', class_ = 'archetype-tile')
        for found_archetype in found_archetypes:
            # Initialize new archetype
            self.archs.append(arch())

            # Find archetype name

class arch:
    def __init__(self):
        # Archetype statistics
        self.name = "" # Archetype name
        self.colors = [] # Deck colors, probably better way to do this
        self.per = 0 # Metagame percentage
        self.is_online = False # Boolean for deck format
        self.paper_price = 0 # Price in USD
        self.MTGO_price = 0 # Price in tix
        self.top_cards = ["","",""] # Names of top top_card
        self.link = "" # String consisting of a link to archetype on mtggoldfish
    def print_to_discord (self):
        pass
    def print_to_terminal(self):
        # Dump all attributes and accompanying values
        print(self.__dict__)
    def full_initialized(self):
        # Ensures all values are non-default
        pass
    def basic_initialized(self):
        # Ensures most important values are non-defualt
        pass

def make_archs(n):
    pass
# make_archs(5)
a = arch()

# b = soup.find_all('div', class_ = "archetype-tile-description-wrapper")
# print(b[1])
# c = soup.find_all('span', class_ = "deck-price-paper")
# print(len(c))
# for i in c:
#     print(i.text)

# deck_titles = soup.find_all('div', class_ = "archetype-tile-title")
# for i in deck_titles:
#     print('----------')
#     print(i.find('span', class_ = "deck-price-online").text)


print(find_all_archs(soup))
