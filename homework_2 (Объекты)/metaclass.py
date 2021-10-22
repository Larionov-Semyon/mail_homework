
class CustomMeta(type):
    """Метакласс: в начале названий всех атрибутов и методов (кроме магических) добавляет префикс "custom_"""
    def __call__(cls, *args, **kwargs):
        print(dir(cls))
        call = type.__call__(cls, *args)
        setattr(cls, "hello", cls.x)
        return cls
        # return super(CustomMeta, cls).__init__(cls, name, bases, attr)

    # def __new__(cls, clsname, bases, dct):
    #     attr = {}
    #     for name, val in dct.items():
    #         if not name.startswith('__'):
    #             attr[f'custom_{name}'] = val
    #         else:
    #             attr[name] = val
    #
    #     print(attr, dct)
    #     return super().__new__(cls, clsname, bases, attr)
    #     # return super(CustomMeta, cls).__init__(cls, name, bases, attr)

    # def __init__(cls, name, bases, nmspc):
    #     print(f'MetaBase.__init__{nmspc.__init__}\n')
    #     attr = {}
    #     for name, val in nmspc.items():
    #         if not name.startswith('__'):
    #             attr[f'custom_{name}'] = val
    #         else:
    #             attr[name] = val
    #     # print(attr)
    #     return super().__init__(name, bases, attr)


class CustomClass(metaclass=CustomMeta):
    """Класс"""
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100


if __name__ == '__main__':
    inst = CustomClass()
    print(dir(inst))
    # print(inst.custom_x)
    # print(inst.custom_val)
    # print(inst.custom_line())
    # print(inst.val)

# ERROR
# print(dir(inst))
# inst.x
# inst.line()
