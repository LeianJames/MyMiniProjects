<<<<<<< HEAD
#This program prints out squares 
# size = 3 -->  ###
#               ###
#               ###

def main():
    size = int(input("What's the size of the box? "))
    print_row(size)

def print_row(size):
    for i in range(size):
        print_square(size)

def print_square(size):
        print("#" * size)

=======
def main():
    size = int(input("What's the size of the box? "))
    print_row(size)

def print_row(size):
    for i in range(size):
        print_square(size)

def print_square(size):
        print("#" * size)

>>>>>>> 8d3122fedf6a1a153ba05f51605d207c37bda853
main()