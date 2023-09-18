class Bank_Account:
  def __init__(self):
    Self.balance =0
    print("Hello!!!Welcome to the deposit & withdrawl machine")
  def deposit(self):
    amount=float(input("Enter amount to be Deposited:"))
    self.balance += amount
    print("\n Amount   Deposited:",amount)
  def withdraw(self):
    amount=float(input("Enter amount to be withdrawan:"))
if self.balance>=amount:
    self.balance-=amount
      print("\n you withdraw:",amount)
  else:
      print("\n Insufficient balance")
  def display(self):
    print("\n Net Avialable   Balance=",self.balance)
  S= Bank_Account()
  S.deposit()
  S.withdraw()
  S.display()
        