from math import ceil


property_price = 0
down_payment = 0
loan_period = 0
interest_rate = 0

print("Welcome to Najeep Mortgage Calculator :3")
#Prompt user for property price
while True:
    try:
        property_price = int(input("Please enter property price: "))
    except ValueError:
        print("Sorry, must be a positive number la cibai")
        continue

    if property_price < 0:
        print("Sorry, must be positive number :=)")
        continue
    else:
        break

#Prompt user for down payment amount
while True:
    try:
        down_payment = int(input("Please enter down payment amount: "))
    except ValueError:
        print("Sorry, must be a positive number la cibai")
        continue

    if down_payment < 0:
        print("Sorry, must be positive number :=)")
        continue
    else:
        break

#Prompt user for loan period
while True:
    try:
        loan_period = int(input("Please enter loan period (years): "))
    except ValueError:
        print("Sorry, must be a positive number la cibai")
        continue

    if loan_period < 0:
        print("Sorry, must be positive number :=)")
        continue
    else:
        break

#Prompt user for down payment amount
while True:
    try:
        interest_rate = float(input("Please enter interest rate: "))
    except ValueError:
        print("Sorry, must be a positive number la cibai")
        continue

    if interest_rate < float(0):
        print("Sorry, must be positive number :=)")
        continue
    else:
        break

#Calculate monthly mortgage
principal_loan = property_price - down_payment
p = principal_loan
#Monthly interest rate
r = (interest_rate/100) / 12
#Number of payments over the loan's lifetime
n = loan_period * 12

Mortgage = (p * ((r * (1+r)**n) / ((1+r)**n - 1)))
Mortgage_2_deci = round(Mortgage, 2)


def amortization_schedule(Mortgage, p, interest_rate, loan_period):
    outstanding_principal = p
    rate_in_decimal = (interest_rate/100) / 12
    print("This is your yearly amortization table")
    for (year) in range(1, loan_period+1):
        if outstanding_principal > 1069.47:
            annual_principal = 0
            annual_interest = 0
            for (month) in range(1, 13):
                interest_paid = outstanding_principal * rate_in_decimal
                principal_paid = Mortgage - interest_paid
                annual_principal += principal_paid
                annual_interest += interest_paid
                outstanding_principal -= principal_paid
            print("Year: {year}; Monthly Payment: {Mortgage}; Interest Paid: {Interest}; Principal Paid: {Principal};\
 Outstanding Principal: {Outstanding}".format(year=year, Mortgage=round(Mortgage, 2), Interest=round(annual_interest, 2),\
                  Principal=round(annual_principal, 2), Outstanding=round(outstanding_principal, 2)))

#Execution
print("Your monthly mortgage will be {mortgage}.".format(mortgage=Mortgage_2_deci))
amortization_schedule(Mortgage, p, interest_rate, loan_period)


print("GG End")