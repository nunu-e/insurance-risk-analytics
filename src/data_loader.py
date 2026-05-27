import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def load_data(path: str):
    """
    Robust data loader with basic error handling.
    """

    try:
        df = pd.read_csv(path)
        logging.info(f"Data loaded successfully with shape: {df.shape}")
        return df

    except FileNotFoundError:
        logging.error(f"File not found: {path}")
        raise

    except pd.errors.EmptyDataError:
        logging.error("File is empty")
        raise

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise