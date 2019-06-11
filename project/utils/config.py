import json
from pandas.io.json import json_normalize
import warnings


def extract_json(url):
    """

    :param url: json location
    :return: pandas.core.frame.DataFrame
    """

    # JSON loading step

    with open(url) as f:
        json_init = json.load(f)
        j = json_normalize(json_init)
    return j


def df_formatting(df):
    """

    :param df: pandas.core.frame.DataFrame
    :return: pandas.core.frame.DataFrame
    """
    warnings.simplefilter(action='ignore', category=FutureWarning)
    filtered_df = df[['id', 'latitude', 'longitude']]
    numeric_df = filtered_df.convert_objects(convert_numeric=True)
    nonull_df = numeric_df[(~numeric_df.latitude.isnull()) & (~numeric_df.longitude.isnull())]
    final_df = nonull_df.reset_index(drop=True)
    return final_df
