import counter
import pytest


def test_counter_inc():
    assert counter.inc(4) == 5


def test_counter_dec():
    assert counter.dec(5) == 4
