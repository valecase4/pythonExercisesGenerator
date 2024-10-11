people = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "is_student": False,
        "address": {
            "street": "123 Elm St",
            "city": "Springfield",
            "zip_code": "62704"
        },
        "languages": ["English", "Spanish", "French"]
    },
    {
        "first_name": "Jane",
        "last_name": "Smith",
        "age": 25,
        "is_student": True,
        "address": {
            "street": "456 Oak St",
            "city": "Greenville",
            "zip_code": "70809"
        },
        "languages": ["English", "German"]
    },
    {
        "first_name": "Emily",
        "last_name": "Johnson",
        "age": 40,
        "is_student": False,
        "address": {
            "street": "789 Pine St",
            "city": "Fairview",
            "zip_code": "90210"
        },
        "languages": ["English", "Italian", "Mandarin"]
    },
    {
        "first_name": "Michael",
        "last_name": "Brown",
        "age": 35,
        "is_student": False,
        "address": {
            "street": "101 Maple St",
            "city": "Lakeside",
            "zip_code": "30318"
        },
        "languages": ["English", "Portuguese"]
    },
    {
        "first_name": "Sarah",
        "last_name": "Davis",
        "age": 28,
        "is_student": True,
        "address": {
            "street": "202 Cedar St",
            "city": "Brookhaven",
            "zip_code": "11235"
        },
        "languages": ["English", "Japanese", "Korean"]
    }
]

age_sum = 0
italian_speakers = 0

for person in people:
    age_sum += person["age"]

    if "Italian" in person["languages"]:
        italian_speakers += 1

how_many_people = len(people)

average_age = round(age_sum / how_many_people, 2)

print(average_age)

print(f"People who speak Italian: {italian_speakers}")
