def is_pangram(s):
    sen = s.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for char in alpha:
        if char not in sen:
            return False
        
    return True 


x = input("type a sentence ")

if is_pangram(x):
    print("True")
else:
    print("false")

   
   


