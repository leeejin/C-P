#1번
class BankAcct:
    balance=0
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,balance):
        self.balance +=balance
    def withdraw(self):
        self.balance = self.balance-balance
        if self.balance-balance <0:
            return "인출 불가: 잔고가 부족함"
        
#2번
class Queue:
    queue=[]
    def __init__(self):
        queue=[]
    def addQueue(self,value):
        self.queue.append(value)
    def isEmpty(self):
        if queue==[]:
            return True
        else:
            return False
    def delQueue(self):
        rtn = self.queue[0]
        del self.queue[0]
        return rtn
