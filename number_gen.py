
import random

#--------------------------------------------------
# Generate a random number
#--------------------------------------------------
number = random.randint(1, 10)

#--------------------------------------------------
# Fortunes is the dictionary that stores keys of
# Integers and values of fortunes
#--------------------------------------------------
dictionary_fortunes = {
    1: "Today is your lucky day.", 
    2: "Something good is coming your way.",
    3: "You will discover something new.",
    4: "A surprise will make you smile.",
    5: "You’re closer to success than you think.",
    6: "Good things happen when you stay positive.",
    7: "A fun opportunity is waiting for you.",
    8: "You will learn something useful soon.",
    9: "Someone will appreciate you today.",
    10: "Your hard work will pay off."
}

#--------------------------------------------------
# Pick the fortune based on the random number
#--------------------------------------------------
fortune = dictionary_fortunes[number]

#--------------------------------------------------
# Print results
#--------------------------------------------------
print("Your fortune:", fortune)
print(dictionary_fortunes.values())
