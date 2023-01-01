class Bank:

    def __init__(self, balance: List[int]):
        self.array_balance=balance
        self.length=len(self.array_balance)
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        
        if 0 <= (account1 - 1) < self.length and 0 <= (account2 - 1) < self.length and  money <= self.array_balance[account1 - 1]:
            self.array_balance[account2 - 1] +=money
            self.array_balance[account1 - 1] -=money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if 0 <= account - 1 < self.length:
            self.array_balance[account - 1] +=money
            return True
        else:
            return False
        

    def withdraw(self, account: int, money: int) -> bool:
        if 0 <= account - 1 < self.length and self.array_balance[account - 1] >= money:
            self.array_balance[account - 1] -=money
            return True
        else:
            return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)