#!/usr/bin/python3
combinations = [
        f"{i}{j}\n" if i == 8 and j == 9 else f"{i}{j}, "
        for i in range(9)
        for j in range(i + 1, 10)
        ]
print("".join(combinations), end="")
