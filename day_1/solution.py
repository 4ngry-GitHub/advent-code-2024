import os

import numpy as np

base_dir: str = os.path.abspath(os.path.dirname(__file__))

with open(f"{base_dir}/input_data.txt", "r") as file:
    # input data processing (loading into 2 sorted, casted to int arrays)
    raw_data: list[str] = file.read().splitlines()
    col_left: np.array = np.array(sorted([int(i.split()[0]) for i in raw_data]))
    col_right: np.array = np.array(sorted([int(i.split()[1]) for i in raw_data]))


total_distance: np.int64 = np.sum(np.abs(col_left - col_right))  # 2086478
print(f"Puzzle answer is: {total_distance}")
