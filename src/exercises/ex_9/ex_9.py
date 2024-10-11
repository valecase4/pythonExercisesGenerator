def my_function(a, b, c):
    try:
        int_list = [float(x) for x in (a, b, c)]
        print(int_list)
    except:
        raise ValueError("All parameters must be convertible to integer")
    
my_function("2", "3.5", 3.5)

my_function("Hello", 4.5, "2")