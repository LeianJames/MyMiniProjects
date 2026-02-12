def main():
    size = int(input("What's the size of the box? "))
    print_row(size)

def print_row(size):
    for i in range(size):
        print_square(size)

def print_square(size):
        print("#" * size)

main()