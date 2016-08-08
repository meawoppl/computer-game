import numpy as np


class Vector:
    def __init__(self, iterable):
        self._v = np.asarray(iterable, dtype=np.uint8)
        self._v[self._v > 0] = 1
        assert self._v.ndim == 1, "Only 1d for vectors"
        assert self._v.size >= 0, "Non zero length"

    def __and__(self, other):
        return Vector(self._v & other._v)

    def __eq__(self, other):
        return np.all(self._v == other._v)

    def __or__(self, other):
        return Vector(self._v | other._v)

    def __xor__(self, other):
        return Vector(self._v ^ other._v)

    def __neg__(self):
        return Vector(1 - self._v)

    # Proxy other methods down onto the array.
    def __getattr__(self, attr):
        return getattr(self._v, attr)

    def run(self):
        length = 0
        mx = 0
        for s in self._v:
            if s:
                length += 1
                mx = max(length, mx)
            else:
                length = 0

        return mx

    def compliment(self):
        return Vector(1 - self._v)

    def copy(self):
        return Vector(self._v.copy())


def random(length, probability):
    """Generate a Vector with length and binary probability given."""
    randomFloats = 1 - np.random.uniform(0, 1, size=length)
    return Vector(1 * (randomFloats < probability))


def ones(length):
    return Vector(np.ones((length)))


def zeros(length):
    return Vector(np.zeros((length)))
