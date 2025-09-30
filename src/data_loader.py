import pandas as pd
import os

def load_weather_data(filepath: str = "data/raw/GlobalWeatherRepository.csv") -> pd.DataFrame:
    """
    Load the weather dataset from CSV.

    Parameters
    ----------
    filepath : str
        Path to the dataset (default: data/raw/GlobalWeatherRepository.csv)

    Returns
    -------
    pd.DataFrame
        Loaded DataFrame with datetime parsing for 'lastupdated'
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(
            f"Dataset not found at {filepath}. "
            "Make sure the file is placed inside data/raw/."
        )

    df = pd.read_csv(filepath)

    # Ensure 'lastupdated' column exists and is converted to datetime
    if "lastupdated" in df.columns:
        df["lastupdated"] = pd.to_datetime(df["lastupdated"], errors="coerce")
    else:
        raise KeyError("'lastupdated' column not found in dataset!")

    return df
