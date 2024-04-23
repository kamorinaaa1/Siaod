from collections import deque

def solve_puzzle(board):
    # Целевое состояние головоломки
    target_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

    # Преобразуем входной массив в кортеж для использования в качестве ключа в словаре
    start_state = tuple(board)

    # Создаем словарь для хранения предыдущих состояний и соответствующих им движений
    predecessors = {start_state: []}

    # Инициализируем очередь для поиска в ширину
    queue = deque([(start_state, [])])

    # Выполняем поиск в ширину
    while queue:
        state, moves = queue.popleft()

        # Если текущее состояние является целевым, возвращаем последовательность движений
        if list(state) == target_state:
            return moves

        # Найти индекс пустого поля (0)
        zero_index = state.index(0)

        # Рассмотреть все возможные движения
        for move in get_possible_moves(zero_index, len(board)):
            new_state = list(state)
            new_state[zero_index], new_state[move] = new_state[move], new_state[zero_index]
            new_state = tuple(new_state)


            # Если новое состояние еще не встречалось, добавить его в очередь и словарь
            if new_state not in predecessors:
                predecessors[new_state] = moves + [move + 1]
                queue.append((new_state, predecessors[new_state]))

    # Если решения нет, вернуть пустой массив
    return []

def get_possible_moves(zero_index, board_size):
    moves = []
    row, col = zero_index // 4, zero_index % 4

    # Проверяем движение вверх
    if row > 0:
        moves.append(zero_index - 4)

    # Проверяем движение вниз
    if row < 3:
        moves.append(zero_index + 4)

    # Проверяем движение влево
    if col > 0:
        moves.append(zero_index - 1)

    # Проверяем движение вправо
    if col < 3:
        moves.append(zero_index + 1)

    return moves

def print_board(board):
    for i in range(0, len(board), 4):
        row = board[i:i+4]
        print(row)

# Пример использования
puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 13, 14, 15, 12]
solution = solve_puzzle(puzzle)

if not solution:
    print("Решения нет")
else:
    print("Последовательность движений для решения головоломки:")
    current_state = puzzle
    print_board(current_state)
    print()

    for move in solution:
        zero_index = current_state.index(0)
        move_index = move - 1
        current_state[zero_index], current_state[move_index] = current_state[move_index], current_state[zero_index]
        print(f"Передвинуть элемент {move} на пустое место")
        print_board(current_state)
        print()