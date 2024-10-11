first_value = int(input("Enter first value: "))
second_value = int(input("Enter second value: "))

while not (first_value % 2 == 0 and second_value % 2 == 0):
    first_value = int(input("Enter first value: "))
    second_value = int(input("Enter second value: "))

print(first_value, second_value)