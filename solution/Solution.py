def solve_knapsack_greedy(knapsack, objects_dist):
    objects_dist1 = sorted(objects_dist.keys(), key=lambda item: (objects_dist[item][0]/objects_dist[item][1]), reverse=True)
    for obj in objects_dist1:
        if knapsack.get_value_and_weight(objects_dist)[1] + (objects_dist[obj][1]) <= knapsack.capacity:
            knapsack.content.append(obj)
    return knapsack
def solve_knapsack_best(knapsack, objects_dist):
    pass
def solve_knapsack_optimal(knapsack, objects_dist):
    pass