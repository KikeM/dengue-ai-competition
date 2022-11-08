import numpy as np
import pandas as pd

from bamboo.cross_validation import TimeSeriesCrossValidation


def test_get_n_splits():
    N_SPLITS = 3
    cross_validation = TimeSeriesCrossValidation(
        n_splits=N_SPLITS,
        size_train=0.5,
        size_test=0.3,
        rnd_state=42,
    )

    num = 20
    index = list(range(num))
    cols = ["f1", "f2", "target"]
    data = np.linspace(0, 10, num).reshape(num, 1)
    data = np.hstack([data, np.linspace(11, 20, num).reshape(num, 1)])
    data = np.hstack([data, np.linspace(100, 200, num).reshape(num, 1)])

    training = pd.DataFrame(index=index, data=data, columns=cols)

    n_splits = cross_validation.get_n_splits(training)

    assert N_SPLITS == n_splits


def test_split():

    cross_validation = TimeSeriesCrossValidation(
        n_splits=3,
        size_train=0.5,
        size_test=0.3,
        rnd_state=42,
    )

    num = 20
    index = list(range(num))
    cols = ["f1", "f2", "target"]
    data = np.linspace(0, 10, num).reshape(num, 1)
    data = np.hstack([data, np.linspace(11, 20, num).reshape(num, 1)])
    data = np.hstack([data, np.linspace(100, 200, num).reshape(num, 1)])

    training = pd.DataFrame(index=index, data=data, columns=cols)

    indices = cross_validation.split(training)
    indices = list(indices)

    expected = [
        (
            pd.Index([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], dtype="int64"),
            pd.Index([12, 13, 14, 15, 16, 17], dtype="int64"),
        ),
        (
            pd.Index([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], dtype="int64"),
            pd.Index([13, 14, 15, 16, 17, 18], dtype="int64"),
        ),
        (
            pd.Index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype="int64"),
            pd.Index([10, 11, 12, 13, 14, 15], dtype="int64"),
        ),
    ]

    for batch_exp, batch_result in zip(expected, indices):
        for interval_exp, interval_result in zip(batch_exp, batch_result):
            assert all(interval_exp == interval_result)

    for idx_train, idx_test in cross_validation.split(training):
        print()
        print(training.loc[idx_train])
        print(training.loc[idx_test])
