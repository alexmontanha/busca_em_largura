from collections import deque

# Definindo o grafo com cidades e conexões (ignora custos neste caso)
graph = {
    'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
    'Zerind': ['Oradea', 'Arad'],
    'Oradea': ['Sibiu', 'Zerind'],
    'Timisoara': ['Lugoj', 'Arad'],
    'Lugoj': ['Mehadia', 'Timisoara'],
    'Mehadia': ['Drobeta', 'Lugoj'],
    'Drobeta': ['Craiova', 'Mehadia'],
    'Sibiu': ['Fagaras', 'Rimnicu Vilcea', 'Arad', 'Oradea'],
    'Rimnicu Vilcea': ['Pitesti', 'Craiova', 'Sibiu'],
    'Craiova': ['Pitesti', 'Drobeta', 'Rimnicu Vilcea'],
    'Fagaras': ['Bucareste', 'Sibiu'],
    'Pitesti': ['Bucareste', 'Rimnicu Vilcea', 'Craiova'],
    'Bucareste': ['Fagaras', 'Pitesti']
}

# Função que implementa a Busca em Largura (BFS)
def bfs(graph, start, goal):
    # Fila para armazenar os caminhos a serem explorados
    queue = deque([[start]])
    # Conjunto para armazenar as cidades já visitadas
    visited = set()

    while queue:
        # Remove o primeiro caminho da fila
        path = queue.popleft()
        # Última cidade visitada neste caminho
        city = path[-1]

        # Se a cidade atual for o destino, retorna o caminho
        if city == goal:
            return path

        # Se a cidade não foi visitada, explore seus vizinhos
        if city not in visited:
            visited.add(city)

            # Para cada cidade vizinha, crie um novo caminho e adicione à fila
            for neighbor in graph[city]:
                new_path = list(path)  # Cria uma cópia do caminho atual
                new_path.append(neighbor)
                queue.append(new_path)

    return None  # Retorna None se não houver caminho

# Exemplo de uso
start_city = 'Arad'
goal_city = 'Bucareste'

path = bfs(graph, start_city, goal_city)

if path:
    print(f"Caminho encontrado de {start_city} para {goal_city}: {' → '.join(path)}")
else:
    print(f"Não foi possível encontrar um caminho de {start_city} para {goal_city}")
