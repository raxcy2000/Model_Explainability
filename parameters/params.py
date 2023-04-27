import os

TITANIC_DATASET = "titanic.csv"

DATA_FOLDER = "data"
main_path = os.getcwd()

data_file_path = os.path.join(os.path.join(main_path, DATA_FOLDER), TITANIC_DATASET)


target_feat = "Survived"

# catboost_param = {'iterations':5000,
#         'learning_rate':0.01,
#         'cat_features':categorical_features,
#         'depth':3,
#         'eval_metric':'AUC',
#         'verbose':200,
#         'od_type':"Iter", # overfit detector
#         'od_wait':5000, # most recent best iteration to wait before stopping
#         'random_seed': 1
#           }