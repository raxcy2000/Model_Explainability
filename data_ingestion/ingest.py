import pandas as pd

def get_data(f):
    """
    This is a function that takes a file path and read in data
    with pandas
    : f: filepath
    : df: resulting data
    """
    if f.endswith('.csv'):
        df = pd.read_csv(f)
    else:
        print("Can only read in '.csv' files")

    return df

def get_target_feature(data, target):
    target = data[target]
    features = data.drop(target, axis='columns')
    print(f"Shape of features is {features.shape}")
    print(f"Shape of target is {target.shape}")

    return features, target