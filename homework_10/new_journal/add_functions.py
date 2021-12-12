# Levenshtein distance
"""
            { i, если j == 0
D(i, j) =   { j, если i == 0
            { min(
            {    D(i, j - 1) + 1,
            {    D(i - 1, j) + 1,              если i != 0 и j != 0
            {    D(i - 1, j - 1) + m(i, j),
            {   )

где m - функция, которая равна 1 при неравенстве букв
        и равно 0 в остальных
"""


def distance_hard_release(a, b):
    def rec_dist(i, j):
        """Рекурсивная функция D(i, j)"""
        if i == 0 or j == 0:
            # если одна из строк пустая, то расстояние до другой строки - ее длина
            return max(i, j)
        else:
            # выбираем минимальное расстояние для трех разных случаев
            return min(
                rec_dist(i, j - 1) + 1,  # удаление
                rec_dist(i - 1, j) + 1,  # вставка
                rec_dist(i - 1, j - 1) + int(a[i - 1] != b[j - 1]),  # замена
            )

    return rec_dist(len(a), len(b))


def distance(a, b):
    """Алгоритм Вагнера-Фишера"""
    n, m = len(a), len(b)
    if n > m:
        # слово B (m букв) должно быть максимально (будущая столбец)
        a, b = b, a
        n, m = m, n

    # Сохраняем только текущую и предыдущую строки
    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add = previous_row[j] + 1
            delete = current_row[j - 1] + 1
            change = previous_row[j - 1] + int(a[j - 1] != b[i - 1])
            current_row[j] = min(add, delete, change)

    return current_row[n]


if __name__ == "__main__":
    print(distance('task', 'zasuk'))
    print(distance('task', 'task'))
