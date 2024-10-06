class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dic = defaultdict(int)
        for num in arr:
            if dic[-num%k] > 0:
                dic[-num%k] -= 1
            else:
                dic[num%k] += 1
        print(dic)        
        for key in dic:
            if dic[key]:
                return False            
                    
        return True   

        