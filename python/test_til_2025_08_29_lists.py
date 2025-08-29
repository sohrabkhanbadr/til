from python.til_2025_08_29_lists import unique_items

def test_unique_items():
    assert set(unique_items([1, 2, 2, 3])) == {1, 2, 3}
    assert set(unique_items([])) == set()
    assert set(unique_items([5, 5, 5])) == {5}
