class Knapsack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.content = []
    def get_value_and_weight(self, objects_dist):
        value = 0
        weight = 0
        for obj in self.content:
            pass
        return value, weight
    def print_content(self, objects_dist) -> None:
        for name in self.content:
            print(name + " " + objects_dist[name][0] + " " + objects_dist[name][1])