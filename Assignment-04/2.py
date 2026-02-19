# floor plan 
floor_plan = [
    [0,0,1,0,0,1,1,1,1,1],
    [1,0,0,0,1,0,0,1,0,1],
    [1,0,1,0,1,0,1,1,0,1],
    [0,0,1,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,0,1,1,1,1,1]
]

start = (5, 1)   
goal = (1, 8)    

rows = len(floor_plan)
cols = len(floor_plan[0])


class Node:
    def __init__(self, position, parent=None, cost=0):
        self.position = position
        self.parent = parent
        self.cost = cost


class PriorityQueue:
    def __init__(self):
        self.data = []

    def push(self, node, priority):
        self.data.append((priority, node))
        self.data.sort(key=lambda x: x[0])

    def pop(self):
        return self.data.pop(0)[1]

    def empty(self):
        return len(self.data) == 0

def heuristic(pos):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])


def best_first_search():

    frontier = PriorityQueue()
    start_node = Node(start)

    frontier.push(start_node, heuristic(start))

    visited = set()

    while not frontier.empty():
        
        current = frontier.pop()

        # goal 
        if current.position == goal:
            return current

        visited.add(current.position)

        x, y = current.position

        # allowed
        moves = [(-1,0), (1,0), (0,-1), (0,1)]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if floor_plan[nx][ny] == 0 and (nx, ny) not in visited:
                    child = Node((nx, ny), current, current.cost + 1)
                    priority = heuristic(child.position)
                    frontier.push(child, priority)
    return None

def print_path(node):
    path = []
    while node:
        path.append(node.position)
        node = node.parent
    return path[::-1]

# main
solution = best_first_search()

print("Evacuation Path:")
print(print_path(solution))
print("Total steps:", solution.cost)
