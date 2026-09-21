import random, sys

def val_input(prompt, minimum=0):
    for i in range(3):
        try:
            amt = int(input(prompt))
        except ValueError:
            print("Input must be a valid number: ")
        else:
            if amt >= minimum:
                return amt
            else:
                print(f"Amount has to be at least {minimum}.")
    else:
        print("Maximum tries exceeded.")
        sys.exit()

class BankInfo():

    def __init__(self):
        self.fn = input("First name: ")
        self.ln = input("Last name: ")
        self.gender = input("Gender: ")
        self.address = input("Address: ")

class BankAccount():

    def __init__(self):
        self.acno = random.randrange(10**12, 10**13)
        self.amount = val_input("\nAmount to deposit: ", self.min_amount)
        self.bank_info = BankInfo()
        self.interest = 0

class Savings(BankAccount):

    min_amount = 10000
    rate = 6
    
    def calculate(self, months):
        self.months = months
        self.interest = (self.amount * (1 + (self.rate/ 100)) ** (months / 12)) - self.amount
        return self.interest

class Current(BankAccount):

    min_amount = 5000
    rate = None
    
def display(acc, savings=True):

    print("\nACCOUNT INFORMATION\n")
    print(f"First name: {acc.bank_info.fn}")
    print(f"Last name: {acc.bank_info.ln}")
    print(f"Gender: {acc.bank_info.gender}")
    print(f"Address: {acc.bank_info.address}")
    print(f"Account Number: {acc.acno}")
    print(f"Amount: {acc.amount}")
    if savings:
        print(f"Months: {acc.months}")
        print(f"Rate of Interest: {acc.rate}%")
        print(f"Interest: {acc.interest}")

def main():

    acc_type = input("\nAccount Type (Savings/Current): ")

    if "s" in acc_type.lower():
        new_acc = Savings()
        months = val_input("\nMonths to calculate interest for: ")
        new_acc.calculate(months)
        display(new_acc)
    else:
        new_acc = Current()
        display(new_acc, False)

main()
