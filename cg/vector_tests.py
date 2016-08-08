import numpy as np
from cg.vector import Vector, random, zeros, ones


v1 = random(100, 0.5)
zs = zeros(100)
os = ones(100)


def test_vec_eq():
    # test __eq__
    assert v1 == v1
    assert v1 == v1.copy()
    assert zs != os


def test_vec_or():
    assert (zs | v1) == v1
    assert (v1 | zs) == v1
    assert (v1 | v1) == v1
    assert (v1 | os) == os


def test_vec_xor():
    assert (zs ^ v1) == v1
    assert (v1 ^ v1) == zeros(100)


def test_vec_and():
    assert (zs & os) == zs
    assert (v1 & v1) == v1


def test_vec_neg():
    assert (-v1 | v1) == os
    assert (-v1 ^ v1) == os
    assert (-v1 & v1) == zs
    assert (-(-v1)) == v1


def test_run():
    a = Vector((0, 0, 0, 1, 1, 1, 1, 0, 0))
    assert a.run() == 4

    a = Vector(np.zeros(100))
    assert a.run() == 0

    a = Vector(np.ones(100))
    assert a.run() == 100

    a = Vector((0, 1, 0, 1, 1, 1, 1, 0, 0))
    assert a.run() == 4

    a = Vector(np.ones(100,))
    assert a.run() == 100


def test_random():
    for p in [0, 0.11, 0.5, 0.99, 1]:
        r = random(1000000, p)

        assert r.size == 1000000

        close = np.allclose(r.mean(), p, rtol=0.001, atol=0.001)
        assert close, "Test for %f failed. %f vs %f" % (p, r.mean(), p)


def test_vector_copy():
    r1 = random(100, 0.3)
    r2 = r1.copy()

    assert r1.sum() == r2.sum()
    assert r1.size == r2.size
    assert r1 == r2


def test_reverse():
    r = random(100, 0.5)
    assert r.sum() == r.reversed().sum()

    assert r.reversed().reversed() == r
