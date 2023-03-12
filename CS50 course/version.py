def main():
    x = get_int("Whats x? ")
    print(f"x is {x}")




def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
        

main()


# Have to include else because if the input is not an integer, the unindented print will try to print out cat. and cat cant be defined because cat or x is not an integer
    
