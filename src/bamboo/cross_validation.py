import numpy as np


class TimeSeriesCrossValidation:
    def __init__(
        self,
        n_splits: int,
        size_train: float,
        size_test: float,
        rnd_state=None,
    ) -> None:
        """Cross validation for timeseries problems.

        Generates adjacent training and test datasets, to avoid
        breaking time dependence.

        Parameters
        ----------
        n_splits : int
            Number of splits to create.
        size_train : float
            Float between [0,1].
        size_test : float
            Float between [0,1].
        rnd_state : int, optional
            Random state, by default None
        """
        self.n_splits = n_splits
        self.size_train = size_train
        self.size_test = size_test
        self.rnd_state = rnd_state

    def get_n_splits(self, X=None, y=None, groups=None):
        return self.n_splits

    def split(self, X, y=None, groups=None):
        """Split data into consecutive train/test folds.

        Parameters
        ----------
        data : pandas.DataFrame or pandas.Series

        Yields
        ------
        train_index : pandas.Index
        test_index : pandas.Index
        """
        length = X.shape[0]
        index_data = X.index

        # Find latest training start
        length_train = int(np.ceil(self.size_train * length))
        length_test = int(np.ceil(self.size_test * length))
        left = length_test + length_train
        right = length - left

        assert (
            right >= self.n_splits
        ), "Sizes and splits do not conform. Reduce number of splits or decrease batch sizes!"

        random = np.random.RandomState(self.rnd_state)
        indices_train = [
            random.randint(low=0, high=right) for _ in range(self.n_splits)
        ]

        for index in indices_train:
            end_train = index + length_train
            train_index = index_data[index:end_train].values
            test_index = index_data[end_train : end_train + length_test].values
            yield train_index, test_index
