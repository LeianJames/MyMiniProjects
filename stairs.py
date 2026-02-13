def triangle():                               
    x = int(input("How tall? "))            # assume x = 5 
    for i in range(1, x+1):                 # range(1, 6) → values of i [1, 2, 3, 4, 5]
        for j in range(i):                  # When i = 1 → range(1) → runs 1 time    When i = 2 → range(2) → runs 2 times
            print("*", end="")
        print() 



def reverse_triangle():
    x = int(input("How tall? "))                # assume x = 5 
    for i in range(x):                          # range(5) → i = 0, 1, 2, 3, 4
        for j in range(x-1, i - 1, -1):         # the inner loop is range(4, -1, -1) --> values of j: [4, 3, 2, 1, 0]
            print("*", end="")
        print()



def pyramid():
    x = int(input("How tall? ")) 
            
 

#-------*           7 spaces | 1 star
#------***          6 spaces | 3 stars
#-----*****         5 spaces | 5 stars
#----*******        4 spaces | 7 stars
#---*********       3 spaces | 9 stars
#--***********      2 spaces | 11 stars