from bamboo.conventions import Conventions


def remove_nonfeature_columns(data):

    data = data.copy()
    cols = [
        Conventions.CITY,
        Conventions.YEAR,
        Conventions.WEEK_START_DATE,
    ]
    features = data.drop(columns=cols)
    if Conventions.TARGET in features.columns:
        target = features.pop(Conventions.TARGET)
    else:
        target = None

    return features, target
