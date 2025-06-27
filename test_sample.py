# content of test_sample.py
import exo11


def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5


def test_exo11():
    assert exo11.est_premier(5)
    assert not exo11.est_premier(6)
    assert exo11.est_premier(7)
    assert not exo11.est_premier(8)
    assert not exo11.est_premier(9)
    assert not exo11.est_premier(33333333333333)
    assert not exo11.est_premier(10000000000)
    assert exo11.est_premier(9576890767)