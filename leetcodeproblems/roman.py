class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {"I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
        }
       
        total = 0
        prev_val = 0
#------------------ use [  ] to get the value of the key from a dictionary
        for char in s:
            val = rom[char]
            if val > prev_val:
                total += val - 2 * prev_val
            else:
                total += val
            prev_val = val
        return total

s = Solution()
result = s.romanToInt("IV")
print(result)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}

        for i, n in enumerate(nums):
            diff = target - nums
            if diff in prevmap:
                return [prevmap[diff], i]    
            prevmap[n] = i
        return
    
    
            