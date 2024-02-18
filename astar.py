import heapq

dict_hn = {'Arad': 336, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
           'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
           'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu': 193,
           'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}

dict_gn = {
    'Arad': dict(Zerind=75, Timisoara=118, Sibiu=140),
    'Bucharest': dict(Urziceni=85, Giurgiu=90, Pitesti=101, Fagaras=211),
    'Craiova': dict(Drobeta=120, Pitesti=138, Rimnicu=146),
    'Drobeta': dict(Mehadia=75, Craiova=120),
    'Eforie': dict(Hirsova=86),
    'Fagaras': dict(Sibiu=99, Bucharest=211),
    'Giurgiu': dict(Bucharest=90),
    'Hirsova': dict(Eforie=86, Urziceni=98),
    'Iasi': dict(Neamt=87, Vaslui=92),
    'Lugoj': dict(Mehadia=70, Timisoara=111),
    'Mehadia': dict(Lugoj=70, Drobeta=75),
    'Neamt': dict(Iasi=87),
    'Oradea': dict(Zerind=71, Sibiu=151),
    'Pitesti': dict(Rimnicu=97, Bucharest=101, Craiova=138),
    'Rimnicu': dict(Sibiu=80, Pitesti=97, Craiova=146),
    'Sibiu': dict(Rimnicu=80, Fagaras=99, Arad=140, Oradea=151),
    'Timisoara': dict(Lugoj=111, Arad=118),
    'Urziceni': dict(Bucharest=85, Hirsova=98, Vaslui=142),
    'Vaslui': dict(Iasi=92, Urziceni=142),
    'Zerind': dict(Oradea=71, Arad=75)
}

def a_star(start, goal, dict_hn, dict_gn):
    open_list = [(0, start)]
    g_values = {node: float('inf') for node in dict_hn}
    g_values[start] = 0
    parent_nodes = {}

    while open_list:
        f, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(parent_nodes, current)

        for neighbor, cost in dict_gn[current].items():
            tentative_g = g_values[current] + cost
            if tentative_g < g_values[neighbor]:
                g_values[neighbor] = tentative_g
                f_value = tentative_g + dict_hn[neighbor]
                heapq.heappush(open_list, (f_value, neighbor))
                parent_nodes[neighbor] = current
    return None

def reconstruct_path(parents, current):
    path = [current]
    while current in parents:
        current = parents[current]
        path.append(current)
    path.reverse()
    return path

start_node = 'Arad'
goal_node = 'Bucharest'

path = a_star(start_node, goal_node, dict_hn, dict_gn)
if path:
    print("Path found:", path)
else:
    print("Path not found.")