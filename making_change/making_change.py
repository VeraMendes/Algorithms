#!/usr/bin/python

import sys

cache = []
def making_change(amount, denominations):
  cache = [0] * (amount + 1)
  cache[0] = 1
  for change in denominations:
    for higher_amount in range(change, amount + 1):
      cache[higher_amount] += cache[higher_amount - change]
    
  return cache[amount]



if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")


  # 30  18
  #      1 5 10 25 50

  # 11111 11111 11111 11111 11111 11111
  # 11111 11111 11111 11111 11111 5
  # 11111 11111 11111 11111 5 5
  # 11111 11111 11111 5 5 5
  # 11111 11111 5 5 5 5
  # 11111 5 5 5 5 5
  # 11111 11111 11111 11111 10
  # 11111 11111 10 10
  # 11111 25
  # 11111 5 5 5 10
  # 11111 5 10 10
  # 11111 11111 5 5 10
  # 11111 11111 11111 5 10
  # 5 5 5 5 5 5 
  # 5 5 5 5 10
  # 5 5 10 10
  # 10 10 10
  # 5 25
