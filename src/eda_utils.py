import pandas as pd
def validate_data(df):
    """
    Basic data validation checks
    """

    assert df is not None, "Dataframe is None"
    assert len(df) > 0, "Dataset is empty"

    required_cols = ["TotalPremium", "TotalClaims"]

    for col in required_cols:
        assert col in df.columns, f"Missing column: {col}"

    return True