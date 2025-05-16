import pytest

from src.pair_groups import group_pairs_by_sum


def test_valid_case():
    data = [6, 4, 12, 10]
    result = group_pairs_by_sum(data)
    assert 16 in result
    assert sorted(result[16]) == sorted([(6, 10), (4, 12)])


def test_no_duplicate_sums():
    data = [1, 2, 3]
    result = group_pairs_by_sum(data)
    assert result == {}


def test_short_input():
    with pytest.raises(ValueError):
        group_pairs_by_sum([5])
