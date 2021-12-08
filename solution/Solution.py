def solve_knapsack_greedy(knapsack, objects_dist):
    objects_dist = sorted(objects_dist, key=lambda x: x[1]/x[0], reverse=True)
    for obj in objects_dist:
        if knapsack.get_value_and_weight(objects_dist)[1] + obj[1] <= knapsack.capacity:
            knapsack.content.append(obj)
    return knapsack.get_value_and_weight(objects_dist)
def solve_knapsack_best(knapsack, objects_dist):
    pass
def solve_knapsack_optimal(knapsack, objects_dist):
    pass
