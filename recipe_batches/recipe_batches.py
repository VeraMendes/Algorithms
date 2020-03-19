#!/usr/bin/python

import math

# use dicts to check how many batches can you make of a recipe using the available ingredients

# first dict has the amount of ingredients for the recipe
# second dict has the amount of ingradients available to use

def recipe_batches(recipe, ingredients):
  counter = float('inf')
  # print(counter)
  for key in recipe.keys():
    if key in ingredients.keys():
      batches = ingredients[key] // recipe[key]
      if batches < counter:
        counter = batches
        if counter == 0:
          return counter

    else:
      return 0


  return counter


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))