import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal

from bamboo.engineering import shift_feature


def test_shift_feature():

    index = list(range(5))
    data = pd.DataFrame(columns=["feat"], index=index, data=index)
    data = data.astype(float)

    data_shift = shift_feature(col="feat", data=data, shifts=3)

    expected = pd.DataFrame(
        {
            "feat": {0: 0, 1: 1, 2: 2, 3: 3, 4: 4},
            "feat_shift1": {0: np.nan, 1: 0.0, 2: 1.0, 3: 2.0, 4: 3.0},
            "feat_shift2": {0: np.nan, 1: np.nan, 2: 0.0, 3: 1.0, 4: 2.0},
            "feat_shift3": {0: np.nan, 1: np.nan, 2: np.nan, 3: 0.0, 4: 1.0},
        },
        dtype=float,
    )

    assert_frame_equal(expected, data_shift)
