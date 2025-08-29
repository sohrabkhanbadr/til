from python.til_2025_08_30_dict_utils import merge_dicts

def test_merge_dicts():
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    result = merge_dicts(d1, d2)
    assert result == {"a": 1, "b": 3, "c": 4}
