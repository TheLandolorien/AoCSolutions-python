#!C:\python27
#--- Day 15: Science for Hungry People ---
#http://adventofcode.com/day/#

import sys, re
import numpy as np
from itertools import product

def main(data):
    recipe = parse_data(data)
    score = score_recipe(recipe)
    print 'The total score of the highest-scoring cookie is {}.'.format(score)

    score = score_recipe_with_calories(recipe)
    print 'The total score of the highest-scoring cookie (w/calories) is {}.'.format(score)


def parse_data(recipe):
    ingredients = np.empty([len(recipe), 5], dtype=int)
    
    for ingredient in recipe:
        index = recipe.index(ingredient)
        components = ingredient.split(' ')
        name = components[0].strip(':')
        capacity = int(components[2].strip(','))
        durability = int(components[4].strip(','))
        flavor = int(components[6].strip(','))
        texture = int(components[8].strip(','))
        calories = int(components[10].strip(','))

        ingredients[index] = (capacity, durability, flavor, texture, calories)
        
    return ingredients

def score_recipe(ingredients):
    weights = gen_weights(len(ingredients))
    best_score = 0

    for weight in weights:
        result = np.average(ingredients, axis=0, weights=weight) * 100

        if min(result) > 0:
            score = np.prod(result[:-1])
            if score > best_score:
                best_score = score

    return int(best_score)
        

def score_recipe_with_calories(ingredients):
    weights = gen_weights(len(ingredients))
    best_score = 0

    for weight in weights:
        result = np.average(ingredients, axis=0, weights=weight) * 100

        if min(result) > 0 and result[4] == 500:
            score = np.prod(result[:-1])
            if score > best_score:
                best_score = score

    return int(best_score)

def gen_weights(length):
    prod = product(range(1, 101), repeat=length)

    for possible in prod:
        if sum(possible) == 100:
            yield possible


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    main(lines)
