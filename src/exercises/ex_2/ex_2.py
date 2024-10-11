import math

shapes = {
    "triangle_1": [(0, 0), (2, 5), (5, 4)],
    "triangle_2": [(2, 4), (4, 5), (2, 6)],
    "triangle_3": [(10, 1), (6, 3), (5, 0)]
}

output = {}

for key, points in shapes.items():
    perimeter = 0
    for i in range(len(points)):

        point_1 = points[i]

        if i != 2:
            point_2 = points[i + 1]
        else:
            point_2 = points[0]

        distance = math.sqrt((point_2[1] - point_1[1]) ** 2 + (point_2[0] - point_1[0]) ** 2)

        perimeter += distance

    output[key] = round(perimeter, 2)

print(output)