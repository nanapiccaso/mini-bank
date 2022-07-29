
class Bankaccount:

    clients=0
    account_number = 1000
    def __init__(self,name,phone,initial_deposit,password):

        self.name = name
        self.phone = phone
        self.account_bal = initial_deposit
        self.password = password
        self.client_acc_num = Bankaccount.account_number

        Bankaccount.clients = Bankaccount.clients + 1
        Bankaccount.account_number = Bankaccount.account_number + 1

    def client_details(self):
        print("user:"+ str(self.name) + "\taccount number :" + str(self.client_acc_num) +  "\t balance:" + str(self.account_bal) +".")


    def deposit (self):
        amount = int(input("enter amount to deposit :"))
        if amount <= 0 :
            print ("amount entered is invalid")
        else :
            self.account_bal = self.account_bal + amount
            print ("acount balance updated. current balance is" + str(self.account_bal) + ".")
  
    
    def withdraw (self):
        withdraw = int(input("enter amount to withdraw :"))
        if withdraw <= self.account_bal and withdraw > 0:
            self.account_bal = self.account_bal - withdraw
            print("account has been debited. current balance is" + str(self.account_bal) + ".")
        
        else :
            print ("invalid transaction")

    def make_payment(self,other):
        payment = int(input("enter amount to pay :"))
        if payment <= self.account_bal and payment> 0:
            self.account_bal = self.account_bal - payment
            other.account_bal = other.account_bal + payment
            print(" account has been debited. current balance is" + str(self.account_bal) + ".")
        else :
            print ("invalid transaction")

            

    




      
    

if __name__ == '__main__'  :  

    client1 = Bankaccount("kwame","0579824782",1000,"meek")
    client2 = Bankaccount("kwasi","0596551954",1200,"sark")
    
    print(client1.client_details())
    print(client2.client_details())
    #print("number of clients are :" + Bankaccount.clients + "." )
    #print(client1.deposit())
    #print(client1.client_details())
    #print(client1.withdraw())
    #print(client1.client_details())
    #print(client1.make_payment(client2))
    #print(client1.client_details())
    #print(client2.client_details())










        

