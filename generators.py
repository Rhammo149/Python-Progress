#yield       generates a little bit of data at a time and not all at once (use for huge amounts of data)

    
def main():
    n =  int(input("whats n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "sheep" * i

if __name__ == "__main__":
    main()


