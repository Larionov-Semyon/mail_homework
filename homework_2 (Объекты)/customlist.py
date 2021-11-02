"""
    Кастомный класс списка
    - Можно вычитать из другого [5, 1, 3, 7] - [1, 2, 7] = [4, -1, -4, 7];
    - Можно складывать с другим [5, 1, 3, 7] + [1, 2, 7] = [6, 3, 10, 7];
    - При сравнении списков должна сравниваться сумма элементов списков;
"""


class CustomList(list):
    """Класс, отнаследованный от списка"""
    def __init__(self, *args):
        super().__init__(args[0])

    def __add__(self, other):
        new_list = []
        for i in range(max(len(self), len(other))):
            if i < min(len(self), len(other)):
                new_list.append(self[i] + other[i])
            elif i >= len(self):
                new_list.append(other[i])
            elif i >= len(other):
                new_list.append(self[i])
        return self.__class__(new_list)

    def __sub__(self, other):
        new_list = []
        for i in range(max(len(self), len(other))):
            if i < min(len(self), len(other)):
                new_list.append(self[i] - other[i])
            elif i >= len(self):
                new_list.append(- other[i])
            elif i >= len(other):
                new_list.append(self[i])
        return self.__class__(new_list)

    def __radd__(self, other):
        return CustomList(other) + self

    def __rsub__(self, other):
        return CustomList(other) - self

    def __eq__(self, other):
        """Равно =="""
        return sum(self) == sum(other)

    def __ne__(self, other):
        """Не равно !="""
        return sum(self) != sum(other)

    def __gt__(self, other):
        """Больше >"""
        return sum(self) > sum(other)

    def __lt__(self, other):
        """Меньше <"""
        return sum(self) < sum(other)

    def __ge__(self, other):
        """Больше или равно >="""
        return sum(self) >= sum(other)

    def __le__(self, other):
        """Меньше или равно <="""
        return sum(self) <= sum(other)


if __name__ == '__main__':
    a = CustomList([1, 2, 3])
    b = CustomList([1, 4, 3])
    # print(a, b)
    # print(a + b)
    print(a - b)
    print(b - a)
    print([1, 3] - a)
    print(type(a - [1, 3]))
    # print(a - [1, 2])
    # print([1, 2] + a)
    # print(type(a + b))
    print(a == b)
