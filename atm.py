class Account:
    def __init__(self,n,no,pin,bal):
        self.acc_name=n
        self.acc_num=no
        self.pin=pin
        self.balance=bal
    def pin_validation(self):
        return int(input("enter pin:"))==self.pin
    def disp_details(self):
        if (self.pin_validation()):
            print(" Acc holders Name:",self.acc_name)
            print(" Acc Number:",self.acc_num)
            print(" Acc Balance:", self.balance)
        else:
            print("invalid pin")
            exit()
    def add_money(self):
        if (self.pin_validation()):
            money_added=int(input("ammount"))
            self.balance+=money_added
            return self.balance
        else:
            print("invalid pin")
            exit()
    def withdraw(self):
        if (self.pin_validation()):
            money_drawn=int(input("ammount"))
            if money_drawn<self.balance:
                self.balance-=money_drawn
                return self.balance
            else:
                print("insufficient balace")
        else:
            print("invalid pin")
            exit()
    def change_pin(self):
        if (self.pin_validation()):
            self.pin=int(input("new pin"))
            print("pin changed")
        else:
            print("invalid pin")
            exit()
    def print_balance(self):
        print(" Acc Balance:", self.balance)


A2=Account("Nishant",2367413,9913,30000)
while True:
    choice=int(input("1=display 2=deposit 3=withdraw 4= change pin 5=exit"))
    if choice==1:
        A2.disp_details()
    elif choice==2:
        A2.add_money()
        A2.print_balance()
    elif choice==3:
        A2.withdraw()
        A2.print_balance()
    elif choice==4:
        A2.change_pin()
    elif choice==5:
        print("Thank you")
        exit()
    else:
        print("wrong input")
