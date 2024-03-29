import sys
import requests

import pandas as pd

from zipfile import ZipFile
from typing import Optional, List
from tqdm import tqdm

from src.setup.paths import RAW_DATA_DIR


def download_one_file_of_raw_data(
    year: int,
    month: Optional[int] = None,
    quarters: Optional[List[int]] = None,
    file_name: Optional[str] = None
):
    """
    In an earlier version of this project, I downloaded the data for 
    every year that Divvy has been in operation, resulting in the code below.
    I have since decided to restrict my training data to 2023's data. 
    
    I did this because it would take a massive amount of memory and time to handle the 
    creation of features and targets, let along the testing and training of machine learning models.    

    I have to delete the parts of this function that pertain to all the previous years, but I haven't had
    the heart to, because getting this working for every year was quite difficult.
    """

    if year == 2014:

        URL_1 = f"https://divvy-tripdata.s3.amazonaws.com/Divvy_Stations_Trips_{year}_Q{quarters[0]}Q{quarters[1]}.zip"
        URL_2 = f"https://divvy-tripdata.s3.amazonaws.com/Divvy_Stations_Trips_{year}_Q{quarters[2]}Q{quarters[3]}.zip"

        response_1 = requests.get(URL_1)
        response_2 = requests.get(URL_2)

        if response_1.status_code == 200:

            path = RAW_DATA_DIR / f"Divvy_Trips_{year}_Q1Q2.zip"
            open(path, "wb").write(response_1.content)

            with ZipFile(file=path, mode="r") as zip:
                zip.extractall(RAW_DATA_DIR / f"Divvy_Trips_{year}_Q1Q2")

        else:
            raise Exception(f"{URL_1} is not available")

        if response_2.status_code == 200:

            path = RAW_DATA_DIR / f"Divvy_Stations_Trips_{year}_Q3Q4.zip"
            open(path, "wb").write(response_2.content)

            with ZipFile(file=path, mode="r") as zip:
                zip.extractall(RAW_DATA_DIR)

        else:
            raise Exception(f"{URL_2} is not available")

    if year == 2015:

        if file_name == f"Divvy_Trips_{year}-Q1Q2":

            URL = f"https://divvy-tripdata.s3.amazonaws.com/{file_name}.zip"
            response = requests.get(URL)

            if response.status_code == 200:

                path = RAW_DATA_DIR / f"Divvy_Trips_{year}-Q1Q2.zip"
                open(path, "wb").write(response.content)

                with ZipFile(file=path, mode="r") as zip:
                    zip.extractall(RAW_DATA_DIR / f"Divvy_Trips_{year}-Q1Q2")

            else:
                raise Exception(f"{URL} is not available")

        elif file_name == f"Divvy_Trips_{year}_Q3Q4":

            URL = f"https://divvy-tripdata.s3.amazonaws.com/{file_name}.zip"
            response = requests.get(URL)

            if response.status_code == 200:

                path = RAW_DATA_DIR / f"Divvy_Trips_{year}_Q3Q4.zip"
                open(path, "wb").write(response.content)

                with ZipFile(file=path, mode="r") as zip:
                    zip.extractall(RAW_DATA_DIR / f"Divvy_Trips_{year}_Q3Q4")

            else:
                raise Exception(f"{URL} is not available")

    if year == 2016:

        if file_name == f"Divvy_Trips_{year}_Q1Q2":

            URL = f"https://divvy-tripdata.s3.amazonaws.com/{file_name}.zip"
            response = requests.get(URL)

            if response.status_code == 200:

                path = RAW_DATA_DIR / f"{file_name}zip"
                open(path, "wb").write(response.content)

                with ZipFile(file=path, mode="r") as zip:
                    zip.extractall(RAW_DATA_DIR / file_name)

            else:
                raise Exception(f"{URL} is not available")

        elif file_name == f"Divvy_Trips_{year}_Q3Q4":

            URL = f"https://divvy-tripdata.s3.amazonaws.com/{file_name}.zip"
            response = requests.get(URL)

            if response.status_code == 200:

                path = RAW_DATA_DIR / f"{file_name}.zip"
                open(path, "wb").write(response.content)

                with ZipFile(file=path, mode="r") as zip:
                    zip.extractall(RAW_DATA_DIR)

            else:
                raise Exception(f"{URL} is not available")

    if year == 2017:

        if file_name == f"Divvy_Trips_{year}_Q1Q2":

            URL = f"https://divvy-tripdata.s3.amazonaws.com/{file_name}.zip"
            response = requests.get(URL)

            if response.status_code == 200:

                path = RAW_DATA_DIR / f"Divvy_Trips_{year}_Q1Q2.zip"
                open(path, "wb").write(response.content)

                with ZipFile(file=path, mode="r") as zip:
                    zip.extractall(RAW_DATA_DIR / f"Divvy_Trips_{year}_Q1Q2")

            else:
                raise Exception(f"{URL} is not available")

        elif file_name == f"Divvy_Trips_{year}_Q3Q4":

            URL = f"https://divvy-tripdata.s3.amazonaws.com/{file_name}.zip"
            response = requests.get(URL)

            if response.status_code == 200:

                path = RAW_DATA_DIR / f"Divvy_Trips_{year}_Q3Q4.zip"
                open(path, "wb").write(response.content)

                with ZipFile(file=path, mode="r") as zip:
                    zip.extractall(RAW_DATA_DIR / f"Divvy_Trips_{year}_Q3Q4")

            else:
                raise Exception(f"{URL} is not available")

    if year in [2018, 2019]:

        for quarter in quarters:

            URL = f"https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_{year}_Q{quarter}.zip"

            response = requests.get(URL)

            if response.status_code == 200:
                path = RAW_DATA_DIR / f"Divvy_Trips_{year}_Q{quarter}.zip"
                open(path, "wb").write(response.content)

                with ZipFile(file=path, mode="r") as zip:
                    zip.extractall(RAW_DATA_DIR / f"Divvy_Trips_{year}_Q{quarter}")

            else:
                raise Exception(f"{URL} is not available")

    if year == 2020:

        if quarters == [1]:

            URL = f"https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_{year}_Q1.zip"
            response = requests.get(URL)

            if response.status_code == 200:

                path = RAW_DATA_DIR / f"Divvy_Trips_{year}_Q1.zip"
                open(path, "wb").write(response.content)

                with ZipFile(file=path, mode="r") as zip:
                    zip.extractall(RAW_DATA_DIR / f"Divvy_Trips_{year}_Q1")

            else:
                raise Exception(f"{URL} is not available")

        if month >= 4:

            URL = f"https://divvy-tripdata.s3.amazonaws.com/{year}{month:02d}-divvy-tripdata.zip"
            response = requests.get(URL)

            if response.status_code == 200:

                path = RAW_DATA_DIR / f"{year}{month}-divvy-tripdata.zip"
                open(path, "wb").write(response.content)

                with ZipFile(file=path, mode="r") as zip:
                    zip.extractall(RAW_DATA_DIR / f"{year}{month:02d}-divvy-tripdata")

            else:
                raise Exception(f"{URL} is not available")

    if year >= 2021:

        URL = f"https://divvy-tripdata.s3.amazonaws.com/{year}{month:02d}-divvy-tripdata.zip"

        response = requests.get(URL)

        if response.status_code == 200:
            path = RAW_DATA_DIR / f"{year}{month:02d}-divvy-tripdata.zip"
            open(path, "wb").write(response.content)

            with ZipFile(file=path, mode="r") as zip:
                zip.extractall(RAW_DATA_DIR / f"{year}{month:02d}-divvy-tripdata")

        else:
            raise Exception(f"{URL} is not available")


def check_for_file_and_download(
    year: int,
    file_name: str,
    quarters: Optional[List[int]] = None,
    month: Optional[List[int]] = None
):

    """This function checks for the presence of a file, and downloads 
    if it is not already available."""

    if quarters is not None:

        local_file = RAW_DATA_DIR / file_name

        if not local_file.exists():

            try:
                print(f"Downloading and extracting {file_name}.zip")

                # Download the file
                download_one_file_of_raw_data(year=year, file_name=file_name, quarters=quarters)

            except:
                print(f"{file_name} is not available")

        else:
            print(f"{file_name} is already in local storage")

    elif type(month) is int:

        local_file = RAW_DATA_DIR / f"{year}{month:02d}-divvy-tripdata"

        if not local_file.exists():

            try:
                print(f"Downloading and extracting {year}{month:02d}-divvy-tripdata.zip")

                # Download the file
                download_one_file_of_raw_data(year=year, month=month)

            except:
                print(f"{year}{month:02d}-divvy-tripdata is not available")

        else:
            print(f"The file {year}{month:02d}-divvy-tripdata.zip is already in local storage")


def get_dataframe_from_folder(
    year: int, 
    file_name: str
    ):

    """Takes the downloaded csv files and returns them as pandas dataframes."""

    data = pd.DataFrame()

    if year == 2014:

        if file_name == f"Divvy_Trips_{year}_Q1Q2":

            data_q1_q2 = pd.read_csv(RAW_DATA_DIR / f"{file_name}/{file_name}.csv")
            data = pd.concat([data, data_q1_q2])

            if data.empty:
                return pd.DataFrame()

            else:
                return data

        else:
            other_months = pd.read_csv(RAW_DATA_DIR / f"Divvy_Stations_Trips_2014_Q3Q4/{file_name}.csv")
            data = pd.concat([data, other_months])

            if data.empty:
                return pd.DataFrame()

            else:
                return data

    elif year == 2015:

        if file_name == f"Divvy_Trips_{year}-Q1Q2":

            for quarter in [1, 2]:
                quarter_data = pd.read_csv(RAW_DATA_DIR / f"{file_name}/Divvy_Trips_{year}-Q{quarter}.csv")
                data = pd.concat([data, quarter_data])

            if data.empty:
                return pd.DataFrame()

            else:
                return data

        elif file_name == f"Divvy_Trips_{year}_Q3Q4":

            for month in [7, 8, 9]:

                intermediate_month = pd.read_csv(
                    RAW_DATA_DIR / f"{file_name}/Divvy_Trips_{year}_{month:02d}.csv"
                )

                data = pd.concat([data, intermediate_month])

            last_quarter = pd.read_csv(
                RAW_DATA_DIR / f"{file_name}/Divvy_Trips_{year}_Q4.csv"
            )

            data = pd.concat([data, last_quarter])

            if data.empty:
                return pd.DataFrame()

            else:
                return data

    elif year == 2016:

        if file_name == f"Divvy_Trips_{year}_Q1Q2":

            first_quarter = pd.read_csv(RAW_DATA_DIR / f"{file_name}/Divvy_Trips_{year}_Q1.csv")

            for month in [4, 5, 6]:
                second_quarter_month = pd.read_csv(RAW_DATA_DIR / f"{file_name}/Divvy_Trips_{year}_{month:02d}.csv")
                data = pd.concat(
                    [data, first_quarter, second_quarter_month]
                )

            if data.empty:
                return pd.DataFrame()

            else:
                return data

        elif file_name == f"Divvy_Trips_{year}_Q3Q4":

            for quarter in [3, 4]:
                quarter_data = pd.read_csv(RAW_DATA_DIR / f"{file_name}/Divvy_Trips_{year}_Q{quarter}.csv")
                data = pd.concat([data, quarter_data])

            if data.empty:
                return pd.DataFrame()

            else:
                return data

    elif year == 2017:

        if file_name == f"Divvy_Trips_{year}_Q1Q2":

            for quarter in [1, 2]:
                quarter_data = pd.read_csv(RAW_DATA_DIR / f"{file_name}/Divvy_Trips_{year}_Q{quarter}.csv")
                data = pd.concat([data, quarter_data])

            if data.empty:
                return pd.DataFrame()

            else:
                return data

        if file_name == f"Divvy_Trips_{year}_Q3Q4":

            for quarter in [3, 4]:
                quarter_data = pd.read_csv(RAW_DATA_DIR / f"{file_name}/Divvy_Trips_{year}_Q{quarter}.csv")
                data = pd.concat([data, quarter_data])

            if data.empty:
                return pd.DataFrame()

            else:
                return data

    else:

        data_one_month = pd.read_csv(RAW_DATA_DIR / f"{file_name}/{file_name}.csv")
        data = pd.concat(
            [data, data_one_month]
        )

        if data.empty:
            return pd.DataFrame()

        
        return data


def load_raw_data(
        year: int,
        months: Optional[List[int]] = None,
        quarters: Optional[List[int]] = None
) -> pd.DataFrame:

    """
    First check for the presence of the data file (and download it if it is absent). 
    Load the downloaded data by 
    """

    if year == 2014:

        file_names_2014 = [
            f"Divvy_Trips_{year}_Q1Q2", f"Divvy_Trips_{year}-Q3-07", f"Divvy_Trips_{year}-Q3-0809",
            f"Divvy_Trips_{year}-Q4"
        ]

        for file_name in file_names_2014:

            # Download the relevant files and return the corresponding dataframes
            check_for_file_and_download(
                year=year, 
                file_name=file_name, 
                quarters=quarters
            )

            yield get_dataframe_from_folder(
                year=year, 
                file_name=file_name
            )

    if year == 2015:

        file_names_2015 = [
            f"Divvy_Trips_{year}-Q1Q2", f"Divvy_Trips_{year}_Q3Q4"
        ]

        for file_name in file_names_2015:
            check_for_file_and_download(year=year, file_name=file_name, quarters=[1])
            yield get_dataframe_from_folder(year=year, file_name=file_name)

    if year == 2016:

        # Download the relevant files
        check_for_file_and_download(
            year=year, 
            file_name=f"Divvy_Trips_{year}_Q1Q2", 
            quarters=[1, 2]
        )

        check_for_file_and_download(
            year=year, 
            file_name=f"Divvy_Trips_{year}_Q3Q4", 
            quarters=[3, 4]
        )

        file_names_2016 = [
            f"Divvy_Trips_{year}_Q1Q2", f"Divvy_Trips_{year}_Q3Q4"
        ]

        for file_name in tqdm(file_names_2016):
            yield get_dataframe_from_folder(year=year, file_name=file_name)

    if year == 2017:

        # Download the relevant files
        check_for_file_and_download(
            year=year, 
            file_name=f"Divvy_Trips_{year}_Q1Q2", 
            quarters=[1, 2]
        )

        check_for_file_and_download(
            year=year, 
            file_name=f"Divvy_Trips_{year}_Q3Q4", 
            quarters=[3, 4]
        )

        file_names_2017 = [
            f"Divvy_Trips_{year}_Q1Q2", f"Divvy_Trips_{year}_Q3Q4"
        ]

        for file_name in file_names_2017:
            yield get_dataframe_from_folder(year=year, file_name=file_name)

    if year in [2018, 2019]:

        for quarter in quarters:

            check_for_file_and_download(
                year=year, 
                file_name=f"Divvy_Trips_{year}_Q{quarter}", 
                quarters=[quarter]
            )

            yield get_dataframe_from_folder(
                year=year, 
                file_name=f"Divvy_Trips_{year}_Q{quarter}"
            )

    if year == 2020 and quarters == [1]:

        check_for_file_and_download(
            year=2020, 
            quarters=[1], 
            file_name=f"Divvy_Trips_{year}_Q1"
        )

        yield get_dataframe_from_folder(
            year=2020, 
            file_name=f"Divvy_Trips_{year}_Q1"
        )

    if year == 2020 and quarters is None:

        months = range(4, 13)

        for month in tqdm(months):

            check_for_file_and_download(
                year=year, 
                month=month, 
                file_name=f"{year}{month:02d}-divvy-tripdata"
            )

            yield get_dataframe_from_folder(
                year=year, 
                file_name=f"{year}{month:02d}-divvy-tripdata"
            )

    if year >= 2021:

        # Download the specified year's worth of data if no month is specified
        if months is None:

            months = range(1, 13)

            for month in months:

                check_for_file_and_download(
                    year=year, 
                    month=month, 
                    file_name=f"{year}{month:02d}-divvy-tripdata"
                )

                yield get_dataframe_from_folder(
                    year=year, 
                    file_name=f"{year}{month:02d}-divvy-tripdata"
                )


        # Download data for only the month specified by the integer "month"
        elif isinstance(months, list):

            for month in months:
                
                check_for_file_and_download(
                    year=year, 
                    month=month, 
                    file_name=f"{year}{month:02d}-divvy-tripdata"
                )

                yield get_dataframe_from_folder(
                    year=year, 
                    file_name=f"{year}{month:02d}-divvy-tripdata"
                )
