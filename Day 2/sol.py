import os
os.chdir('C:/advent-of-code/Day 2')

def is_valid_sequence(seq):
    if len(seq) < 2:
        return True
    diff = seq[1] - seq[0]
    if abs(diff) < 1 or abs(diff) > 3:
        return False
    for i in range(2, len(seq)):
        if (seq[i] - seq[i-1]) * diff <= 0 or abs(seq[i] - seq[i-1]) < 1 or abs(seq[i] - seq[i-1]) > 3:
            return False
    return True

def is_safe_with_dampener(seq):
    if is_valid_sequence(seq):
        return True
    for i in range(len(seq)):
        if is_valid_sequence(seq[:i] + seq[i+1:]):
            return True
    return False

total = 0
with open("data.txt", "r") as my_file:
    for line in my_file:
        seq = list(map(int, line.split()))
        if is_safe_with_dampener(seq):
            total += 1

print(total)