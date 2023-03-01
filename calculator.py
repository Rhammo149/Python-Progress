x = float(input("What's x? "))
y = float(input("What's y? "))

z = (x / y)

#(f"{Variable:,}"") add a comma in numbers

print(f"{z:.2f}")


def square(n):
    return pow(n, 2) 


def main():
    x = int(input("Whats x? "))
    print("x squared is", square(x))

main()   