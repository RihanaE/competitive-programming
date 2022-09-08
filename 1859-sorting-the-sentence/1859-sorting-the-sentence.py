class Solution:
    def sortSentence(self, s: str) -> str:
        store=[]
        new=""
        for i in range(len(s)):
            if s[i] != " ":
                new= new + s[i]

            if s[i] == " " or i == len(s) - 1:
                store.append(new)
                new=""


        new_store=[]
        for i in range(len(store)+1):
            for j in range(len(store)):

                if str(i) in store[j]:
                    new_store.append(store[j])

        result=""


        for i in range(1,len(store)+1):
            result=result+new_store[i-1]

        results=""
        j=1
        for i in result:
            if j in range(1,len(store)+1) and str(j)==i:
                results=results+" "
                j+=1

            else:
                results=results+i

        return results.rstrip()

