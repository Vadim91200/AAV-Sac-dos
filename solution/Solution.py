def solve_knapsack_greedy(knapsack, objects_dist):
    objects_dist1 = sorted(objects_dist.keys(), key=lambda item: (objects_dist[item][0]/objects_dist[item][1]), reverse=True)
    for obj in objects_dist1:
        if knapsack.get_value_and_weight(objects_dist)[1] + (objects_dist[obj][1]) <= knapsack.capacity:
            knapsack.content.append(obj)
    return knapsack

def solve_knapsack_best(knapsack, objects_dist):
    pass    
def solve_knapsack_optimal(knapsack, objects_dist):
    Dictionnairemodifier = objects_dist.copy()
    Dictionnairemodifier = list(Dictionnairemodifier.items())
    return knapsack_recursive(knapsack, objects_dist, Dictionnairemodifier, 0)

def knapsack_recursive(knapsack, objects_dict, objects_list, currentIndex):
  if knapsack.capacity - knapsack.get_value_and_weight(objects_dict)[1] <= 0 or currentIndex >= len(objects_list):
    return knapsack

  knapsack1 = knapsack.copy()
  knapsack2 = knapsack.copy()
  if knapsack.get_value_and_weight(objects_dict)[1] + objects_list[currentIndex][1][1] <= knapsack.capacity:
      knapsack1.content.append(objects_list[currentIndex][0])
      knapsack1 = knapsack_recursive(
    knapsack1, objects_dict, objects_list, currentIndex + 1)

  knapsack2 = knapsack_recursive(
    knapsack2, objects_dict, objects_list, currentIndex + 1)

  if knapsack1.get_value_and_weight(objects_dict)[0] > knapsack2.get_value_and_weight(objects_dict)[0]:
      return knapsack1
  return knapsack2