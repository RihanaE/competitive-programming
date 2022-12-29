class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        diction={}
        
        for i in cpdomains:
            diction= self.separator(i,diction)
            
        result=[]
        for key,value in diction.items():
            result.append(f"{value} {key}")
            
        return result
    
# make a hash map for the domains by mapping the domain with the accessing time

    def separator(self,domain,store):
        num=""
        
        pointer=0
        
        # will separate the given number from the string
        
        while domain[pointer] != " ":
            num +=domain[pointer]
            pointer +=1
            
        pointer +=1
        right_pointer=len(domain) - 1
        
        while right_pointer >= 0:
            if domain[right_pointer] == "." and domain[right_pointer + 1:] not in store:
                store[domain[right_pointer + 1:]]=int(num)
                
            elif domain[right_pointer] == ".":
                store[domain[right_pointer + 1:]] +=int(num)
                
            elif domain[right_pointer] == " " and domain[right_pointer + 1:] not in store:
                store[domain[right_pointer + 1:]]=int(num)
                
            elif domain[right_pointer] == " " :
                store[domain[right_pointer + 1:]] +=int(num)
                
            right_pointer -=1
            
        return store