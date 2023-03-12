from VocabDic import python_dictionary


word = input("Enter a Python keyword to look up: ")

if word in python_dictionary:
    print(python_dictionary[word])
else:
    print("Sorry, the word you entered is not in the dictionary.")
    