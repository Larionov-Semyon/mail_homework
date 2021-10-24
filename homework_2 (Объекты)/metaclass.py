"""Создание метакласса для добавления префикса к методам и атрибутам"""


class CustomMeta(type):
    """Метакласс:
    в начале названий всех атрибутов и методов
    (кроме магических) добавляет префикс 'custom_'
    """

    def __new__(cls, key, bases, classdict):
        """Изменение названия атрибутов и методов класса"""
        # print('META NEW')
        new_dict = cls._add_prefix_custom(classdict)
        return super().__new__(cls, key, bases, new_dict)

    def __call__(cls, *args, **kwargs):
        """Изменение названия атрибутов экземпляра"""
        # print('META CALL')
        obj = type.__call__(cls, *args, **kwargs)
        obj.__dict__ = cls._add_prefix_custom(obj.__dict__)
        return obj

    @staticmethod
    def _add_prefix_custom(old_dict):
        """Функция добавления префикса"""
        new_dict = {}
        for key, val in old_dict.items():
            if key.startswith('__') and key.endswith('__'):
                new_dict[key] = val
            else:
                new_dict[f'custom_{key}'] = val
        return new_dict


class CustomClass(metaclass=CustomMeta):
    """Пробный класс"""
    x = 50

    def __init__(self, val=99):
        # print('CLASS INIT')
        self.val = val

    def line(self):
        """Test func line"""
        return 100

    def new_line(self):
        """Test func new line"""
        return self.custom_val + 100


if __name__ == '__main__':
    inst = CustomClass()
    # print(dir(inst))
    print('END --- ', [i for i in dir(inst) if not i.startswith('__')])
    print('custom_x', inst.custom_x)    # 50
    print('custom_line()', inst.custom_line())  # 100
    print('custom_val', inst.custom_val)    # 99
    print('custom_new_line', inst.custom_new_line()) # 199
    try:
        print(inst.val)
    except AttributeError:
        print('\nAttributeError: нет inst.val')

    # print(inst.x)
    # print(inst.val)
    # print(inst.custom_line())
    # print(inst.val)
