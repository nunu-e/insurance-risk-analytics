from src.data_loader import load_data


def test_load_data():
    assert callable(load_data)
