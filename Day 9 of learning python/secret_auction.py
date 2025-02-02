
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished: 
  name = input("what's your name? ")
  price = int(input("what's your bid?: $"))
  bids[name] = price

  asking_to_countinue = input("Are there any other bidders? Type 'yes' or 'no' \n ")
  if asking_to_countinue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif asking_to_countinue == "yes":
    bids.clear()
      

  
   
