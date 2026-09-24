class LimitExceededError(Exception):
    print

class ATM():

    def __init__(self):
        self.__withdrawals = 0
        self.__total = 0

    def inputAmount(self):

        self.__withdrawals += 1

        if self.__withdrawals  > self.maxWithdrawals:
            raise LimitExceededError(f"\nA maximum of {self.maxWithdrawals} withdrawals are allowed.")

        while True:
            try:
                amount = int(input("\nEnter the withdrawal amount: "))
                break
            except ValueError:
                print("Invalid value")

        if self.__total + amount > self.limit:
            raise LimitExceededError(f"\nThe withdrawal amount must not exceed {self.limit}.")
  
        else:
            self.__total += amount
            print("Transation Successful")

class HDFCBank(ATM):

    maxWithdrawals = 3
    limit = 20000

class AXISBank(ATM):

    maxWithdrawals = 5
    limit = 30000

bank = input("HDFC Bank or Axis Bank? :")
if "a" in bank.lower():
    acc = AXISBank()
else:
    acc = HDFCBank()

while True:
    acc.inputAmount()

    con = input("\nNext transaction? (y/n)")
    if "n" in con.lower():
        break
