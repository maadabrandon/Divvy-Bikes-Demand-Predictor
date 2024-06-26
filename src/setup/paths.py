import os 
from pathlib import Path 


PARENT_DIR = Path("_file_").parent.resolve().parent.resolve().parent.resolve()

DATA_DIR = PARENT_DIR/"data"
RAW_DATA_DIR = DATA_DIR/"raw"
MODELS_DIR = PARENT_DIR/"models"
TEMPORARY_DATA = DATA_DIR/"temporary"

PARQUETS = RAW_DATA_DIR/"Parquets"

CLEANED_DATA = DATA_DIR/"cleaned"
TRANSFORMED_DATA = DATA_DIR/"transformed"
GEOGRAPHICAL_DATA = DATA_DIR/"geographical"

TIME_SERIES_DATA = TRANSFORMED_DATA/"time series"
TRAINING_DATA = TRANSFORMED_DATA/"training data"


def make_fundamental_paths() -> None:
    for path in [
        DATA_DIR, CLEANED_DATA, RAW_DATA_DIR, PARQUETS, GEOGRAPHICAL_DATA, TRANSFORMED_DATA, TIME_SERIES_DATA,
        TRAINING_DATA, MODELS_DIR
    ]: 
        if not Path(path).exists():
            os.mkdir(path)


if __name__ == "__main__":
    make_fundamental_paths()
    