import tkSnack
import json
import requests
import random
from tkinter import *
from tkinter import messagebox
import tkinter as ttk
import numpy
import pyogg
import simpleaudio as sa
import vlc
import time


# Function to access api
def access_api(pokemon):
    try:
        request_msg = "https://pokeapi.co/api/v2/pokemon/" + str(pokemon)
        poke_data = requests.get(request_msg).json()
        return poke_data
    except requests.ConnectionError:
        print("Please try another pokemon or pokedex number")
        return None

# Auxillary Function to print stats
def print_stats(data):
    if data == None:
        text_box['state'] = 'normal'
        text_box.delete("1.0", "end")
        text_box.insert('end', "Please fix spelling, enter a pokedex entry from 1 to 905, or try a different pokemon")
        text_box['state'] = 'disabled'
        return None
    # Name
    text_box['state'] = 'normal'
    text_box.delete("1.0", "end")
    base_name = str(data['name'])
    written_name = str(data['name']).replace("-", " ").capitalize()
    msg = "Name: " + written_name + "\n"
    text_box.insert('end', msg)
    print(msg)
    
    # Pokedex number
    pdxid = str(data['id'])
    msg = "Pokedex number: " + pdxid + "\n"
    text_box.insert('end', msg)
    print(f"Pokedex number: {pdxid}")
    
    # Height
    height = str(data['height']/10)
    print(f"Height: {height}")
    text_box.insert('end', "Height: " + height + "\n")

    # Weight
    weight = str(data['weight']/10)
    text_box.insert('end', "Weight: " + weight + "\n")
    print(f"Weight: {weight}")

    # Typing
    print(f"{written_name} has types:")
    text_box.insert('end', written_name + " has types:\n")
    type_list = []
    for cat in data['types']:
        typing = cat['type']['name'].capitalize()
        text_box.insert('end', "\t" + typing + "\n")
        print(f"\t{typing}")

    # Abilities
    print(f"{written_name} has potential abilities:")
    text_box.insert('end', written_name + " has potential abilities:\n")
    ability_list = []
    for cat in data['abilities']:
        #ability_list.append(
        ability = str(cat['ability']['name']).replace("-", " ").capitalize()
        text_box.insert('end', "\t" + ability + "\n")
        print(f"\t{ability}")

    # Base Stats
    print(f"{written_name} has base stats of:")
    text_box.insert('end', written_name + " has base stats of:\n")
    for cat in data['stats']:
        name = str(cat['stat']['name']).replace("-", " ").capitalize()
        stat = str(cat['base_stat'])
        print(f"\t{name}: {stat}")
        text_box.insert('end', "\t" + name + ": " + stat + "\n")
    text_box['state'] = 'disabled'
    show_image(pdxid)
    play_sound(pdxid)

# Random Pokemon
def random_pokemon(*args):
    random_pdx = random.randint(0,905)
    print(random_pdx)
    data = access_api(random_pdx)
    print_stats(data)

# Input Pokemon
def input_pokemon(* args):
    try:
        pokemon_value = pokemon.get()
        if isinstance(pokemon_value, str):
            pokemon_value = pokemon_value.lower()
        data = access_api(pokemon_value)
        print_stats(data)
        pokemon.set("")
    except ValueError:
        pass
    

# Debug pokemon
def debug_pokemon():
    input_response = random.randint(0, 905)
    input_response = input("enter pokemon")
    data = access_api(input_response)
    print_stats(data)

# Show image
def show_image(name):
    file_path = "sprites/pokemon/" + name + ".png"
    print(file_path)
    pokemon_sprite = PhotoImage(file = file_path)
    pokemon_sprite = pokemon_sprite.zoom(2, 2)
    sprite['image'] = pokemon_sprite
    if pokemon_sprite not in sprite_list:
        sprite_list.append(pokemon_sprite)

# Play sound function
# Only supports up to id number 721
def play_sound(id_num):
    if int(id_num) > 721:
        return
    file_path = "sounds/" + id_num + ".mp3"
    p = vlc.MediaPlayer(file_path)
    p.play()
    duration = p.get_length() / 1000
    time.sleep(duration)

# Creating Display frame
root = Tk()
root.title("Simple Pokedex")

# Display window
content = ttk.Frame(root, width = 800, height = 480, padx = 10, pady = 10)
content.grid(column=0, row = 0, sticky=(N, W, E, S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

# Widgets

# Random button
ttk.Button(content, text = "Random Pokemon", command = random_pokemon).grid(column = 1, row = 4, sticky = W)

# Entry SeaO[Orch
pokemon = StringVar()
pokemon_entry = ttk.Entry(content, width = 10, textvariable = pokemon)
pokemon_entry.grid(column = 1, row = 1, sticky = (W, E))

ttk.Button(content, text = "Search", command = input_pokemon).grid(column=1, row=2, sticky = W)
root.bind("<Return>", input_pokemon)

# Labels
ttk.Label(content, text = "Enter Pokemon name of Pokedex number").grid(column =2, row = 1, sticky = E)
ttk.Label(content, text = "Search for a random Pokemon").grid(column = 2, row = 4, sticky = W)
ttk.Label(content, text = "Sound only works for first 721 pokemon").grid(column = 4, row = 4, sticky = (S, E))

# Image test

# Sound test

#play sound

sprite = ttk.Label(content)
sprite.grid(column = 2, row = 2, sticky = (N, S))
global sprite_list
sprite_list = []

# Text test
global text_box
text_box = Text(content, width = 40, height = 20)
text_box['state'] = 'disabled'
text_box.grid(column = 4, row = 2, sticky = (N, S))
text_box.insert("1.0", "Pokemon Stats:")

root.mainloop()
