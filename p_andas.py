import pandas as pd

df = pd.DataFrame(
    [
        [1, "Math for Juniors", 3, False],
        [2, "Geometry in nature", 1, False],
        [3, "Just a chance", 1, True],
        [4, "Linear functions with fun", 5, True],
        [5, "About zero", 2, True],
        [6, "Logic for beginers", 3, False]
    ]
)

df.columns = ["ID", "Name", "Amount", "Promo"]

print(df)

print(df[["ID", "Amount"]])