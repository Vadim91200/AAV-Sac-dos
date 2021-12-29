import numpy as np
def solve_knapsack_greedy(knapsack, objects_dist):
    objects_dist1 = sorted(objects_dist.keys(), key=lambda item: (objects_dist[item][0]/objects_dist[item][1]), reverse=True) # objects_dist1 sort by value/weight ratio
    for obj in objects_dist1:
        if knapsack.get_value_and_weight(objects_dist)[1] + (objects_dist[obj][1]) <= knapsack.capacity: # if the knapsack can hold the object
            knapsack.content.append(obj) # add the object to the knapsack
    return knapsack

def solve_knapsack_best(knapsack, objects_dist):
    objects_list = list(objects_dist.items()) # convert the dictionary to a list
    numItems = len(objects_list) # number of items in the knapsack
    capacity = knapsack.capacity # capacity of knapsack

	# create an empty matrix
    matrix = np.zeros((numItems+1,capacity+1)) #rows representing items #columns representing capacity

	# loop through table rows
    for i in range(1,numItems+1):
        # loop through table columns
        for w in range(1,capacity+1):
			# if weight of the current item is less than the capacity
            if objects_list[i-1][1][1] <= w:
				# worth of the matrix before the current item
                valueOne = np.float64(matrix[i-1][w])
				# worth of the matrix after adding the current item 
                valueTwo = np.float64(objects_list[i-1][1][0] + matrix[i-1][w-objects_list[i-1][1][1]])
				# take maximum of either valueOne or valueTwo
                matrix[i][w] = int(max(valueOne, valueTwo))

            else: # if weight of the current item is greater than the capacity
                matrix[i][w] = matrix[i-1][w]
		
    checkItem(knapsack, numItems, capacity, objects_list, matrix)
    return knapsack
def checkItem(knapsack, numItems, capacity, objects_list, matrix):
    # When the numItemes = 0 the check is finished or if numItems or capacity = 0 then the check is unnecessary  
    if numItems <= 0 or capacity <= 0:
        return knapsack
    # pick the content of the matrix at the current index
    pick = matrix[numItems][capacity]
    # if the pick is different than the content of the matrix at the previous index
    if pick != matrix[numItems-1][capacity]:
        # add the item to the knapsack
        knapsack.content.append(objects_list[numItems-1][0])
        # repeat with the new capacity and numItems
        checkItem(knapsack, numItems-1, capacity-objects_list[numItems-1][1][1], objects_list, matrix)
    else:
        # repeat with the new numItems
        checkItem(knapsack, numItems-1, capacity, objects_list, matrix)
	
def solve_knapsack_optimal(knapsack, objects_dist):
    Dictionnairemodifier = objects_dist.copy()
    Dictionnairemodifier = list(Dictionnairemodifier.items())
    return knapsack_recursive(knapsack, objects_dist, Dictionnairemodifier, 0)

def knapsack_recursive(knapsack, objects_dict, objects_list, currentIndex):
    firstknapsack = knapsack.copy()
    secondknapsack = knapsack.copy()
    # if the knapsack is full or the current index is is higher than  len of objects_list
    if knapsack.capacity - knapsack.get_value_and_weight(objects_dict)[1] <= 0 or currentIndex >= len(objects_list):
        return knapsack
    # if the knapsack can hold the current object
    if knapsack.get_value_and_weight(objects_dict)[1] + objects_list[currentIndex][1][1] <= knapsack.capacity:
      firstknapsack.content.append(objects_list[currentIndex][0])
      firstknapsack = knapsack_recursive(firstknapsack, objects_dict, objects_list, currentIndex + 1)

    secondknapsack = knapsack_recursive(secondknapsack, objects_dict, objects_list, currentIndex + 1)
    # return the knapsack with the highest value
    if firstknapsack.get_value_and_weight(objects_dict)[0] > secondknapsack.get_value_and_weight(objects_dict)[0]:
        return firstknapsack
    return secondknapsack