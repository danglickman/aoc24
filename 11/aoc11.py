import functools
import itertools

with open('input') as f:
    input = f.read().strip()

stones = list(map(int, input.split()))

BLINKS = 75

# 0 -> 1
# no_digits even -> split in half
# else: mult by 2024
@functools.lru_cache(maxsize=None)
def count_stones(stone, blinks):
    if blinks == 0:
        value = 1
    elif stone == 0:
        value = count_stones(1, blinks-1)
    elif (x := len(s := str(stone))) % 2 == 0:
        value = count_stones(int(s[:x // 2]), blinks - 1)
        value += count_stones(int(s[x // 2:]), blinks - 1)
    else:
        value = count_stones(stone * 2024, blinks - 1)
    return value

print(sum(count_stones(s, BLINKS) for s in stones))