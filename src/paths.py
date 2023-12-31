from pathlib import Path 
import os 

PARENT_DIR = Path("_file_").parent.resolve().parent
DATA_DIR = PARENT_DIR/"data"
RAW_DATA_DIR = DATA_DIR/"raw"
MODELS_DIR = PARENT_DIR/"models"
TEMPORARY_DATA = DATA_DIR/"temporary"

PARQUETS = RAW_DATA_DIR/"Parquets"
ORIGINAL_DATA_TYPES = PARQUETS/"With Original Variable Types"
ALTERED_DATA_TYPES = PARQUETS/"With Altered Variable Types"


CLEANED_DATA = DATA_DIR/"cleaned"
TRANSFORMED_DATA = DATA_DIR/"transformed"
GEOGRAPHICAL_DATA = DATA_DIR/"geographical"


if not Path(DATA_DIR).exists():
    os.mkdir(DATA_DIR)

if not Path(RAW_DATA_DIR).exists():
    os.mkdir(RAW_DATA_DIR)

if not Path(TRANSFORMED_DATA).exists():
    os.mkdir(TRANSFORMED_DATA)
