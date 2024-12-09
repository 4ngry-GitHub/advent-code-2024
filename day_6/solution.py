import os

import pandas as pd  # noqa
import numpy as np

base_dir: str = os.path.abspath(os.path.dirname(__file__))

with open(f"{base_dir}/input_data.txt", "r") as file:
    data: str = file.read().splitlines()

blocked_position: str = "#"
cur_position: str = "^"

map_array: np.ndarray = np.array([list(row) for row in data])
guard_x, guard_y = np.where(map_array == cur_position)[1][0], np.where(map_array == cur_position)[0][0]  # start pos
directions: np.ndarray = np.array([(0, -1), (1, 0), (0, 1), (-1, 0)])  # * up, right, down, left
direction_idx: int = 0  # guard direction
visited: np.ndarray = np.zeros(map_array.shape, dtype=bool)  # visited positions

visited[guard_y, guard_x] = True  # start pos is visited by default
while True:
    next_x_pos, next_y_pos = (
        guard_x + directions[direction_idx, 0],
        guard_y + directions[direction_idx, 1],
    )

    if (
        next_x_pos < 0
        or next_x_pos >= map_array.shape[1]
        or next_y_pos < 0
        or next_y_pos >= map_array.shape[0]
    ):
        break

    if map_array[next_y_pos, next_x_pos] == blocked_position:
        direction_idx = (direction_idx + 1) % 4  # make right turn if next pos is blocked
    else:
        guard_x, guard_y = next_x_pos, next_y_pos
        visited[guard_y, guard_x] = True


print(f"The puzzle answer is: {np.sum(visited)}")
