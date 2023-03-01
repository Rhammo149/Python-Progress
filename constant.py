MEOWS = 3


for _ in range(MEOWS):
    print("meow")

class Cat():
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")
cat = Cat()
cat.meow()

#--------------------------------------------------- mypy constant.py,  type hints, """doc string"""

def meow(n: int):
    """
    Meow n times.
    :param n: number of times to mewo
    :type n: int
    :raise TypeError: if n is not an int
    """
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meow(number)


#------------------------------------------ -n 3   
import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows.py")




