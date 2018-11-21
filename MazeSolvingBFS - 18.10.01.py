from collections import deque

#https://drive.google.com/open?id=1j7W-cX6dYOYzFOQwodKlMvOWaWNz3cIj

board = [
    [2, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 0, 1], 
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 3]
]

node_dict = {}
for i in range(10):
    for j in range(10):
        if board[i][j] != 0:
            node_dict[(i,j)] = (i,j)
            
#for node in list(node_dict):
    #print(node)


# Adjacency List:

neigh_dict = {}


for node in list(node_dict):
    neigh_dict[node] = []
    node_x, node_y = node_dict[node]
    
    for new_node in node_dict:
        
        new_node_x, new_node_y = node_dict[new_node]
        delta_x = abs(new_node_x - node_x)
        delta_y = abs(new_node_y - node_y) 

        if delta_x + delta_y == 1:
            neigh_dict[node].append(new_node)

#print('caminho entre', start, 'e', end)  
#print(bfs(start, end))

def bfs(start, end):
    queue = deque([start]) # fila de processamento []
    came_from = {} # mapeia 'node' em 'parent node' (algoritmo primeiro visitou 'parent node', e de lá visitou 'node' 
    came_from[start] = None # 'start' não possui 'parent node'
    
    while len(queue) > 0:
        node = queue.popleft() # retira 1o elemento da fila
        if node == end:
            path = find_path_between_nodes(start, end, came_from)
            return path # retorna caminho
        for neigh in neigh_dict[node]: # percorre todos os vizinhos de node
            if neigh not in came_from: # neigh não foi visitado
                came_from[neigh] = node # 'node' como pai de 'neigh'
                queue.append(neigh) # e adiciona neigh na fila
    return [] # não existe caminho entre start e end

def find_path_between_nodes(start, end, came_from):   
    rev_path = []
    node = end
    while node != start:
        rev_path.append(node)
        node = came_from[node]
    rev_path.append(start)
    rev_path.reverse()
    return rev_path


    
start = (0,0)
end = (9,9)

print('caminho entre', start, 'e', end)  
print(bfs(start, end))
