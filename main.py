import os
from art import logo

print(logo)

bids = {}
more_bidders = True

while more_bidders == True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bids.update({name: bid})

    response = input("Are there more bidders? Type 'yes' or 'no': ")
    if response == "no":
        more_bidders = False
    elif response == "yes":
        os.system('cls||clear')

print(bids)