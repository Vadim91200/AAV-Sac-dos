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

  firstknapsack = knapsack.copy()
  secondknapsack = knapsack.copy()
  if knapsack.get_value_and_weight(objects_dict)[1] + objects_list[currentIndex][1][1] <= knapsack.capacity:
      firstknapsack.content.append(objects_list[currentIndex][0])
      firstknapsack = knapsack_recursive(firstknapsack, objects_dict, objects_list, currentIndex + 1)
  else:
      secondknapsack = knapsack_recursive(secondknapsack, objects_dict, objects_list, currentIndex + 1)

  if firstknapsack.get_value_and_weight(objects_dict)[0] > secondknapsack.get_value_and_weight(objects_dict)[0]:
      return firstknapsack
  else:
      return secondknapsack