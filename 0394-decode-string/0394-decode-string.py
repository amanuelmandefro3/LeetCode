class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s,ind, num):
            ans,j = [], ind
            while j < len(s) and  s[j] != ']':
                if s[j] == '[': 
                    j += 1
                elif s[j].isdigit():
                    num2 = j
                    while s[j].isdigit():  
                        j += 1 
                    last_idx, val = decode(s,j,int(s[num2:j]))
                    j =  last_idx +1
                    ans.extend(val)

                else:
                    ans.append(s[j])
                    j += 1
                  
            return j,ans*num

            

        # i, num = 0, ''
        # res = ''
        # while i < len(s):
        #     if s[i].isalpha():
        #         res += s[i]
        #     elif s[i] == '[':
        #         last_idx, ans = decode(s, i, num)
        #         res += ans
        #         i = last_idx + 1
        #     else:
        #         num = ''
        #         while s[i].isdigit():
        #             num += s[i]
        #             i += 1
        #         num = int(num) 

        _, res = decode(s, 0, 1)
        return ''.join(res) 


        