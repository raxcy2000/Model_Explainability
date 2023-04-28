import os

TITANIC_DATASET = "titanic.csv"
CALIFORNIA_DATASET = "california_housing_data.csv"
BOSTON_DATASET = "Boston_housing_dataset.csv"

DATA_FOLDER = "data"
main_path = os.getcwd()

data_file_path = os.path.join(os.path.join(main_path, DATA_FOLDER), TITANIC_DATASET)
cali_data_file_path = os.path.join(os.path.join(main_path, DATA_FOLDER), CALIFORNIA_DATASET)
boston_data_file_path = os.path.join(os.path.join(main_path, DATA_FOLDER), BOSTON_DATASET)


target_feat = "Survived"

