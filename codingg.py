#1 Learning Variablesss


# Variable 1 stores a number and is the score
#------------------------------------------------------------------------
#This code is a recreation of buying a game with making a username and password
#and email.
#------------------------------------------------------------------------
# this section sets up all the starting values the program needs
#------------------------------------------------------------------------
player_age = 21
player_name = "AL0N3"
texting_privilege = None

age_confirmed = False
name_confirmed = False
game_purchased = False
email_confirmed = False
password_confirmed = False
promo_used = False

bank_balance = 50
game_price = 20
promo_code = "uday is smart"

saicoins = 0
#------------------------------------------------------------------------
# this section has helper functions for input and password checks
#------------------------------------------------------------------------
def ask():
    return input().lower()

def has_number(s):
    return any(c.isdigit() for c in s)

def has_special(s):
    specials = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|"
    return any(c in specials for c in s)
#---------------------------------------------------------------------------------
# this section handles confirming the player's age and updating texting privileges
#---------------------------------------------------------------------------------
print(f"Player age is {player_age}, Correct? (yes/no)")
choice = ask()

if choice == "yes":
    print("Successful")
    age_confirmed = True
elif choice == "no":
    print("Re-Enter Your Age")
    player_age = int(input("Enter your age: "))
    if player_age < 18:
        texting_privilege = False
    else:
        texting_privilege = True
    age_confirmed = True
#--------------------------------------------------------------
# this section handles confirming or changing the player's name
#--------------------------------------------------------------
print(f"Player name is {player_name}, Correct? (yes/no)")
choice_two = ask()

if choice_two == "yes":
    print("Successful")
    name_confirmed = True
elif choice_two == "no":
    print("Re-Enter Your Name")
    player_name = input("Enter your name: ")
    name_confirmed = True
#-----------------------------------------------------------------------------
# this section checks for a promo code and applies a discount if it's correct
#-----------------------------------------------------------------------------
print("Do you have a promo code or coupon? (yes/no)")
has_code = ask()

if has_code == "yes":
    print("Enter your promo code:")
    entered_code = input().strip().lower()
    if entered_code == promo_code:
        print("Promo code applied.")
        game_price = round(game_price * 0.90, 2)
        promo_used = True
    else:
        print("Invalid promo code.")
elif has_code == "no":
    print("Skipping promo code.")
#----------------------------------------------------------------------------------
# this section handles buying the game and checking if the player has enough money
#----------------------------------------------------------------------------------
print(f"The game costs ${game_price}. Your balance is ${bank_balance}. Buy the game? (yes/no)")
buy_choice = ask()

if buy_choice == "yes":
    if bank_balance >= game_price:
        bank_balance -= game_price
        game_purchased = True
        print("Purchase successful.")
    else:
        print("Not enough money.")
elif buy_choice == "no":
    print("Purchase canceled.")
#------------------------------------------------------------
# this section forces the player to enter a valid gmail email
#------------------------------------------------------------
email = ""
while not email_confirmed:
    email = input("Enter your email: ")
    if email.endswith("@gmail.com"):
        email_confirmed = True
        print("Email accepted.")
    else:
        print("Invalid email. Must be a Gmail address.")
#----------------------------------------------------------------------
# this section makes the player create a strong password and confirm it
#----------------------------------------------------------------------
while not password_confirmed:
    password = input("Create a password (8+ chars, 1 number, 1 special): ")
    password_check = input("Re-enter your password: ")

    if len(password) >= 8 and has_number(password) and has_special(password) and password == password_check:
        print("Password confirmed.")
        password_confirmed = True
    else:
        print("Password invalid. Try again.")
#---------------------------------------------------------------------------
# this section checks if everything is done and then offers the SaiCoin shop
#---------------------------------------------------------------------------
if age_confirmed and name_confirmed and game_purchased and email_confirmed and password_confirmed:
    print("All done!")
    print("Do you want to buy SaiCoins? (yes/no)")
    buy_sc = ask()
#-----------------------------------------------------------------
# this section is the SaiCoin store where the player can buy coins
#-----------------------------------------------------------------
    if buy_sc == "yes":
        print("SaiCoin Store:")
        print("1) $1  = 10 SaiCoins")
        print("2) $5  = 50 SaiCoins")
        print("3) $10 = 100 SaiCoins")
        print("4) $20 = 200 SaiCoins")
        print("Choose an option or type 0 to skip:")
        choice_sc = input()

        if choice_sc == "1" and bank_balance >= 1:
            bank_balance -= 1
            saicoins += 10
        elif choice_sc == "2" and bank_balance >= 5:
            bank_balance -= 5
            saicoins += 50
        elif choice_sc == "3" and bank_balance >= 10:
            bank_balance -= 10
            saicoins += 100
        elif choice_sc == "4" and bank_balance >= 20:
            bank_balance -= 20
            saicoins += 200

        print(f"You now have {saicoins} SaiCoins.")
        print(f"Remaining balance: ${bank_balance}")
    else:
        print("Skipping SaiCoin purchase.")
else:
    print("Process incomplete.")
