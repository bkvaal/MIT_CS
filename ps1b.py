balance = int(raw_input('Enter the outstanding balance on your credit card: '))
rate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))

payment = 0
while True:
    test_balance = balance
    total_paid = 0
    payment += 10
    for month in range(1,13):
        interest_paid = test_balance * rate/12
        prin_paid = payment - interest_paid
        test_balance -= prin_paid
       
        total_paid += payment
        if test_balance < 0: break
    if test_balance < 0: break     
print 'RESULT'
print 'Monthly payment to pay off debt in 1 year: ', payment
print 'Number of months needed: ', month
print 'Balance: ', round(test_balance,2)

