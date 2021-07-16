class Atm(object):
    def __init__(self,card_no,pin_no):
        self.card_no = card_no
        self.pin_no = pin_no
       
    def withdrawal(self):
        print("you requested for  withdrawal")
        
    def balance_enquiry(self):
        print("you are having insufficient balence")
        
    def deposit(self):
        print("you deposited the money")
    
        
atm1= Atm("123456","7891011")
print(atm1.card_no)
print(atm1.pin_no)
atm1.withdrawal()
atm1.balance_enquiry()
atm1.deposit()

        
