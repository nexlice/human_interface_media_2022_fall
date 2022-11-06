import numpy as np

from src import correlation, three_channel_correlation


def test_correlation():
    image = np.asarray([
        [1, 2, 3],
        [4, 5, 6]
    ])
    patch = np.asarray([
        [10, 20],
        [30, 40]
    ])
    expected = np.asarray([
        10 + 40 + 120 + 200, 20 + 60 + 150 + 240
    ])
    result = correlation(image, patch)
    
    # assert >> raise exception when given condition is false.
    # np.allclose >> true if given two np arrays are close
    # https://numpy.org/doc/stable/reference/generated/numpy.allclose.html
    assert np.allclose(expected, result), "expected and result are not the same"

def test_three_channel_correlation():
    # TODO: implement this test
    ...
