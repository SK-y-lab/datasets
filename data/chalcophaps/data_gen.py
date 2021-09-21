import random

import pandas as pd

random.seed(0)
rows = 30

df = pd.DataFrame(
    {
        "date": pd.date_range("20210901", periods=rows),
        "item": random.choices(["Apple", "Grape", "Orange"], k=rows, weights=[7, 5, 3]),
        "qty": [int(random.gammavariate(alpha=1, beta=2)) for _ in range(rows)],
    }
)

df = df.query("qty>0")

df.to_csv("sample.csv", index=None)
df.to_excel("sample.xlsx", index=None)
