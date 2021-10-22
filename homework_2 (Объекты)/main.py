class CustomList(list):
    def __init__(self, *args):
        super(CustomList, self).__init__(args[0])

    def _add(self, other):
        new_list = []
        for i in range(max(len(self), len(other))):
            if i < min(len(self), len(other)):
                new_list.append(self[i] + other[i])
            elif i >= len(self):
                new_list.append(other[i])
            elif i >= len(other):
                new_list.append(self[i])
        return self.__class__(new_list)

    def __radd__(self, other):
        return self._add(other)

    def __add__(self, other):
        return self._add(other)

    def _sub(self, other):
        # return self.__class__(*[item for item in self if item not in other])
        # print('sub')
        new_list = []
        for i in range(max(len(self), len(other))):
            if i < min(len(self), len(other)):
                new_list.append(self[i] - other[i])
            elif i >= len(self):
                new_list.append(- other[i])
            elif i >= len(other):
                new_list.append(self[i])
        return self.__class__(new_list)

    def __sub__(self, other):
        return self._sub(other)

    def __rsub__(self, other):
        return CustomList(other) - self

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)


if __name__ == '__main__':
    a = CustomList([1, 2, 3])
    b = CustomList([1, 4, 3])
    # print(a, b)
    # print(a + b)
    print(a - b)
    print(b - a)
    print([1, 3] - a)
    print(a - [1, 3])
    # print(a - [1, 2])
    # print([1, 2] + a)
    # print(type(a + b))
    print(a == b)
