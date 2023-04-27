import os

TITANIC_DATASET = "titanic.csv"

DATA_FOLDER = "data"
main_path = os.getcwd()

data_file_path = os.path.join(os.path.join(main_path, DATA_FOLDER), TITANIC_DATASET)


target_feat = "Survived"