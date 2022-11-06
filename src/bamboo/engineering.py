def shift_feature(col, data, shifts):
    """Create shifted features to analyse influence from the past.

    Parameters
    ----------
    col : str
    data : pandas.DataFrame
    shifts : int or iterable of ints
        Number of shifts to lookback into the past.

    Returns
    -------
    data : pandas.DataFrame
        With new columns including the shifted feature.
    """

    data = data.copy()

    if isinstance(shifts, int):
        shifts = range(1, shifts + 1)

    for shift in shifts:
        name = "_shift".join([col, str(shift)])
        data[name] = data[col].shift(shift)

    return data
