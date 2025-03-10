import random
import time
lives = 4

#TEXT
def print_slow(text):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.04)
    print()

def print_fast(text):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.01)
    print()

# GAME INTRODUCTION
def start_game():
    customer_count = 0  # Counter for the number of customers served
    print_slow("Welcome to the Krusty Krab, PATRICK!")
    print_slow("Your best friend, SPONGEBOB, is sick! Today you must take his place and serve customers, protect the secret formula, and make sure you don't mess up!")
    print_slow("Your goal is to serve FIVE (5) total customers with only THREE (3) lives.\nGOODLUCK!")

# CUSTOMER TAKES ORDER
def greet_customer():
    print_slow("\nA hungry customer walks up to the counter.")
    print_slow("CUSTOMER: Is this the Krusty Krab?")
    print_slow(">> PATRICK: No, this is PATRICK.")
    print_slow("\nCUSTOMER: ...Oh, Okay. PATRICK,")
    
start_game()
greet_customer()

def take_order(lives, wants_drink):
    patty_ingredients = ["Sea Lettuce", "Tartar Sauce", "Sea Cheese", "Sea Pickles", "Sea Ketchup", "Jellyfish Jelly"]
    customer_ingredients = random.sample(patty_ingredients, random.randint(1, len(patty_ingredients)))
    wants_drink = random.choice([True, False])
    
    if wants_drink == True:
        print_slow("CUSTOMER: I'd like to start off with Kelp Juice.")
    elif wants_drink == False:
        print_slow("CUSTOMER: No drink for me today, please.")
    
    print_slow(f"CUSTOMER: And I'd like my Krabby Patty with {', '.join(customer_ingredients)}. ")
    
    print_slow("\nMake the customer's order by adding the correct ingredients!\nThe Refrigerator includes: ")
    print_slow(", ".join(patty_ingredients))
    chosen_ingredients = input(">> CHOOSE INGREDIENTS (separated by commas):  ").split(', ')
    chosen_ingredients = [ingredient.strip() for ingredient in chosen_ingredients]
    
    valid_ingredients = [ingredient for ingredient in chosen_ingredients if ingredient in patty_ingredients]
    
    if set(valid_ingredients) != set(customer_ingredients):
        print_slow("\nThe customer is disappointed! You chose the wrong ingredients.\n >> YOU LOST ONE (1) LIFE.")
        lives -= 1
    else:
        print_slow(f"You've made a Krabby Patty with {', '.join(valid_ingredients)}!")
        
    if wants_drink:
        drink_choice = input(">> ADD A DRINK? (Yes/No): ")
        
        if drink_choice == "Yes" and :
            print_slow("You give the customer their drink.")
        elif drink_choice == "No":
            print_slow("The customer didn't want a drink! YOU LOST ONE (1) LIFE!")

    if drink_choice == "No":
        print_slow("You forgot to give the customer their drink.\n >> YOU LOST ONE (1) LIFE.")
        lives -= 1