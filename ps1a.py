## test changes for git


balance = int(raw_input('Enter the outstanding balance on your credit card: '))
rate = float(raw_input('Enter your annual interest rate: '))
min_monthly = float(raw_input('Enter your minimum monthly payment: '))

                
total_paid = 0

for month in range(1,13):
    print 'Month: ', month
    min_payment = balance * min_monthly
    print 'Minimum monthly payment: ',round(min_payment,2)
    interest_paid = balance * rate/12
    prin_paid = min_payment - interest_paid
    print 'Principal paid: ', round(prin_paid,2)
    balance -= prin_paid
    print 'Remaining balance: ', round(balance,2)
    total_paid += min_payment

print 'RESULT'
print 'Total amount paid: ', round(total_paid,2)
print 'Remaining balance: ', round(balance,2)
