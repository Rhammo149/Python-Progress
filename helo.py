while True:
    word = input(" Enter a word that is less than 10 characters")
    text = input("Enter a text that is less than 1000 characters")
    if len(word) > 10 or len(text) > 1000:
        print("You have exceeded the maximum length of characters for the typed word or text")
        
    else:
        break

words = text.split()
count = text.count(word)


print(count)
