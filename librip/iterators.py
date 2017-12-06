class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.ignore_case = kwargs.get('ignore_case', False)
        self.__prev = None
        self.items = list(filter(self.__check_unique, items))
        self.len = len(self.items)
        self.ind = 0

    def __check_unique(self, x):
        if self.ignore_case:
            if type(x) == str and type(self.__prev) == str:
                if x.casefold() == self.__prev.casefold():
                    return False
                if x == self.__prev:
                    return False
            if x == self.__prev:
                return False
        else:
            if x == self.__prev:
                return False

        self.__prev = x
        return True

    def __next__(self):
        if self.ind == self.len:
            raise StopIteration

        self.ind += 1
        return self.items[self.ind - 1]

    def __iter__(self):
        return self

