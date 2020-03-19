#!/usr/bin/python

import argparse

# daily-trading Amazon Stock
# input -> list of values
# output -> 1 value (max profit that can be made for a single buy and sell)
# max difference between smallest and largest in the list
# computed as a subtraction between a value and another value that comes before it

# keep checking current_min_price_so_far and max_profit_so_far

# plan


a = [100, 90, 80, 50, 20, 10]
b = [10, 7, 5, 8, 11, 9]
c = [1050, 270, 1540, 3800, 2]
d = [100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]
e = [10000, 1000, 5900, 50, 5000, 10]


def find_max_profit(prices):

    if len(prices) < 2:
        return "Not enough values to calculate profit"
    else:
        my_list = []
        for i, a in enumerate(prices):
            for b in prices[i+1:]:

                profit = b - a
                my_list.append(profit)

        result = max(my_list)

    return result



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))