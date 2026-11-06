import requests
import random

pokemon_list = ["groudon", "rayquaza", "kyogre", "zekrom", "kyurem"]
answer = random.choice(pokemon_list)
choices = ", ".join(pokemon_list)

url = f"https://pokeapi.co/api/v2/pokemon/{answer}"

response = requests.get(url, timeout=2)

if response.status_code == 200:
    data = response.json()
    height = data["height"]
    weight = data["weight"]
    print(" Ey, Who's that Pokemon?")
    print("Height:", height)
    print("Weight:", weight)
    print("Choices:", choices)

    done = False
    for attempt in range(3):
        if done == False:
            choice = input("guess or exit? ").lower().strip()
            if choice == "exit":
                print("You exited. The Pokemon was .....  ", answer)
                done = True
            elif choice == "guess":
                guess = input("Your guess: ").lower().strip()
                
                if guess not in pokemon_list:
                    print("Invalid Pokemon. Choose from:", choices)
                elif guess == answer:
                    print("Correct! You win!")
                    done = True
                else:
                    print("enkkk, Wrong!")
            else:
                print("Type guess or exit only.")

    if done == False:
        print("You failed. The Pokemon was .....  ", answer)
else:
    print("Request failed. Status:", response.status_code)