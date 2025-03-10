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

# TAKING ORDER
def take_order():
    global lives
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
    
    # TRACKING IF ORDER IS CORRECT
    order_correct = set(valid_ingredients) == set(customer_ingredients)

    if not order_correct:
        print_slow("\nThe customer is disappointed! You chose the wrong ingredients.\n>> YOU LOST ONE (1) LIFE.")
        lives -= 1
    else:
        print_slow(f"You've made a Krabby Patty with {', '.join(valid_ingredients)}!")
    
    if wants_drink == True:
        drink_choice = input(">> ADD A DRINK? (Yes/No): ")
        
        if drink_choice == "Yes":
            print_slow("You give the customer their drink.")
        elif drink_choice == "No":
            print_slow("You forgot to give the customer their drink! \n>> YOU LOST ONE (1) LIFE.")
            lives -= 1
    
    if wants_drink == False:
        drink_choice = input(">> ADD A DRINK? (Yes/No): ")
        
        if drink_choice == "No":
            print_slow("The customer is satisfied.")
        elif drink_choice == "Yes":
            print_slow("The customer didn't want a drink!>> YOU LOST ONE (1) LIFE!")
            lives -= 1

    return order_correct  # Return whether the order was correct or no
    
x = take_order()

def serve_order(order_correct):
    print_slow("You hand the final order to the customer.")
    
    if order_correct:
        print_slow("CUSTOMER: This is perfect, Thank you so much!")
        print_slow("The customer accepts the food, and walks out the Krusty Krab happily.")
    else:
        print_slow("CUSTOMER: Ugh, this isn't what I wanted. I'm disappointed!")
        print_slow("The customer takes the food, and storms out the Krusty Krab angrily.")
    
    if random.random() < 0.3:
        plankton_attack(lives)
    else:
        print_slow("\nThanks to you, the Krusty Krab is running smoothly.")
        
serve_order(x)

def plankton_attack(lives):
    print_slow("\nPlankton suddenly appears in the kitchen!")
    choice = input(">> What will you do? (1) Run after him (2) Ignore him: ")
    
    if choice == "1":
        print_slow("You chase Plankton away and take back the formula succesfully!")
    else:
        print_slow("Plankton succesfully steals the formula! GAME OVER.")
        game_over()
        
def game_over():
    print_slow("GAME OVER!")
    choice = input("Play again? (y/n):\n")
    if choice.lower() == "y":
        start_game
    else:
        print_slow("Thanks for playing! See you next time!")
        exit()

def start_game():
    lives = 4
    print_slow("Welcome to the Krusty Krab!")
    print_slow("Serve customers, protect the secret formula, and make sure you don't mess up!")
    
    while lives > 0:
        greet_customer(lives)
        
    game_over()
    
start_game()
    print_slow("GAME OVER!")
    choice = input("Play again? (y/n):\n")
    if choice.lower() == "y":
        start_game
    else:
        print_slow("Thanks for playing! See you next time!")
        exit()

def start_game():
    lives = 4
    print_slow("Welcome to the Krusty Krab!")
    print_slow("Serve customers, protect the secret formula, and make sure you don't mess up!")
    
    while lives > 0:
        greet_customer(lives)
        
    game_over()
    
start_game()