import pytest
import data_pipe


def test_sum_as_string():
    assert data_pipe.sum_as_string(1, 1) == "2"
