def get_number(prompt, conversion_type=float, minimum=0):
    while True:
        try:
            num = conversion_type(input(prompt))
        except ValueError:
            print("Invalid input, please try again.")
        else:
            if num < minimum:
                print(f"Value cannot be below {minimum}, please try again.")
            else:
                break
    return num
    
def get_income(months):
    salary = get_number("Monthly Salary: ")
    extra = get_number(f"Extra income over the {months} month period (if any): ")

    income = (salary * months) + extra
    return {
        "Salary": salary,
        "Extra": extra,
        "Income": income
        }

def get_expenses(months):
     rent = get_number("Monthly rent: ")
     utilities = get_number("Monthly utilities: ")
     groceries = get_number("Monthly groceries: ")
     transport = get_number("Monthly transport expense: ")
     misc = get_number(f"Other miscellaneous expenses during the {months} month period: ")

     total_expenses = (rent + utilities + groceries + transport) * months + misc
     return {
         "Rent": rent,
         "Utilities": utilities,
         "Groceries": groceries,
         "Transport": transport,
         "Miscellaneous": misc,
         "Total Expenses": total_expenses
         }

def calculate(income, expenses, affordability_threshold=20):
    savings = income - expenses
    pct_diff = 0
    affordability = False

    if income != 0:
        pct_diff = (savings / income) * 100

    if pct_diff >=  affordability_threshold:
        affordability = True
    return {
        "Savings": savings,
        "Percentage Saved/Lost": pct_diff,
        "Affordability": affordability
        }

def generate_report(income_data, expense_data, calculations):
    print("\n------------------------")
    print("PERSONAL FINANACE REPORT")
    print("------------------------")
    print("INCOME")
    print("------------------------")
    for k, v in income_data.items():
        print(f"{k}: {v}")
    print("------------------------")
    print("EXPENSES")
    print("------------------------")
    for k, v in expense_data.items():
        print(f"{k}: {v}")
    print("------------------------")
    print("FINANCIAL SUMMARY")
    print("------------------------")
    for k, v in calculations.items():
        print(f"{k}: {v}")
    print("------------------------")

months = get_number("Number of months to calculate for: ", int)
income_data = get_income(months)
expense_data = get_expenses(months)
calculations = calculate(income_data["Income"], expense_data["Total Expenses"])

generate_report(income_data, expense_data, calculations)

    


