class Knapsack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.content = []
    def get_value_and_weight(self, objects_dist):
        value = 0
        weight = 0
        for name in self.content:
            value += (objects_dist[name][0])
            weight += (objects_dist[name][1])
        return value, weight
    def print_content(self, objects_dist) -> None:
        for name in self.content:
            print(name,objects_dist[name][0], objects_dist[name][1])
        print("Le sac a ", len(self.content)," objets, pour une valeur de ", self.get_value_and_weight(objects_dist)[0] ," et un poids de ",self.get_value_and_weight(objects_dist)[1],"/",self.capacity, sep="")
