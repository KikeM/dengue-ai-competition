from pathlib import Path

import pandas as pd

from bamboo.conventions import Conventions, Submission
from bamboo.data_manager import DataManager
from bamboo.utils import remove_nonfeature_columns

HERE = Path(__file__)
PATH_SUMISSIONS = HERE.parents[2] / "submissions"


def create_submission(name: str, data_manager: DataManager, models: dict) -> None:
    """Create submission CSV file.

    Parameters
    ----------
    name : str
        Experiment name.
    data_manager : DataManager
        Data manager to access the test data.
    models : dict
        Dictionary containing the model for each city.
    """

    cities = Submission.CITIES
    submission = pd.DataFrame()
    for city in cities:
        estimator = models[city]
        test_data = data_manager.get_city_test_data(city=city)
        features_test, _ = remove_nonfeature_columns(data=test_data)

        prediction = pd.Series(
            estimator.predict(features_test),
            name=Conventions.TARGET,
            index=test_data.index,
        )

        _submission = pd.merge(
            left=test_data,
            right=prediction,
            left_index=True,
            right_index=True,
        )
        submission = pd.concat([submission, _submission], axis=0)

    # Enforce data type
    submission[Conventions.TARGET] = submission[Conventions.TARGET].astype(int)

    # Create name
    today = pd.to_datetime("today").date()
    filename = "_".join([str(today), name])
    filename += ".csv"

    submission[Submission.COLS_SUBMISSION].to_csv(
        PATH_SUMISSIONS / filename, index=False
    )

    return submission
