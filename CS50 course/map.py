#------------------- map
   
def main():
    yell("Hi", "you")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)
    

if __name__ == "__main__":
    main()

 