class bank_accont:
    def __init__(self,account_number,account_name,IFSC,balance):
        self.account_number=account_number
        self.account_name=account_name
        self.IFSC=IFSC
        self.balance=balance
        
    def withdrawal_details(self,withdraw):
        self.witdraw=self.balance-withdraw
        return self.witdraw
    
    def compare_balance(self,other):
        print(self.balance- other.balance)
        
    
naveen=bank_accont(1234,'prakash','IOBA',500)
ammu=bank_accont(6789,'pallavi','SBIA',1000)

naveen.compare_balance(ammu)
