
class CustomMeta(type):
    """Метакласс: в начале названий всех атрибутов и методов (кроме магических) добавляет префикс "custom_"""
    def __new__(cls, clsname, bases, dct):
        attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                attr[f'custom_{name}'] = val
            else:
                attr[name] = val

        return type.__new__(cls, clsname, bases, attr)


class CustomClass(metaclass=CustomMeta):
    """Класс"""
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100


inst = CustomClass()
print(inst.custom_x)
print(inst.val)
print(inst.custom_line())

# ERROR
# print(dir(inst))
# inst.x
# inst.line()
