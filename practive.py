def main():
    print(sum_even([1, 2, 3, 4, 22, 20, 5, 6]))


def sum_even(nums):
    even_sum = 0   
    for num in nums:
        if is_even(num):
            even_sum += num
    return even_sum

def is_even(n):
   return n % 2 == 0



main()
