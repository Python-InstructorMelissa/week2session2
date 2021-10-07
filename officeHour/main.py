"""
- make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
- display_user_balance(self) - have this method print the user's name and account balance to the terminal
eg. "User: Guido van Rossum, Balance: $150
- BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
"""

class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def makeDeposit(self, amount):
        self.balance += amount
        print(f"{self.name} made a deposit of ${amount}. New balance is ${self.balance}")

    def makeWithdrawal(self, amount):
        self.balance -= amount
        print(f"{self.name} made a Withdrawl of ${amount}. New balance is ${self.balance}")
        if self.balance < 0:
            print(f'{self.name}, you now have a negative balance please deposit money')
        else:
            print(f'Yay you still have money left')

    def displayBalance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")

    def transferMoney(self, user, amount):
        self.balance -= amount
        user.balance += amount
        print(f"{self.name} transferred ${amount} to {user.name}")
        self.displayBalance()
        user.displayBalance()

    def interestPayment(self, amount):
        self.balance += (self.balance * amount)
        print(f"{self.name} received a intrest payment.  New balance is ${self.balance}")

    def payBill(self, bill):
        self.balance -= bill.billTotal
        print(f"{bill.billName} was paid in the amount of ${bill.billTotal}.  {self.name} your balance is now ${self.balance}")

class Bill:
    def __init__(self, billName, billTotal):
        self.billName = billName
        self.billTotal = billTotal

janeDoe = User("Jane Doe")
johnSmith = User("John Smith")

janeDoe.displayBalance()
johnSmith.displayBalance()

janeDoe.makeDeposit(1000)
janeDoe.makeDeposit(50)
johnSmith.makeDeposit(100)

janeDoe.makeWithdrawal(100)

johnSmith.transferMoney(janeDoe, 50)

janeDoe.interestPayment(.01)
johnSmith.interestPayment(.01)

car = Bill("Car Payment", 300)
phone = Bill("Cell Phone", 100)
janeDoe.payBill(car)