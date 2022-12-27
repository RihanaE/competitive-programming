class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #n1 is length of num1 where indexing start from 0
        #n2 is length of num1 where indexing start from 0
        diction={"0" :0 , "1":1 , "2" :2 , "3" :3, "4":4 , "5":5, "6" :6 ,"7":7 ,"8" :8 ,"9": 9}
        number1=self.converter(num1,diction)
        number2=self.converter(num2 , diction)
        
        return f"{number1*number2}"
        
        
    def converter(self, num, reference):
        result=0
        for i in num:
            result *=10
            result +=reference[i]
            
        return result
        
        