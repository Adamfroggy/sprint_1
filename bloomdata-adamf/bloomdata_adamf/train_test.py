import pandas as pd

def train_test_split(df, frac=0.8, random_state=None):

    train_set = df.sample(frac=frac, random_state=random_state)

    test_set = df.drop(train_set.index)

    return train_set, test_set