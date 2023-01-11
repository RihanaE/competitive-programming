class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        store1 = num1.split("+")
        store2 = num2.split("+")
        length1 = len(store1[-1])
        length2 = len(store2[-1])
        store_mul = []
        
        store_mul.append(str(int(store1[0]) * int(store2[0])))
        store_mul.append(str(int(store1[0]) * int(store2[-1][:length2 - 1])) + "i")
        
        store_mul.append(str(int(store1[-1][:length1 - 1]) * int(store2[0])) + "i")
        store_mul.append(str(int(store1[-1][:length1 - 1]) * int(store2[-1][:length2 - 1]) * -1))
        
        no_i = 0
        no_r = 0
        
        for i in store_mul:
            if "i" in i:
                no_i += int(i[:len(i) - 1])
                
            else:
                no_r += int(i)
                
        result=str(no_r) + "+" + str(no_i) + "i"
        
        return result