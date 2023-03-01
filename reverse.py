def reverse_words(x):
    n = " ".join(x.split()[::-1])
    return n
 
x = "hello world"
reverse_words(x)

#splits one string into substrings
#it then defines each string as word and sees if it contains a digit
# it then filters the digits in numerical order and puts into a string
#it then returns as the correct order in a string with .join(words) 


def order(sentence):
    words = sentence.split()
    words.sort(key=lambda word: ''.join(filter(str.isdigit, word)))
    return " ".join(words)






#used lambda function so it tests each x(num) in numbers and returns true or false. 
#the filter function only filters out what returned true and puts that into a list
#it then prints out the new even_numbers list


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)  # Output: [2, 4, 6, 8, 10]


#------------- counts the persistence until number is one digit and returns the count
def persistence(n):
    number = n
    count = 0
    while number >= 10:
        digits = []
        while number > 0:
            digit = number % 10
            digits.append(digit)
            number //= 10
        product = digits[0]
        for digit in digits[1:]:
            product *= digit
        number = product
        count += 1
    return count

#---------- replacing certains stuff in arrays reordering odd numbers in accending order without effect the index of the even numbers
import numpy as np

def sort_array(source_array):
    source_array = np.array(source_array)  # Convert input to NumPy array
    ind = np.where(source_array % 2 != 0)
    sorted_arr = np.sort(source_array[ind])
    source_array[ind] = sorted_arr
    return source_array.tolist()  # Convert the result back to a list
