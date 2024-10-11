input_list = [7, 1, 3, 10, 4, 19, 2, 3, 4]

smallest_value = input_list[0]

for x in input_list:
    if x < smallest_value:
        smallest_value = x

if smallest_value % 2 == 0:
    print(smallest_value)
else:
    print("The smallest value must be even in order to be printed.")