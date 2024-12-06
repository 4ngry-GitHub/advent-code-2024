import os

import pandas as pd
import numpy as np

base_dir: str = os.path.abspath(os.path.dirname(__file__))


with open(f"{base_dir}/input_data.txt", "r") as file:
    raw_data: list[str] = file.read().splitlines()
    processed_data: list = [[int(j) for j in i.split()] for i in raw_data]

df: pd.DataFrame = pd.DataFrame(processed_data)


def is_safe(row: pd.Series) -> bool:
    row = row.dropna()
    # validating for increasing or decreasing
    is_increasing: bool = all(row[i] < row[i + 1] for i in range(len(row) - 1))
    is_decreasing: bool = all(row[i] > row[i + 1] for i in range(len(row) - 1))

    # validating allowed distance range (1-3)
    is_valid_differences: bool = all(
        1 <= abs(row[i] - row[i + 1]) <= 3 for i in range(len(row) - 1)
    )

    return (is_increasing or is_decreasing) and is_valid_differences


df["is_safe"] = df.apply(is_safe, axis=1)
safe_report_count: np.int64 = df["is_safe"].sum()  # 148

print(f"The puzzle answer is: {safe_report_count}")
