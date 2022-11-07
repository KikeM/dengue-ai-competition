class Conventions:

    TARGET = "total_cases"
    INDICES = ["year", "weekofyear"]
    CITY = "city"
    WEEKOFYEAR = "weekofyear"
    WEEK_START_DATE = "week_start_date"
    YEAR = "year"


class Submission:

    COLS_SUBMISSION = [
        Conventions.CITY,
        Conventions.YEAR,
        Conventions.WEEKOFYEAR,
        Conventions.TARGET,
    ]
    CITIES = ["sj", "iq"]
