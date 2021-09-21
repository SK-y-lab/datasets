import random

import pandas as pd

random.seed(0)
date = pd.date_range("20210901", "20210930", freq="H")
rows = len(date)

df = pd.DataFrame(
    {
        "date": date,
        "store": random.choices(["Tokyo", "Osaka"], k=rows, weights=[7, 5]),
        "item": random.choices(["Apple", "Grape", "Orange"], k=rows, weights=[7, 5, 3]),
        "qty": [int(random.gammavariate(alpha=1, beta=2)) for _ in range(rows)],
    }
)

df = df.query("qty > 0")

df.to_csv("sample.csv", index=None)
