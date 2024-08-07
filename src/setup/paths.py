import os 
from pathlib import Path 


PARENT_DIR = Path("_file_").parent.resolve()

DATA_DIR = PARENT_DIR/"data"
RAW_DATA_DIR = DATA_DIR/"raw"
MODELS_DIR = PARENT_DIR/"models"
LOCAL_SAVE_DIR = MODELS_DIR/"locally_created"
COMET_SAVE_DIR = MODELS_DIR/"comet_downloads"

PARQUETS = RAW_DATA_DIR/"Parquets"

CLEANED_DATA = DATA_DIR/"cleaned"
TRANSFORMED_DATA = DATA_DIR/"transformed"
GEOGRAPHICAL_DATA = DATA_DIR/"geographical"

INDEXER_ONE = GEOGRAPHICAL_DATA/"indexer_one"
INDEXER_TWO = GEOGRAPHICAL_DATA/"indexer_two"

TIME_SERIES_DATA = TRANSFORMED_DATA/"time series"
TRAINING_DATA = TRANSFORMED_DATA/"training data"
INFERENCE_DATA = TRANSFORMED_DATA/"inference"


def make_fundamental_paths() -> None:
    for path in [
        DATA_DIR, CLEANED_DATA, RAW_DATA_DIR, PARQUETS, GEOGRAPHICAL_DATA, TRANSFORMED_DATA, TIME_SERIES_DATA,
        TRAINING_DATA, INFERENCE_DATA, MODELS_DIR, LOCAL_SAVE_DIR, COMET_SAVE_DIR, INDEXER_ONE, INDEXER_TWO
    ]: 
        if not Path(path).exists():
            os.mkdir(path)


if __name__ == "__main__":
    os.chdir(PARENT_DIR)
    print(PARENT_DIR)
    