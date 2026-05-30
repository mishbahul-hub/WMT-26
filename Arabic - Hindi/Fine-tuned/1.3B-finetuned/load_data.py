import pandas as pd
from datasets import Dataset

def load_data(file_path):
    df = pd.read_csv(file_path)
    print(f"Loaded : {len(df)} from filepath: {file_path}")
    df.head(5)
    train_ds = Dataset.from_pandas(df, preserve_index=False)
    print(f"Train: {len(train_ds)} ")
    return df, train_ds