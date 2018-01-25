import math
import heapq


class Node:
    def __init__(self, name, distance=math.inf, prev=None):
        self.name = name
        self.distance = distance
        self.prev = prev

    def __gt__(self, other):
        return self.distance > other.distance

    def __lt__(self, other):
        return self.distance < other.distance


def visit_node(node, conns):
    for conn in conns:
        if node in conn:
            source = conn.index(node)
            target = 1 - source
            if conn[target].distance > conn[source].distance + conn[2]:
                conn[target].distance = conn[source].distance + conn[2]
                conn[target].prev = conn[source]
    

def dijkstra(target, nodes, connections):
    backup = []
    for i in nodes:
        backup.append(i)
    while target in nodes:
        heapq.heapify(nodes)
        node = heapq.heappop(nodes)
        visit_node(node, connections)

    current = target.prev
    print("Go to", target.name)
    while current is not None:
        print("from", current.name)
        current = current.prev
        
    print("Total distance", target.distance)
            

conns = []
a = Node("a", 0) # This is the source 
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")

nodes = [a, b, c, d, e, f, g]

conns.append((a, b,  24))
conns.append((a, c,  71))
conns.append((b, e,  59))
conns.append((b, d, 103))
conns.append((c, e, 134))
conns.append((c, f, 101))
conns.append((c, g, 169))
conns.append((e, f, 65))
conns.append((f, g, 141))


dijkstra(f, nodes, conns)
