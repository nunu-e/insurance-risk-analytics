import pandas as pd


def load_data(path):
    """
    Load insurance dataset
    """
    return pd.read_csv(path)
