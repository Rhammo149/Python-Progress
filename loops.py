
i = 0
while i < 3:
    print("meow")
    i += 1
#use underscore if the variable isnt going to be used again as good habit
for _ in range(3):
    print("meow")

#end="" means to not make a new line after print
print("meow\n" * 3, end="")

while True:
    n = int(input("Whats n? "))
    if n > 0:
        break
for _ in range(n):
    print("meow")


def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("whats n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
