def inventory_tracker():
    cart = {}
    
    food_items = {
        "milk": 192,
        "eggs": 350,
        "bread": 120,
        "cheese": 75,
        "apples": 200,
        "bananas": 180,
        "chicken": 90,
        "rice": 300,
        "pasta": 250,
        "yogurt": 140
    }

    tech_items = {
        "laptop": 42,
        "smartphone": 85,
        "tablet": 60,
        "headphones": 150,
        "keyboard": 95,
        "mouse": 110,
        "monitor": 40,
        "usb cable": 300,
        "portable charger": 120,
        "smartwatch": 55
    }
    
    home_items = {
        "toilet paper": 240,
        "paper towels": 180,
        "laundry detergent": 75,
        "dish soap": 130,
        "trash bags": 200,
        "light bulbs": 95,
        "cleaning spray": 110,
        "sponges": 160,
        "batteries": 140,
        "hand soap": 150
    }

    print("Hi, what would you like to buy?")
    print("We have tech, home items, and food!")
    print("Pick from: tech, food, or home.")
    choice = input().lower()

    if choice == "tech":
        print(f"We have {tech_items} in stock today.")
        print("What would you like to buy?")
        tech_choice = input().lower()

        if tech_choice in tech_items:
            stock = tech_items[tech_choice]

            tech_prices = {
                "laptop": 300,
                "smartphone": 500,
                "tablet": 250,
                "headphones": 80,
                "keyboard": 40,
                "mouse": 25,
                "monitor": 150,
                "usb cable": 10,
                "portable charger": 35,
                "smartwatch": 200
            }

            price = tech_prices[tech_choice]

            print(f"This is priced at ${price} and we have {stock} in stock.")
            print("How many would you like to buy?")
            amount = int(input())

            if amount < 1 or amount > stock:
                print("Do not waste my time, get out of my store!")
                return

            total = amount * price
            print(f"That will cost ${total}")
            print("Card or Cash?")
            payment_method = input().lower()

            if payment_method == "card":
                new_total = total * 0.90
                print(f"Your new total is ${new_total}")
            else:
                new_total = total * 0.80
                print(f"Your new total is ${new_total}")

            tech_items[tech_choice] -= amount
            print(f"Thanks! Now we only have {tech_items[tech_choice]} {tech_choice}(s) left!")
        else:
            print("I dont have time for you. Get out!")
            exit()

    elif choice == "food":
        print(f"We have {food_items} in stock today.")
        print("What would you like to buy?")
        food_choice = input().lower()
        
        if food_choice in food_items:
            stock = food_items[food_choice]

            food_prices = {
                "milk": 4,
                "eggs": 3,
                "bread": 2,
                "cheese": 5,
                "apples": 1,
                "bananas": 1,
                "chicken": 8,
                "rice": 3,
                "pasta": 2,
                "yogurt": 1
            }

            price = food_prices[food_choice]       
            print(f"This is priced at ${price} and we have {stock} in stock.")
            print("How many would you like to buy?")
            amount = int(input())

            if amount < 1 or amount > stock:
                print("Do not waste my time, get out of my store!")
                return

            total = amount * price
            print(f"That will cost ${total}")
            print("Card or Cash?")
            payment_method = input().lower()

            if payment_method == "card":
                new_total = total * 0.90
                print(f"Your new total is ${new_total}")
            else:
                new_total = total * 0.80
                print(f"Your new total is ${new_total}")

            food_items[food_choice] -= amount
            print(f"Thanks! Now we only have {food_items[food_choice]} {food_choice}(s) left!")
        else:
            print("I dont have time for you. Get out!")
            exit()

    elif choice == "home":
        print(f"We have {home_items} in stock today.")
        print("What would you like to buy?")
        home_choice = input().lower()

        if home_choice in home_items:
            stock = home_items[home_choice]

            home_prices = {
                "toilet paper": 6,
                "paper towels": 5,
                "laundry detergent": 12,
                "dish soap": 4,
                "trash bags": 7,
                "light bulbs": 10,
                "cleaning spray": 6,
                "sponges": 3,
                "batteries": 8,
                "hand soap": 3
            }

            price = home_prices[home_choice]
            print(f"This is priced at ${price} and we have {stock} in stock.")
            print("How many would you like to buy?")
            amount = int(input())

            if amount < 1:
                print("Do not waste my time, get out of my store!")
                return
            elif amount > stock:
                print(f"We have only {stock}, please pick an amount lower then that.")
                amount = int(input())
                if amount > stock:
                    print("I dont have time for you. Get out of my store!")
                    exit()
            
            total = amount * price
            print(f"That will cost ${total}")
            print("Card or Cash?")
            payment_method = input().lower()

            if payment_method == "card":
                new_total = total * 0.90
                print(f"Your new total is ${new_total}")
            else:
                new_total = total * 0.80
                print(f"Your new total is ${new_total}")

                home_items[home_choice] -= amount
                print(f"Thanks! Now we only have {home_items[home_choice]} {home_choice}(s) left!")
        else:
            print("I dont have time for you. Get out!")
            exit()
    else:
        print("I dont have time for you. Get out!")
                        
        exit()
    
    
    print("Would you like to sign up for a rewards program?")
    rewards_choice = input().lower()

    if rewards_choice == "yes":
        print("Alright! Type in your gmail please")
        gmail = input().lower()

        if "@gmail.com" in gmail:
            print("Alright, now make a password please! It needs to have 8 characters, 1 special character, and a number!")

            password = input()

            special_characters = "!@#$%^&*()"
            numbers = "0123456789"

            if len(password) >= 8 and any(c in password for c in special_characters) and any(n in password for n in numbers):
                print("Amazing!")
                print("Thank you, you are in the rewards program now!")
                print("Have a good day!")
            else:
                print("Invalid. Skipping..")
                print("Have a good day!")
        else:
            print("Invalid gmail. Skipping..")
            print("Have a good day!")
    else:
        print("No problem.")
        print("Have a good day!")


inventory_tracker()

  
