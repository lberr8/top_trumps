import random
import requests

def selected_pokemon():
    pokemon_id = random.randint(1, 151) # 1. Generate a random number between 1 and 151 to use as the Pokemon ID number
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)  # 2. Using the Pokemon API get a Pokemon based on its ID number
    pokemon = requests.get(url).json()

    chosen_pokemon = {} # 3. Create a dictionary that contains the returned Pokemon's name, id, height and weight (★https://pokeapi.co/)
    chosen_pokemon["Name"] = pokemon["name"].upper()
    chosen_pokemon["Height"] = pokemon["height"]
    chosen_pokemon["Weight"] = pokemon["weight"]
    chosen_pokemon["Base stat"] = pokemon["stats"][0]["base_stat"]
    chosen_pokemon["Experience"] = pokemon["base_experience"]
    chosen_pokemon["Number of moves"] = len(pokemon["moves"])

    return chosen_pokemon


print("Let's play Pokemon Top Trumps!" + "\n")

print("You have selected: " + "\n")
print("Loading...." + "\n")

player_pokemon = selected_pokemon() # 4a Get a random Pokemon for the player and...
# print(player_pokemon)
# print("\n")

for poke, stat in player_pokemon.items(): # print player's card
    print(poke.title() + ":", stat)
print("\n")

# create dictionary to make stat selection input easier for user

input_selection = {"1":"Height",
                   "2":"Weight",
                   "3":"Base stat",
                   "4":"Experience",
                   "5":"Number of moves"
                    }

poke_stat = input("Please enter a number to select a stat to play: " + "\n" + "1 - Height" + "\n" + "2 - Weight" + "\n" + "3 - Base stat" + "\n" + "4 - Experience" + "\n" + "5 - Number of moves" + "\n" + "\n" + "Enter number here: ")  # 5. Ask the user which stat they want to use (id, height or weight)
print("\n")
print(f"You have chosen: {input_selection[poke_stat]}")
print("\n")

stat = input_selection[poke_stat]
player_poke_stat = player_pokemon[stat]

# print(player_poke_stat)


opponent_pokemon = selected_pokemon() # 4b get another pokemon for their opponent
opponent_pokemon_stat = opponent_pokemon[stat]

if player_poke_stat == opponent_pokemon_stat:   # 6. Compare the player's and opponent's Pokemon on the chosen stat to decide who wins
    print("*** It's a draw! ***" + "\n")
elif player_poke_stat > opponent_pokemon_stat:
    print("*** You win! ***")
else:
    print("*** You lose! ***")
print("\n")

print("Your opponent's card was: " + "\n")


for poke, stat in opponent_pokemon.items(): # print opponent's card
    print(poke.title() + ":", stat)
print("\n")
