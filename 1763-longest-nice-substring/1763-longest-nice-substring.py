class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ''
        def divide_conquer(l,r):
            check_in = set(s[l:r])
            i = l
            while i < r:
                if s[i].lower() == s[i] and s[i].upper() not in check_in:
                    divide_conquer(l,i)
                    divide_conquer(i+1,r)
                    break 
                elif s[i].lower() not in check_in:   
                        divide_conquer(l,i)
                        divide_conquer(i+1,r)
                        break 
                i += 1 
            else:              
                nonlocal ans
                if r - l > len(ans):
                    ans = s[l:r]

        divide_conquer(0, len(s))
        return ans        


        