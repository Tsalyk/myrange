class Range:
    def __init__(self, start=None, step=None, limit=None):
        if step is None and limit is None:
            limit = start
            start = 0
            step = 1
        elif limit is None:
            limit = step
            step = 1

        self.__step = step
        self.__limit = limit
        self.__res = start - step

    def __next__(self):
        if self.__res + self.__step < self.__limit and self.__step > 0:
            self.__res += self.__step
        elif self.__res + self.__step > self.__limit and self.__step < 0:
            self.__res += self.__step
        else:
            raise StopIteration
        return self.__res

    def __iter__(self):
        return self