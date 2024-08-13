class User(object):
    def __init__(self,
                 id,
                 name,
                 email,
                 phone,
                 account,):
        self.id = id
        self,name = name
        self.email = email
        self.phone = phone
        self.account = account
                
        
class Bankaccount(object):
    def __init__(self,
        amount = 0,
        min_balance = 0,):
        
        self.min_balance = min_balance
        self.amount = amount

