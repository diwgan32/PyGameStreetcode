class T(tuple):
    def __new__(cls, *args):
        return tuple.__new__(cls, args)
    def __add__(self, other):
        return T(*([self._join(x) for x in zip(self, other)]))
    def __sub__(self, other):
        return self.__add__(-i for i in other)
    def _join(self, x):
    	return x[0] | x[1]

def rect_overlap(A, B):
    w = 0.5 * (A[2] + B[2]);
    h = 0.5 * (A[3] + B[3]);
    dx = A[0] - B[0];
    dy = A[1] - B[1];

    if (abs(dx) <= w and abs(dy) <= h):
    
        wy = w * dy;
        hx = h * dx;

        if (wy > hx):
            if (wy > -hx):
                return True
            else:
                return True
        else:
            if (wy > -hx):
                return True
            else:
                return True
    return False