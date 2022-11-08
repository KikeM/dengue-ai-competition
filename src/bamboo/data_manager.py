from functools import cache, cached_property
from pathlib import Path

import pandas as pd

from bamboo.conventions import Conventions

HERE = Path(__file__)
PATH_DATA = HERE.parents[2] / "data"


class DataManager:

    PATH_TRAIN_FEATURES = Path(PATH_DATA / "dengue_features_train.csv")
    PATH_TRAIN_LABELS = Path(PATH_DATA / "dengue_labels_train.csv")
    PATH_TEST_FEATURES = Path(PATH_DATA / "dengue_features_test.csv")

    INDEX_COLS = ["city", "year", "weekofyear"]

    def __init__(self) -> None:

        self.train_features = pd.read_csv(self.PATH_TRAIN_FEATURES)
        self.train_labels = pd.read_csv(self.PATH_TRAIN_LABELS)
        self.test_features = pd.read_csv(self.PATH_TEST_FEATURES)

    @cached_property
    def cities(self):
        cities = self.train_features["city"].unique()
        return cities

    def describe_features(self):
        describe = self.train_features.describe().T
        return describe

    def describe_labels(self):
        describe = self.train_labels.describe().T
        return describe

    @cache
    def get_city_training_data(self, city):
        train_features = self.train_features.query(f"city=='{city}'")
        train_labels = self.train_labels.query(f"city=='{city}'")

        _check_dimension_pre = train_features.shape[0]

        training_data = pd.merge(
            left=train_features,
            right=train_labels,
            right_on=self.INDEX_COLS,
            left_on=self.INDEX_COLS,
        )

        # Check : information loss
        _check_dimension_post = training_data.shape[0]
        assert _check_dimension_pre == _check_dimension_post

        training_data = self.define_types(training_data)

        return training_data

    @cache
    def get_city_test_data(self, city):
        test_features = self.test_features.query(f"city=='{city}'")
        test_features = self.define_types(test_features)
        return test_features

    @staticmethod
    def define_types(data):
        data = data.copy()

        WEEK_START_DATE = Conventions.WEEK_START_DATE
        data[WEEK_START_DATE] = pd.to_datetime(data[WEEK_START_DATE], yearfirst=True)

        return data
