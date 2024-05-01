class Solution:
    def findComplement(self, num: int) -> int:
        b = bin(num)
        nums = [] 
        for i in range(len(b)):
            if i < 2:
                nums.append(b[i])
            else:
                if b[i] == '0':
                    nums.append('1')
                else:
                    nums.append('0')        

        nums =  ''.join(nums)
        


        return int(nums, 2)
        