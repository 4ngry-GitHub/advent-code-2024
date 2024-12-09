import os

import pandas as pd  # noqa

base_dir: str = os.path.abspath(os.path.dirname(__file__))

with open(f"{base_dir}/input_data.txt", "r") as file:
    raw_data: str = file.read().splitlines()


df: pd.DataFrame = pd.DataFrame([list(i) for i in raw_data])
search_word: str = "XMAS"  # I kept the uppercase since input data is all uppercase
search_count: int = 0
search_directions: tuple = [(0, 1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]


def is_search_word(x: int, y: int, dx: int, dy: int) -> bool:
    # x - vertical pos, y - horizontal pos, dx - x direction, dy - y direction
    for i, char in enumerate(search_word):
        nx, ny = x + i * dx, y + i * dy
        if nx < 0 or ny < 0 or nx >= df.shape[0] or ny >= df.shape[1] or df.iloc[nx, ny] != char:
            return False
    return True


for x in range(df.shape[0]):
    for y in range(df.shape[1]):
        for dx, dy in search_directions:
            if is_search_word(x, y, dx, dy):
                search_count += 1

print(f"The puzzle answer is: {search_count}")
