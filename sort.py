# Сортировка выбором.
# Берётся срез массива, в котором минимальный элемент переносят в самый левый угол,
# после чего срез уменьшается и цикл повторяется.
import random
import time
def func(m, n, limMin, limMax):
    mas = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            mas[i][j] = random.randint(limMin, limMax)
    return mas

m = int(input())
n = int(input())
min_limit = int(input())
max_limit = int(input())
mas = func(m, n, min_limit, max_limit)
start_time = time.time()
for i in mas:
    print(i)

print()
for i in range(m):
    for t in range(n):
        ind = t
        for j in range(t, n):
            if mas[i][j] < mas[i][ind]:
                ind = j
        mas[i][t], mas[i][ind] = mas[i][ind], mas[i][t]

for i in mas:
    print(i)
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))
# Сортировка вставкой.
import random
import time

def func(m, n, limMin, limMax):
    mas = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            mas[i][j] = random.randint(limMin, limMax)
    return mas

m = int(input())
n = int(input())
min_limit = int(input())
max_limit = int(input())
mas = func(m, n, min_limit, max_limit)
start_time = time.time()
for i in mas:
    print(i)
print()

for array in mas:
    for i in range(1, n):
        while i > 0 and array[i] < array[i - 1]:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
    print(array)

print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))
# Сортировка обменом. || Сортировка пузырьком.
import random
def func(m, n, limMin, limMax):
    mas = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            mas[i][j] = random.randint(limMin, limMax)
    return mas

m = int(input())
n = int(input())
min_limit = int(input())
max_limit = int(input())
mas = func(m, n, min_limit, max_limit)
start_time = time.time()
for i in mas:
    print(i)

print()
for i in range(m):
    for t in range(n):
        for j in range(n - 1):
            if (mas[i][j] > mas[i][j + 1]):
                mas[i][j], mas[i][j+1] = mas[i][j+1], mas[i][j]


for i in mas:
    print(i)
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))
# Сортировка Шелла.
import random
import math
def func(m, n, limMin, limMax):
    mas = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            mas[i][j] = random.randint(limMin, limMax)
    return mas

m = int(input())
n = int(input())
min_limit = int(input())
max_limit = int(input())
mas = func(m, n, min_limit, max_limit)
start_time = time.time()
for i in mas:
    print(i)

print()
for array in mas:
    k = int(math.log2(n))
    interval = 2**k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i] #сдвиг элементов массива на нужное расстояние
            j = i
            while j >= interval and array[j - interval] > temp: #происходит сравнение и сдвиг элементов для сортировки массива по принципу "разделяй и властвуй".
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k - 1
    print(array)
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))
# Быстрая сортировка.
import random
def func(m, n, limMin, limMax):
    mas = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            mas[i][j] = random.randint(limMin, limMax)
    return mas

m = int(input())
n = int(input())
min_limit = int(input())
max_limit = int(input())
mas = func(m, n, min_limit, max_limit)
start_time = time.time()
for i in mas:
    print(i)

print()

def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        q = random.choice(array)
        l = []
        m = []
        r = []
        for elem in array:
            if elem < q:
                l.append(elem)
            elif elem > q:
                r.append(elem)
            else:
                m.append(elem)
        return quickSort(l) + m + quickSort(r)

for array in mas:
    print(quickSort(array))

print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))
# Турнирная сортировка.
import random
def func(m, n, limMin, limMax):
    mas = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            mas[i][j] = random.randint(limMin, limMax)
    return mas

m = int(input())
n = int(input())
min_limit = int(input())
max_limit = int(input())
mas = func(m, n, min_limit, max_limit)
start_time = time.time()
for i in mas:
    print(i)
print()

def tournamentSort(arr):
    tree = [None] * 2 * len(arr)
    nodes = len(tree) // 2

    for i, v in enumerate(arr):
        tree[nodes + i] = (i, v)

    for j in range(nodes - 1, 0, -1):
        tree[j] = min(tree[2 * j], tree[2 * j + 1], key = lambda x: (x[1], x[0]))

    for i in range(nodes):
        min_i, min_v = tree[1]
        next_i = min_i + nodes
        while next_i > 1:
            tree[next_i] = (min_i, float('inf'))
            next_i //= 2

        arr[i] = min_v
        tree[min_i + nodes] = (min_i, float('inf'))

        for j in range(min_i + nodes, 1, -1):
            if j % 2 == 0:
                tree[j // 2] = min(tree[j], tree[j + 1], key=lambda x: (x[1], x[0]))
            else:
                tree[j // 2] = min(tree[j - 1], tree[j], key=lambda x: (x[1], x[0]))

    return arr


for array in mas:
    print(tournamentSort(array))
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))