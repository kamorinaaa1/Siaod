import heapq
import copy
import sys
from collections import deque

n = int(input('начальная вершина: '))
m = int(input('конечная вершина: '))

graph_from_txt_2 = []
file = open("матрица.txt")
arr = file.readlines()
for i in range(len(arr)):
    graph_from_txt_1 = []  # Инициализация пустого списка перед каждой итерацией
    arr[i] = arr[i].strip().split(" ")
    for j in arr[i]:
        el = int(j)
        graph_from_txt_1.append(el)
    graph_from_txt_2.append(graph_from_txt_1)
print(graph_from_txt_2)
graph = copy.deepcopy(graph_from_txt_2)


def floyd_warshall(graph, start, end):
    n = len(graph)
    distances = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                distances[i][j] = 0
            elif graph[i][j] != 0:
                distances[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances[start][end]


start_vertex = n
end_vertex = m
shortest_distance = floyd_warshall(graph, start_vertex, end_vertex)
print(f"1.Кратчайшее расстояние от вершины {start_vertex} до вершины {end_vertex}: {shortest_distance}")


def dijkstra(graph, start, end):
    distances = {vertex: float('inf') for vertex in range(len(graph))}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_vertex == end:
            break

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in range(len(graph[current_vertex])):
            if graph[current_vertex][neighbor] > 0:
                distance = current_distance + graph[current_vertex][neighbor]
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

    return distances[end]


start_vertex = n
end_vertex = m
shortest_distance = dijkstra(graph, start_vertex, end_vertex)

print(f"2.Кратчайшее расстояние от вершины {start_vertex} до вершины {end_vertex}: {shortest_distance}")


def bellman_ford(graph, start, end):
    n = len(graph)
    distances = [float('inf') for _ in range(n)]
    distances[start] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if graph[u][v] != 0:
                    if distances[u] + graph[u][v] < distances[v]:
                        distances[v] = distances[u] + graph[u][v]

    return distances[end]


start_vertex = n
end_vertex = m
shortest_distance = bellman_ford(graph, start_vertex, end_vertex)

print(f"3.Кратчайшее расстояние от вершины {start_vertex} до вершины {end_vertex}: {shortest_distance}")


def levit_algorithm(graph, start):
    n = len(graph)
    distance = [sys.maxsize] * n
    distance[start] = 0

    queue = deque([start])
    queue_set = set([start])

    while queue:
        v = queue.popleft()
        queue_set.remove(v)

        for u, weight in enumerate(graph[v]):
            if weight != 0 and distance[u] > distance[v] + weight:
                distance[u] = distance[v] + weight

                if u not in queue_set:
                    if weight == 0:
                        queue.appendleft(u)
                    else:
                        queue.append(u)
                    queue_set.add(u)

    return distance


start_vertex = n
end_vertex = m

shortest_path = levit_algorithm(graph, start_vertex)
print(f"5.Кратчайшее расстояние от вершины {start_vertex} до вершины {end_vertex}: {shortest_path[end_vertex]}")