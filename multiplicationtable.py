#This function shows the multiplication table of numbers 1 through 10

def table():
    for i in range (1, 11):
        for j in range(1,11):
            k = i * j
            print(f"{i} x {j} = {k} \n" )

table()