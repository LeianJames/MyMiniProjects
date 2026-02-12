def find_largest():
    a = int(input("Whats a? "))
    b = int(input("What's b? "))
    c = int(input("What's c? "))

    if a > b and a > c:
        largest = a

    elif b > a and b > c:
        largest = b

    else: 
        largest = c

    print(largest)