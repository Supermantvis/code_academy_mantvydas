Sales_Price = float(input('Enter sales price of house in US dollars: '))
Down_Payment =  float(input('Enter down payment as a percentage of Sales Price, e.g. 5 for 5%: '))
Loan_Amount = Sales_Price*(1-Down_Payment/100)
Mortgage_Type =  float(input('Enter mortgage type in years, e.g 15 for 15 years: '))
Loan_Term = int(12*Mortgage_Type)
Interest_Rate =  float(input('Enter loan interest rate as a percentage, e.g 4 for 4%: '))
Tax_Rate=float(input('Enter county tax rate: '))
Home_Insurance=float(input('Enter your yearly Homeowners Insurance: '))

Home_Ins=Home_Insurance/12
Tax_Amount= (Sales_Price*Tax_Rate)/12
R = 1 +(Interest_Rate)/(12*100)
X = Loan_Amount*(R**Loan_Term)*(1-R)/(1-R**Loan_Term)

Monthly_Interest = []
Monthly_Balance = []
for i in range(1,Loan_Term+1):
    Interest = Loan_Amount*(R-1)
    Loan_Amount = Loan_Amount - (X-Interest)
    Monthly_Interest.append(Interest)
    Monthly_Balance.append(Loan_Amount)

print(sum(Monthly_Interest))
print("\n")
print(sum(Monthly_Balance))