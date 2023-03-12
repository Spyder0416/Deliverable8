import numpy as np

def populate_list(length):
    return np.random.randint(10, 51, length)

def sum_list_elements(lst):
    return sum(lst)

while True:
    try:
        n = int(input("Enter an integer number between 5 and 15: "))
        if n < 5 or n > 15:
            print("Error: Number is not between 5 and 15.")
            continue
    except ValueError:
        print("Error: The entered value is not a valid integer.")
        continue
    
    lst = populate_list(n)
    print("The elements of the list are:", end=" ")
    print(*lst)
    
    sum = sum_list_elements(lst)
    print("The sum is:", sum)
    
    break

