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
    distances = [[float('inf') for _ in range(n)] for _ in range(n)]  # Создание матрицы расстояний dist размером n x n,
    # где n - количество вершин в графе. Изначально все элементы матрицы устанавливаются в бесконечность.

    for i in range(n):
        for j in range(n):
            if i == j:
                distances[i][j] = 0
            elif graph[i][j] != 0:
                distances[i][j] = graph[i][j]  #

    # проходимся ао всем вершинам к и обновляем матрицу дист
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])#проверка мин расстояние
                #с помощью к

    return distances[start][end]


start_vertex = n
end_vertex = m
shortest_distance = floyd_warshall(graph, start_vertex, end_vertex)

print(f"1.Кратчайшее расстояние от вершины {start_vertex} до вершины {end_vertex}: {shortest_distance}")


def dijkstra(graph, start, end):
    # Инициализация словаря расстояний с бесконечными значениями для всех вершин
    distances = {vertex: float('inf') for vertex in range(len(graph))}
    distances[start] = 0  # Расстояние от начальной вершины до самой себя равно 0

    # Очередь с приоритетами, содержащая пары (расстояние, вершина), начинаем с начальной вершины
    queue = [(0, start)]

    # Пока очередь не пуста, продолжаем обработку
    while queue:
        # Извлекаем вершину с наименьшим расстоянием до начальной вершины
        current_distance, current_vertex = heapq.heappop(queue)

        # Если текущая вершина является конечной, прерываем цикл
        if current_vertex == end:
            break

        # Если расстояние до текущей вершины больше уже известного, пропускаем её
        if current_distance > distances[current_vertex]:
            continue

        # Перебираем всех соседей текущей вершины
        for neighbor in range(len(graph[current_vertex])):
            # Если существует ребро между текущей вершиной и соседом
            if graph[current_vertex][neighbor] > 0:
                # Вычисляем расстояние до соседа через текущую вершину
                distance = current_distance + graph[current_vertex][neighbor]
                # Если новое расстояние меньше уже известного, обновляем его
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    # Добавляем соседа в очередь с приоритетами для дальнейшей обработки
                    heapq.heappush(queue, (distance, neighbor))

    # Возвращаем кратчайшее расстояние до конечной вершины
    return distances[end]



start_vertex = n
end_vertex = m
shortest_distance = dijkstra(graph, start_vertex, end_vertex)

print(f"2.Кратчайшее расстояние от вершины {start_vertex} до вершины {end_vertex}: {shortest_distance}")


def bellman_ford(graph, start, end):
    n = len(graph)  # Получаем количество вершин в графе
    distances = [float('inf') for _ in range(n)]  # Инициализируем список расстояний максимально возможными значениями
    distances[start] = 0  # Расстояние от начальной вершины до самой себя равно 0