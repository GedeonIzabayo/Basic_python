import pandas as pd

data = {
        "height": [1.5, 2.0, 1.2, 1.6],
        "sex": [0, 0, 1, 0],
        "age": [22, 53, 15, 26]
}

data_df = pd.DataFrame(data)
data_df