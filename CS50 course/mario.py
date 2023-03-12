def main():
    print_column(3)


#height means (3) in this case
def print_column(height):
    print("#\n" * height, end="")
main()




def main1():
    print_row(4)

def print_row(width):
    print("?" * width)
main1()



def main2():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)
        


main2()
