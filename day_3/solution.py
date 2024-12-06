import os
import re

base_dir: str = os.path.abspath(os.path.dirname(__file__))

with open(f"{base_dir}/input_data.txt", "r") as file:
    raw_data: str = file.read()


# creating regexp pattern and searching for matches
re_pattern: str = r"mul\((\d{1,3}),(\d{1,3})\)"
matches: list[tuple] = re.findall(re_pattern, raw_data)
total_sum: int = 0

for match in matches:
    x: int = int(match[0])
    y: int = int(match[1])
    total_sum += x * y

print(f"The puzzle answer is: {total_sum}")  # 173529487
