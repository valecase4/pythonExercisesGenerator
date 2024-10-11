import math

points = {
    "A": (0, 0),
    "B": (9, 2),
    "C": (3, 4),
    "D": (1, 10),
    "E": (5, 6),
    "F": (4, 2)
}

max_length = 0
best_pair = (None, None)

for key, pair in points.items():
    for key_2, pair_2 in points.items():
        if key != key_2:
            distance = math.sqrt((pair[1] - pair_2[1]) ** 2 + (pair[0] - pair_2[0]) ** 2)

            print(key, key_2, distance)

            if distance > max_length:
                max_length = distance
                best_pair = (key, key_2)

print(best_pair)