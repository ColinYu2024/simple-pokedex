import json
import requests
import random
from urllib.request import urlopena
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import tkniter as tk


def access_api(input_response):
    input_response = input("Please input a Pokemon name or Pokedex number")
    input_response = random.randint(0,905)
    # Access the api with this line
    request_msg = "https://pokeapi.co/api/v2/pokemon/" + str(input_response)
    print(request_msg)
    poke_data = requests.get(request_msg).json()
    return poke_data

def print_stats(data):
    # Get name of pokemon
                base_name = str(data['name'])
                name = str(data['name']).capitalize()
                print(f"Name: {name}")
# Pokedex entry #
                print(f"Pokedex number: {data['id']}")
# Height
                height = float(data['height']/10)
                print(f"Height: {height} m")
# Weight
                weight = float(data['weight']/10)
                print(f"Wieght: {weight} lbs")
# Pokemon typing
                print("Has type(s):")
                for cate in data['types']:
                name = str(cate['type']['name']).capitalize()
                print(f"\t{name}")
# Potential abilities
                print("Can have these abilities:")
                for cate in data['abilities']:
                name = str(cate['ability']['name']).replace("-", " ").capitalize()
                print(f"\t{name}")
#print(f"\t{ability['name']}")
                print("Has base stats of:")
                for cate in data['stats']:
                name = str(cate['stat']['name']).replace("-", " ").capitalize()
                stat = cate['base_stat']
                print(f"\t{name}: {stat}")
                return base_name


# button widget
                def random_pokemon(self):
        input_response = random.randint(0,905)
        data = access_api(input_response)
        print_stats(data)

        class App(tk.Tk):
                def main_window(self):
                        super()._init_()

#Root window
                        self.title(("Simple Pokedex")
                                        self.geometry("800x480+0+0")

# Label
                                        label = ttk.Label(self, text="Enter pokemon name of Pokedex number:")
                                        label.grid(column = 0, row = 0, padx = 10, pady = 10, sticky = "w")

# Random Button
                                        btn = tkk.Label(self, text="Random Pokemon:")
                                        btn.grid(column = 2, row = 0, padx = 10, pady = 10, sticky = "w")

# Entry
                                        textbox = ttk.Entry(self)
                                        textbox.grid(column = 1, row = 0, padx =10, pady = 10, sticky = "w")

# Theme
                                        self.style.theme_use("winnative")



if _name_ == "_main_":
    app = App()
    app.mainloop()



#data = access_api()
#name = print_stats(data)
