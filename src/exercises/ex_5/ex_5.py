tuples = [(9, 3), (4, 5), (9, 9), (4, 2), (10, 2), (20, 3), (4, 1)]

even_tuples = []

for tuple in tuples:
    if tuple[0] % 2 == 0 and tuple[1] % 2 == 0:
        even_tuples.append(tuple)

max_value = 0
best_tuple = (None, None)

for tuple in even_tuples:
    if (tuple[0] + tuple[1]) > 0:
        best_tuple = tuple

print(tuple)