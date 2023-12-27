import pandas as pd


def rm_outlier(df):

    data = df.values.tolist()

    def calculate_median(lst):
        n = len(lst)
        sorted_lst = sorted(lst)
        if n % 2 == 1:
            return sorted_lst[n // 2]
        else:
            mid1 = sorted_lst[n // 2 - 1]
            mid2 = sorted_lst[n // 2]
            return (mid1 + mid2) / 2

    q1_values = [calculate_median(col[:len(col)//2]) for col in data]
    q3_values = [calculate_median(col[(len(col)+1)//2:]) for col in data]

    iqr_values = [q3 - q1 for q1, q3 in zip(q1_values, q3_values)]

    lower_bounds = [q1 - 1.5 * iqr for q1, iqr in zip(q1_values, iqr_values)]
    upper_bounds = [q3 + 1.5 * iqr for q3, iqr in zip(q3_values, iqr_values)]

    cleaned_data = [
        [val if lower <= val <= upper else None for val,
            (lower, upper) in zip(row, zip(lower_bounds, upper_bounds))]
        for row in data
    ]

    cleaned_df = pd.DataFrame(cleaned_data, columns=df.columns)

    cleaned_df = cleaned_df.dropna()

    return cleaned_df
