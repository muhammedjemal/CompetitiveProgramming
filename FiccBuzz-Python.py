class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        nums = []
        for x in range(1, n+1):

            if (x % 3 == 0) and (x % 5 == 0):
                nums.append("FizzBuzz")

            elif (x % 3==0) :
                nums.append("Fizz")

            elif (x % 5) == 0:
                nums.append("Buzz")

            else:
                nums.append(str(x))
        
        return nums
