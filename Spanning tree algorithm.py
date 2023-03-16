#Mateo Ruiz Davila
#00212195

import heapq

#Se crea elnodo
class Node:
    def __init__(self, node_id, is_switch):
        self.node_id = node_id
        self.is_switch = is_switch
    
    def __eq__(self, other):
        return self.node_id == other.node_id
    
    def __hash__(self):
        return hash(self.node_id)

#Se define el grafo
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = dict()
        
    def add_node(self, node_id, is_switch):
        node = Node(node_id, is_switch)
        self.nodes.add(node)
        self.edges[node] = set()
    
    def add_edge(self, u_id, v_id):
        u = Node(u_id, False)
        v = Node(v_id, False)
        if u not in self.nodes or v not in self.nodes:
            return False
        self.edges[u].add(v)
        self.edges[v].add(u)
        return True

#Se inicializa el algoritmo
def spanning_tree(graph, start_node):
    #Iniciacion de variables 
    mst = {}
    visited = set()
    heap = [(0, start_node)]
    heapq.heapify(heap)
        
    # loop until heap is empty
    while heap:
        # Obtiene el edge mas pequeno 
        weight, node = heapq.heappop(heap)
            
        # Checa si los nodos ya fueron vistados antes
        if node in visited:
                continue
            
        # Marca los nodos vistados y agrega un edge al minimum spanning tree
        visited.add(node)
        if node != start_node:
            mst[(node, parent)] = weight
            
        # Agregra los edges adjacentes al heap
        for adj_node, adj_weight in graph[node].items():
            if adj_node not in visited:
                heapq.heappush(heap, (adj_weight, adj_node))
                    
        # Actualiza al nodo padre
        parent = node
        
    # Calcula el peso total del minimum spanning tree
    tree_weight = sum(weight for weight in mst.values())
        
    # retorna el minimum spanning tree y su peso
    return mst, tree_weight


def main():
    # creacion del grafo
    graph = {
        'A': {'B': 1, 'C': 2},
        'B': {'A': 1, 'C': 3, 'D': 1},
        'C': {'A': 2, 'B': 3, 'D': 1},
        'D': {'B': 1, 'C': 1}
    }
    
    # Calcula el minimum spanning tree
    tree_edges, tree_weight = spanning_tree(graph, 'A')
    
    # Imprime minimum spanning tree
    print("Minimum Spanning Tree Edges:")
    for edge, weight in tree_edges.items():
        print(f"{edge[0]} -- {edge[1]}: {weight}")
    
    print(f"Minimum Spanning Tree Weight: {tree_weight}")
    
if __name__ == '__main__':
    main()
