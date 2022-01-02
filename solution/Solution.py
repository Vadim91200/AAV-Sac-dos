import numpy as np


def solve_knapsack_greedy(knapsack, objects_dict):
    objects_dict1 = sorted(objects_dict.keys(), key=lambda item: (objects_dict[item][0] / objects_dict[item][1]), reverse=True)  # objects_dict1 sort by value/weight ratio
    for obj in objects_dict1:
        if knapsack.get_weight(objects_dict) + (objects_dict[obj][1]) <= knapsack.capacity:  # if the knapsack can hold the object
            knapsack.add_object(obj)  # add the object to the knapsack
    return knapsack


def solve_knapsack_best(knapsack, objects_dict):
    objects_list = list(objects_dict.items())  # convert the dictionary to a list
    numItems = len(objects_list)  # number of items in the knapsack
    capacity = knapsack.capacity  # capacity of knapsack

# create an empty matrix
    matrix = np.zeros((numItems + 1, capacity + 1))  # rows represents items columns represents capacity

# loop through table rows
    for i in range(1, numItems + 1):
        # loop through table columns
        for w in range(1, capacity + 1):
            # if weight of the current item is less than the capacity
            if objects_list[i - 1][1][1] <= w:
                # worth of the matrix before the current item
                valueOne = np.float64(matrix[i - 1][w])
                # worth of the matrix after adding the current item
                valueTwo = np.float64(objects_list[i - 1][1][0] + matrix[i - 1][w - objects_list[i - 1][1][1]])
                # take maximum of either valueOne or valueTwo
                matrix[i][w] = int(max(valueOne, valueTwo))
            else:  # if weight of the current item is greater than the capacity
                matrix[i][w] = matrix[i - 1][w]
    checkItem(knapsack, numItems, capacity, objects_list, matrix)
    return knapsack


def checkItem(knapsack, numItems, capacity, objects_list, matrix):
    # When the numItemes or the = 0 the check is finished or if numItems or capacity = 0 at the begining then the check is unnecessary
    if numItems <= 0 or capacity <= 0:
        return knapsack
    # pick the content of the matrix at the current index
    pick = matrix[numItems][capacity]
    # if the pick is different than the content of the matrix at the previous index
    if pick != matrix[numItems - 1][capacity]:
        # add the item to the knapsack
        knapsack.add_object(objects_list[numItems - 1][0])
        # repeat with the new capacity and numItems
        checkItem(knapsack, numItems - 1, capacity - objects_list[numItems - 1][1][1], objects_list, matrix)
    else:
        # repeat with the new numItems
        checkItem(knapsack, numItems - 1, capacity, objects_list, matrix)


def solve_knapsack_optimal(knapsack, objects_dict):
    changedDictionary = objects_dict.copy()
    ListDictionary = list(changedDictionary.items())
    return knapsack_recursive(knapsack, objects_dict, ListDictionary, 0)


def knapsack_recursive(knapsack, objects_dict, objects_list, currentIndex):
    # if the knapsack is full or the current index is higher than len of objects_list
    if knapsack.capacity - knapsack.get_weight(objects_dict) <= 0 or currentIndex >= len(objects_list):
        return knapsack
    modifiedsack = knapsack.copy()
    untouchedsack = knapsack.copy()
    # if the knapsack can hold the current object
    if knapsack.get_weight(objects_dict) + objects_list[currentIndex][1][1] <= knapsack.capacity:
        modifiedsack.add_object(objects_list[currentIndex][0])
        modifiedsack = knapsack_recursive(modifiedsack, objects_dict, objects_list, currentIndex + 1)
    # otherwise
    untouchedsack = knapsack_recursive(untouchedsack, objects_dict, objects_list, currentIndex + 1)
    # return the knapsack with the highest value
    if modifiedsack.get_value(objects_dict) > untouchedsack.get_value(objects_dict):
        return modifiedsack
    return untouchedsack
