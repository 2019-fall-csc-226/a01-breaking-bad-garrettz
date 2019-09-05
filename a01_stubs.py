######################################################################
# Author: Zyshavia Garrett
# Username: garrettz
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1

import time
user_input = (input("What is your birth year?"))

if user_input == "2000":
    print("You are a fire breathing dragon.")
    print("Hot, Hot!")

elif user_input == "2001":
    print("You are a slithering snake!")
    print("The biggest snake of them all!")

elif user_input == "2002":
    print("You are a happy horse!")
    print("Such a nobel steed!")

elif user_input == "2003":
    print("You are a gracious goat!")
    print("It must be nice being the Greatest Of All Time!")
    time.sleep(2)
    print("Get it...because it spells goat:)")

elif user_input == "2004":
    print("You're a magical monkey!")
    time.sleep(2)
    print("How is the view from the trees?")

elif user_input == "2005":
    print("You are a righteous rooster!")
    time.sleep(2)
    print("Hmmmmmm...fried chicken!")

elif user_input == "2006":
    print("You are a dog!")
    print("Who's a good boy!")
    time.sleep(2)
    print("WHO LET THE DOGS OUT!")

elif user_input == "2007":
    print("You are a plump pig!")
    time.sleep(2)
    print("Oink, oink!")

elif user_input == "2008":
    print("You are a rat!")
    print("Ewwwww...I'm just kidding. Rats are cute!")
    time.sleep(2)
    print("Sometimes...")

elif user_input == "2009":
    print("You are a Ox!")
    time.sleep(2)
    print("What an odd but beautiful animal to be!")

elif user_input == "2010":
    print("You're a Tiger!")
    time.sleep(2)
    print("It's the eye of the tiger! :) ")

elif user_input == "2011":
    print("You are a cute and fuzzy rabbit!")
    time.sleep(2)
    print("Which is my favorite animal by the way!")


print('')



# See the a01_pets.py for examples


######################################################################
# (Required) Task 2

import time
user_input = (input("What is your friends birth year?"))

if user_input == "2000":
    print("They are a fire breathing dragon too.")
    print("Hot, Hot!")

elif user_input == "2001":
    print("They are a slimy snake!")
    print("Ewww!")

elif user_input == "2002":
    print("They are a horse!")
    print("NEIGHHHHHH!")

elif user_input == "2003":
    print("They are a goat!")
    time.sleep(2)
    print("Another Greatest Of All Time!")

elif user_input == "2004":
    print("They are a monkey!")
    time.sleep(2)
    print("Swinging in the beautiful trees?")

elif user_input == "2005":
    print("They are a rooster!")
    time.sleep(2)
    print("BA-CAWk!")

elif user_input == "2006":
    print("They are a dog!")
    time.sleep(2)
    print("WHO LET THE DOGS OUT!")

elif user_input == "2007":
    print("They are a pig!")
    time.sleep(2)
    print("Who has the bacon!")

elif user_input == "2008":
    print("They are a rat!")
    print("Ewwwww...nasty!")
    time.sleep(2)
    print("Just kidding...")

elif user_input == "2009":
    print("They are a Ox!")
    time.sleep(2)
    print("Such majestic animals!")

elif user_input == "2010":
    print("They are a Tiger!")
    time.sleep(2)
    print("War-Eagle...SIKE!!! I'm a Alabama fan...ROLL TIDE! :) ")

elif user_input == "2011":
    print("They are a rabbit!")
    time.sleep(2)
    print("Awwwweee...cute!")


print('')

######################################################################
# (Optional) Task 3

# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between
