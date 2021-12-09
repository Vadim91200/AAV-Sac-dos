def solve_knapsack_greedy(knapsack, objects_dist):
    objects_dist = sorting(objects_dist)
    for obj in objects_dist:
        if knapsack.get_value_and_weight(objects_dist)[1] + int(objects_dist[obj][1]) <= knapsack.capacity:
            knapsack.content.append(obj)
    return knapsack
def solve_knapsack_best(knapsack, objects_dist):
    pass
def solve_knapsack_optimal(knapsack, objects_dist):
    pass
def sorting(objects_dist):
    for name in objects_dist:
        for name2 in objects_dist:
            if objects_dist[name][0]/objects_dist[name][1] > objects_dist[name2][0]/objects_dist[name2][1]:
                objects_dist[name], objects_dist[name2] = objects_dist[name2], objects_dist[name]
    return objects_dist