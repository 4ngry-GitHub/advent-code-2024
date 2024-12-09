import os

import pandas as pd  # noqa

base_dir: str = os.path.abspath(os.path.dirname(__file__))

with open(f"{base_dir}/input_data.txt", "r") as file:
    raw_data: str = file.read().splitlines()


rules: list[str] = []  # * first part of input data
updates: list = []  # * second part

for line in raw_data:
    if line.strip():
        if "|" in line:
            rules.append(line)
        else:
            updates.append(list(map(int, line.split(","))))

df: pd.DataFrame = pd.DataFrame([line.split("|") for line in rules], columns=["x", "y"])
df["x"] = df["x"].astype(int)
df["y"] = df["y"].astype(int)


def is_valid_order(update: list) -> bool:
    # checking if an update list has a valid order according to rules
    for _, row in df.iterrows():
        if row["x"] in update and row["y"] in update:
            x_index = update.index(row["x"])
            y_index = update.index(row["y"])
            if x_index > y_index:
                return False
    return True


valid_updates: list = [update for update in updates if is_valid_order(update)]
middle_pages: list[int] = [update[len(update) // 2] for update in valid_updates]

print(f"The puzzle answer is: {sum(middle_pages)}")
