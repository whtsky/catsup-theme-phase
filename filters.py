def day(date):
    """

    :param date: a typical post date in catsup.
     like `2012-12-21`
    :return: the day number.like `21`
    """

    return date[8:]


def month(date):
    """

    :param date: a typical post date in catsup.
     like `2012-12-21`
    :return: the month in English.like `Dec`
    """
    import datetime
    return datetime.date(2000, int(date[5:7]), 1).strftime('%b')


def year(date):
    """

    :param date: a typical post date in catsup.
     like `2012-12-21`
    :return: the year number.like `2012`
    """

    return date[:4]