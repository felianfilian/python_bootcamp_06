

def start():
    numbers = [1, 2, 3]

    new_numbers = [n + 1 for n in numbers]
    print(new_numbers)

    name = "mario"
    new_name = [letter for letter in name]
    print(new_name)

    new_num02 = [n * 2 for n in range(1, 5) if n < 3]
    print(new_num02)
