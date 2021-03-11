from bs4 import BeautifulSoup
import requests
import copy
import re
import matplotlib.pyplot as plt
import numpy as np

class meta():
    def __init__(self, format):
        r = requests.get("https://www.mtggoldfish.com/metagame/" + format + "#paper")
        soup = BeautifulSoup(r.text, 'html.parser')
        self.archs = []
        self.find_all_archs(soup)

    def find_all_archs(self, soup):
        # Separate archetypes
        found_archetypes = soup.find('div', id = "metagame-decks-container").find_all('div', class_ = 'archetype-tile')
        for found_archetype in found_archetypes:
            # Initialize new archetype
            self.archs.append(arch())

            # Find archetype name
            title_box = found_archetype.find("div", class_ = "archetype-tile-title") # Pulls up titlebox
            self.archs[-1].name = title_box.find('span').text[1:-1] # Grabs name from titlebox, inserts into new arch

            # Find metagame percentage, number of decks
            text = found_archetype.find('div', class_ = "archetype-tile-statistic metagame-percentage").text
            self.archs[-1].per = float(re.findall("\d.*%", text)[0][0:-1])
            self.archs[-1].num_decks = int(re.findall("\(.*\)", text)[0][1:-1])

            # Find deck colors
            color_string = found_archetype.find("span", class_ = "manacost")
            if(color_string):
                color_string = color_string.attrs['aria-label']
                color_string = color_string[8:].split(" ")
                self.archs[-1].colors = color_string
            else:
                self.archs[-1].colors = []

            # Find
            # print('----------')
    def pie_meta(self, n):
        # Create and save a pie chart of the current meta
        counter = 0
        y = []
        my_labels = []
        while( (counter < n) and counter < len(self.archs)):
            y.append(self.archs[counter].per)
            my_labels.append(self.archs[counter].name)
            counter += 1
        y = np.array(y)
        plt.pie(y, labels = my_labels, autopct='%1.1f%%')
        plt.savefig('test.png')

    def print_to_terminal(self):
        for i in self.archs:
            i.print_to_terminal()
            print('--------')
class arch:
    def __init__(self):
        # Archetype statistics
        self.name = "" # Archetype name
        self.per = 0 # Metagame percentage
        self.num_decks = 0 # Number of decks in the metagame
        self.colors = [] # Deck colors, probably better way to do this
        self.paper_price = 0 # Price in USD
        self.MTGO_price = 0 # Price in tix
        self.top_cards = ["","",""] # Names of top top_card
        self.link = "" # String consisting of a link to archetype on mtggoldfish

    def print_to_terminal(self):
        # Dump all attributes and accompanying values
        print(self.__dict__)
    def full_initialized(self):
        # Ensures all values are non-default
        pass
    def basic_initialized(self):
        # Ensures most important values are non-defualt
        pass

M = meta('commander')
M.pie_meta(10)
