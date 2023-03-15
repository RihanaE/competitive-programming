class Solution:
    def decodeString(self, s: str) -> str:
        return self.helper(s, 0)
        
    def helper(self, s, pointer):
        if pointer == len(s):
            return ""
        
        else:
            n = 0
            store = ""
            while pointer != len(s):
                if s[pointer].isdigit():
                    n = (n * 10) + int(s[pointer])
                    pointer += 1

                elif s[pointer] == "[":
                    if n != 0:
                        store, pointer = store + n * self.helper(s, pointer + 1)[0], self.helper(s, pointer + 1)[1] 
                        n = 0
                        

                    else:
                        store, pointer = store + self.helper(s, pointer + 1)[0], self.helper(s, pointer + 1)[1] 
                        

                elif s[pointer] == "]":
                    pointer += 1
                    return store, pointer

                else:
                    store += s[pointer]
                    pointer += 1
                
            return store
        
#         left = 0
#         right = 0
#         string_ = ""
        
        
        
#         for i , ch in enumerate (s):
#             if ch == "[" :
#                 left = i
#                 string_ = ""
                
#             elif ch == "]":
#                 right = i
#                 break
                
#             else:
#                 string_ += ch
                
                
                
                
#         j = left - 1
#         num = ""
        
#         while s[j].isdigit() and j > -1:
#             num = s[j] + num
#             j -=1
            
        
#         string_ =s [: j + 1] + int(num) * string_ + s[right + 1:]
        
#         return self.decodeString(string_)