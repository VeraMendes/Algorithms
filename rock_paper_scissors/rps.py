#!/usr/bin/python

import sys

# def rock_paper_scissors(n):
#   results = []
#   if n<= 0:
#     return [[]]

#   def play(string, arr):
#     print(string)
#     print(arr)
#     if string != '':
#       arr.append(string)
#     if len(arr) == n:
#       results.append(arr)
#       # arr.pop()
#       return results
   
#     # if string != '':
#     #   arr.append(string)
  
#     play('rock', arr)
#     play('paper', arr)
#     play('scissors', arr)

#   play('', [])

#   return results 

def rock_paper_scissors(n):
    #strings = [[‘rock’],[‘paper’],[‘scissors’]]
    if n <= 0:
        return [[]]
    else:
        return add_string(rock_paper_scissors(n-1))
def add_string(play):
    list_return =[]
    strings = [['rock'],['paper'],['scissors']]
    for i in play:
        for j in strings:
            list_return.append(i + j)
    return list_return


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')