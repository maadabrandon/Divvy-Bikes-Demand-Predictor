import random
import pickle
import pathlib

import numpy as np
import pandas as pd

from tqdm import tqdm


def view_memory_usage(
    data: pd.DataFrame,
    column: str
):
    """
    This function allows us to view the amount of memory being
    used by one or more columns of a given dataframe.
    """

    yield data[column].memory_usage(index=False, deep=True)


def change_column_data_type(
    data: pd.DataFrame,
    columns: list,
    to_format: str
):
    """
    This function changes the datatype of one or more columns of 
    a given dataframe.
    """

    data[columns] = data[columns].astype(to_format)


def save_dict(
    dictionary: dict,
    folder: pathlib.PosixPath,
    file_name: str
):
    """ 
    Save a dictionary (as a .pkl file) into a specified folder,
    and with a specified file name
    """

    with open(f"{folder}/{file_name}", "wb") as file:
        pickle.dump(dictionary, file)


def add_rounded_coordinates_to_dataframe(data: pd.DataFrame, decimal_places: int, scenario: str):
    """
    This function takes the latitude and longitude columns of a dataframe,
    rounds them down to a specified number of decimal places, and creates
    a new column for these.
    """

    new_lats = []
    new_longs = []

    latitudes = tqdm(
        iterable=data[f"{scenario}_lat"].values,
        desc="Working on latitudes"
    )

    longitudes = tqdm(
        iterable=data[f"{scenario}_lng"].values,
        desc="Working on longitudes"
    )

    for latitude in latitudes:
        new_lats.append(
            np.round(latitude, decimals=decimal_places)
        )

    for longitude in longitudes:
        new_longs.append(
            np.round(longitude, decimals=decimal_places)
        )

    # Insert the rounded latitudes into the dataframe
    data.insert(
        loc=data.shape[1],
        column=f"rounded_{scenario}_lat",
        value=pd.Series(new_lats),
        allow_duplicates=False
    )

    # Insert the rounded longitudes into the dataframe
    data.insert(
        loc=data.shape[1],
        column=f"rounded_{scenario}_lng",
        value=pd.Series(new_longs),
        allow_duplicates=False
    )


def add_column_of_rounded_points(data: pd.DataFrame, scenario: str):
    """Make a column which consists of points containing the rounded latitudes and longitudes."""

    points = list(
        zip(
            data[f"rounded_{scenario}_lat"], data[f"rounded_{scenario}_lng"]
        )
    )

    data.insert(
        loc=data.shape[1],
        column=f"rounded_{scenario}_points",
        value=pd.Series(points),
        allow_duplicates=False
    )


def make_new_station_ids(data: pd.DataFrame, scenario: str) -> dict:
    """
    This function makes a list of random numbers for each unique point, and 
    associates each point with a corresponding number. This effectively creates new 
    IDs for each location.
    """

    num_unique_points = len(
        data[f"rounded_{scenario}_points"].unique()
    )

    # Set a seed to ensure reproducibility. 
    random.seed(69)

    # Make a list of k values consisting of values taken from the population
    station_ids = random.sample(
        population=range(num_unique_points), 
        k=num_unique_points
    )

    # Make a dictionary of points
    points_and_new_ids = {}

    for point, value in tqdm(zip(data[f"rounded_{scenario}_points"].unique(), station_ids)):
        points_and_new_ids[point] = value

    return points_and_new_ids


# Form a column of said IDs (in the appropriate order)
def add_column_of_ids(
    data: pd.DataFrame,
    scenario: str,
    points_and_ids: dict
):
    
    """
    Take each point, and the ID which corresponds to it (within its dictionary),
    and put those IDs in the relevant dataframe (in a manner that matches each 
    point with its ID row-wise).
    """

    location_ids = [
        points_and_ids[point] for point in list(data.loc[:, f"rounded_{scenario}_points"]) if
        point in points_and_ids.keys()
    ]

    data.insert(
        loc=data.shape[1],
        column=f"{scenario}_station_id",
        value=pd.Series(location_ids),
        allow_duplicates=False
    )
