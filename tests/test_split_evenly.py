"""A diner splits a bill evenly."""

import pytest

from bill_splitter import split_evenly


def test_the_bill_divides_exactly():
    assert split_evenly(6000, 3) == [2000, 2000, 2000]


def test_the_bill_leaves_pennies_over():
    shares = split_evenly(1000, 3)

    assert shares == [334, 333, 333]
    assert sum(shares) == 1000


def test_a_bill_needs_someone_to_pay_it():
    with pytest.raises(ValueError):
        split_evenly(1000, 0)
