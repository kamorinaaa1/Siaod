import random
import time

def func(m, n, limMin, limMax):
    mas = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            mas[i][j] = random.randint(limMin, limMax)
    return mas

user_m = int(input())
user_n = int(input())
user_min_limit = int(input())
user_max_limit = int(input())
mas= func(user_m, user_n, user_min_limit, user_max_limit)
for i in mas:
    print(i)