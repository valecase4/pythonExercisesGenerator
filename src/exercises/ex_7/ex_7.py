def reverse_dict(input_dict):
    items_list = list(input_dict.items())
    reversed_list = reversed(items_list)
    new_dict = dict(reversed_list)
    
    return new_dict

example = {"first_name": "John", "last_name": "Jackson", "age": 45, "languages": ["English", "Italian"]}

output = reverse_dict(example)

print(output)
