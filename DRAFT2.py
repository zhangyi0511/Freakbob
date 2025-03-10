import random
import time
lives = 4
customer_count = 0

# TEXT STYLE
def print_slow(text):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.04)
    print()

# GAME INTRODUCTION
def start_game():
    global lives, customer_count
    lives = 4
    customer_count = 0
    print_slow("Welcome to the Krusty Krab, PATRICK!")
    print_slow("Your best friend, SPONGEBOB, is sick! Today you must take his place and serve customers, protect the secret formula, and make sure you don't mess up!")
    print_slow("Your goal is to serve FIVE (5) total customers with only FOUR (4) lives.\nGOOD LUCK!")

# GREET CUSTOMER
def greet_customer():
    print_slow("\nA hungry customer walks up to the counter.")
    print_slow("CUSTOMER: Is this the Krusty Krab?")
    print_slow(">> PATRICK: No, this is PATRICK.")
    print_slow("\nCUSTOMER: ...Oh, Okay. PATRICK,")

# TAKING CUSTOMER ORDER
def take_order():
    global lives
    patty_ingredients = ["Sea Lettuce", "Tartar Sauce", "Sea Cheese", "Sea Pickles", "Sea Ketchup", "Jellyfish Jelly"]
    customer_ingredients = random.sample(patty_ingredients, random.randint(1, len(patty_ingredients)))
    wants_drink = random.choice([True, False])

    if wants_drink:
        print_slow("CUSTOMER: I'd like to start off with Kelp Juice.")
    else:
        print_slow("CUSTOMER: No drink for me today, please.")

    print_slow(f"CUSTOMER: And I'd like my Krabby Patty with {', '.join(customer_ingredients)}. ")

    # MAKE KRABBY PATTY
    print_slow("\nMake the customer's order by adding the correct ingredients!\nThe Refrigerator includes: ")
    print_slow(", ".join(patty_ingredients))
    
    chosen_ingredients = input(">> CHOOSE INGREDIENTS (separated by commas): ").split(', ')
    chosen_ingredients = [ingredient.strip() for ingredient in chosen_ingredients]

    valid_ingredients = [ingredient for ingredient in chosen_ingredients if ingredient in patty_ingredients]
    food_correct = set(valid_ingredients) == set(customer_ingredients)

    # MAKE KELP JUICE
    drink_choice = input(">> ADD A DRINK? (Yes/No): ").strip().lower()
    drink_correct = (drink_choice == "yes" and wants_drink) or (drink_choice == "no" and not wants_drink)

    if not food_correct:
        lives -= 1
        print_slow(f"\nThe customer is disappointed! You chose the wrong ingredients.\n>> YOU LOST ONE (1) LIFE.\n>> LIVES LEFT: {lives}")

    if not drink_correct:
        lives -= 1
        print_slow(f"\nYou made a mistake with the Kelp Juice!\n>> YOU LOST ONE (1) LIFE.\n>> LIVES LEFT: {lives}")

    order_correct = food_correct and drink_correct
    return order_correct

# SERVING CUSTOMER
def serve_order(order_correct):
    global customer_count
    print_slow("\nYou hand the complete order to the customer.")
    
    if order_correct:
        print_slow("CUSTOMER: This is perfect, Thank you so much!")
        print_slow("The customer accepts the food, and walks out the Krusty Krab happily.")
    else:
        print_slow("CUSTOMER: Ugh, this isn't what I wanted!")
        print_slow("The customer takes the food, and storms out the Krusty Krab angrily.")
    
    customer_count += 1
    if random.random() < 0.35:
        plankton_attack()

# PLANKTON ATTACK
def plankton_attack():
    global lives
    print_slow("\nPlankton suddenly appears in the kitchen!")
    print_slow("(1) Run after PLANKTON\n(2) Ignore PLANKTON")
    try:
        choice = int(input(">> WHAT WILL YOU DO?: "))
    except ValueError:
        print("\n----- ERROR: Please input an Integer. -----")
        plankton_attack()
    else:
        if choice == 1:
            print_slow("\nYou chase PLANKTON away and take back the secret formula successfully!")
            print_slow("PLANKTON: I'll be back for that secret formula, PATRICK!")
            print_slow("In defeat, PLANKTON runs back to the Chum Bucket.")
            return # RETURNS TO MAIN GAME LOOP
        else:
            print_slow("\nPLANKTON successfully steals the Krabby Patty secret formula!")
            print_slow("MR. KRABS is furious, and bans you from ever coming back!")
            print_slow("The Krusty Krab shuts down, and the Chum Bucket earns Bikini Bottom’s favor!")
            game_over()

# GAME OVER SCREEN
def game_over():
    global lives, customer_count
    print_slow("\n----- GAME OVER! -----")
    choice = input(">> PLAY AGAIN? (Yes/No): ")
    if choice == "Yes":
        start_game()
        main_game_loop()
    else:
        print_slow("Thanks for playing, PATRICK! See you next time!")
        exit()

# MAIN GAME LOOP
def main_game_loop():
    global lives, customer_count
    while 0 < lives <= 4 and customer_count < 5:
        greet_customer()
        order_correct = take_order()
        serve_order(order_correct)
    
    if customer_count == 5:
        print_slow("\n----- CONGRATULATIONS! -----")
        print_slow("You successfully served FIVE customers and completed your shift!")
        print_slow("SPONGEBOB will be proud of you. Well done, PATRICK!")
        
        choice = input("\n>> PLAY AGAIN? (Yes/No): ")
        if choice == "Yes":
            start_game()
            main_game_loop()
        else:
            print_slow("Thanks for playing, PATRICK! See you next time!")
            exit()
    else:
        game_over()

# START THE GAME
start_game()
main_game_loop()
