"""Splits a restaurant bill between the people at the table.

Amounts are in pence, so nothing is lost to rounding.
"""


def split_evenly(total, diners):
    """Each diner's share of the total, largest first.

    When the total does not divide exactly, the pennies left over go one
    each to the first diners, so the shares always add up to the total.
    """
    if diners < 1:
        raise ValueError("a bill needs at least one diner")
    share, left_over = divmod(total, diners)
    return [share + 1 if diner < left_over else share for diner in range(diners)]
