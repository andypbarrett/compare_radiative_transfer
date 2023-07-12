"""Input-output functions"""

import pandas as pd

fish = 'cod'

def load_seaicert_output(filepath):
    """Reads output of seaicert into a pandas.Dataframe

    :filepath: path to file: str or pathlib.Path

    :returns: pandas.Dataframe
    """
    return pd.read_csv(filepath, index_col=0, parse_dates=True)