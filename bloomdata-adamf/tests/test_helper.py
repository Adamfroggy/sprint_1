import pandas as pd
from bloomdata_adamf.null_helper import null_count

def test_null_count():
    df = pd.DataFrame({
        'column_0': [None, 4, 3],
        'column_1': [9, None, None],
        'column_2': [10, 2, 2]
    })
    result = null_count(df)
    assert result == 3