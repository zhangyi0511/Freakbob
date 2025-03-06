import random
import time

# TEXT
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

# CUSTOMER INTERACTION
def greet_customer(lives):
    print_slow("\nA hungry customer walks up to the counter.")
    print_slow("CUSTOMER: Is this the Krusty Krab?")
    print_slow(">> PATRICK: No, this is PATRICK.")
    print_slow("\nCUSTOMER: ...Oh, Okay. PATRICK,")
    
    wants_drink = random.choice([True, False])

    if wants_drink:
        print_slow("CUSTOMER: I'd like to start off with Kelp Juice.")
    else:
        print_slow("CUSTOMER: No drink for me today, please.")
               
    take_order(lives, wants_drink)
   
# TAKE ORDER
def take_order(lives, wants_drink):
    patty_ingredients = ["Lettuce", "Tomato", "Cheese", "Pickles", "Onions", "Bacon"]
    customer_ingredients = random.sample(patty_ingredients, random.randint(1, len(patty_ingredients)))
    print_slow(f"CUSTOMER: And I'd like my Krabby Patty with {', '.join(customer_ingredients)}. ")
   
    print_slow("\nMake the customer's order by adding the correct ingredients! \nThe Refrigerator includes: ")
    print_slow(", ".join(patty_ingredients))
    chosen_ingredients = input(">> CHOOSE INGREDIENTS (separated by commas):  ").split(', ')
    chosen_ingredients = [ingredient.strip() for ingredient in chosen_ingredients]
    
    valid_ingredients = [ingredient for ingredient in chosen_ingredients if ingredient in patty_ingredients]
    
    if set(valid_ingredients) != set(customer_ingredients):
        print_slow("\nThe customer is disappointed! You chose the wrong ingredients.\n >> YOU LOST ONE (1) LIFE.")
        lives -= 1
        
    print_slow(f"You've made a Krabby Patty with {', '.join(valid_ingredients)}!")
    
    if wants_drink:
        drink_choice = input(">> ADD A DRINK? (Yes/No): ")
        if drink_choice == "Yes":
            print_slow("You give the customer their drink.")
            
        if drink_choice == "No":
            print_slow("You forgot to give the customer their drink.\n >> YOU LOST ONE (1) LIFE.")
            lives -= 1
    
    serve_order(lives)

def serve_order(lives):
    # Serving the customer
    print_slow("You hand the order to the customer.")
    print_slow("CUSTOMER: Thank you so much!")         
                 
    if random.random() < 0.3:
        plankton_attack(lives)
    else:
        print_slow("\nCongratulations! The Krusty Krab is running smoothly.")

# PLANKTON ATTACK
def plankton_attack(lives):
    print_slow("\nPLANKTON suddenly appears in the kitchen!")
    choice = input(">> What will you do?\n(1) Run after PLANKTON\n(2) Ignore PLANKTON: ")
    
    if choice == "1":
        print_slow("\nYou chase Plankton away, and successfully take back the secret formula!")
    else:
        print_slow("\nPlankton successfully steals the secret formula! Mr. Krabs is Furious, and the Krusty Krab shuts down! \n ----- GAME OVER -----")
        game_over()

# GAME OVER
def game_over():
    print_slow("\n----- GAME OVER -----")
    choice = input("\nPlay again? (Yes/No): ")
    if choice == "Yes":
        start_game()
    else:
        print_slow("\nThanks for playing! See you next time, PATRICK!")
        exit()

def start_game():
    lives = 4
    customer_count = 0  # Counter for the number of customers served
    print_slow("Welcome to the Krusty Krab, PATRICK!")
    print_slow("Your best friend, SPONGEBOB, is sick! Today you must take his place and serve customers, protect the secret formula, and make sure you don't mess up!")
    
    # Continue the game until 5 customers are served or lives are lost
    while lives > 0 and customer_count < 5:
        greet_customer(lives)
        lives = take_order(lives, random.choice([True, False]))  # Update lives after each customer
        customer_count += 1  # Increment the counter after serving a customer
        
        if lives <= 0:
            game_over()
            break
    
    if customer_count == 5:
        print_slow("\nCongratulations! You've successfully served 5 customers today!")
        print_slow("The Krusty Krab is running as smooth as ever!")
        
        # SpongeBob's appearance and thanks
        print_slow("\nSPONGEBOB suddenly appears from the front door!")
        print_slow("SPONGEBOB: Wow, PATRICK! You really saved the day! Thanks for filling in for me!")
        print_slow("SPONGEBOB: The Krusty Krab is in good hands with you! Keep it up!")
        
        game_over()

start_game()
