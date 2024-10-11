strings = ["hello", "computer", "programming", "python", "apple", "sun", "hello, world!"]

shortest = strings[0]
min_length = len(shortest)

for i in range(1, len(strings)):
    length = len(strings[i])
    if length < min_length:
        shortest = strings[i]
        min_length = length

print(shortest)