import os
from art import logo

print(logo)

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  
  print(bids)
  print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
more_bidders = True

while more_bidders == True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bids.update({name: bid})

    response = input("Are there more bidders? Type 'yes' or 'no': ")
    if response == "no":
        more_bidders = False
        find_highest_bidder(bids)
    elif response == "yes":
        os.system('cls||clear')
