class T(tuple):
    def __new__(cls, *args):
        return tuple.__new__(cls, args)
    def __add__(self, other):
        return T(*([self._join(x) for x in zip(self, other)]))
    def __sub__(self, other):
        return self.__add__(-i for i in other)
    def _join(self, x):
    	return x[0] | x[1]