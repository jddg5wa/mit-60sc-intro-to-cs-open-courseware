initialBalance = float(input("Enter the outstanding balance on your credit card: "))
interestRate = float(input("Enter the annual credit card interest rate as a decimal: "))

monthlyInterestRate = interestRate/12

low = initialBalance/12
high = (initialBalance * (1 + (interestRate/12.0)) * 12.0)/12
currentMonthlyPayment = (low + high)/2

epsilon = .01
balance = initialBalance

while (high - low >= epsilon):
	
	currentMonthlyPayment = (low + high)/2
	currentMonth = 0
	balance = initialBalance

	while (currentMonth < 12 and balance > 0):
		interest = round(balance*interestRate/12, 2)
		balance += interest - currentMonthlyPayment
		# balance = round(balance * (1 + monthlyInterestRate) - currentMonthlyPayment,2)
		currentMonth += 1

	print ("balance",balance)
	if balance < 0:
		high = currentMonthlyPayment
		print("high",high)
		

	else:
		low = currentMonthlyPayment
		print ("low", low)
		

	print ("high - low", high-low)
		
		
print("RESULT")
print("Montly payment to pay off debt in 1 year: " + str(round(currentMonthlyPayment,2)))
print("Number of months needed: " + str(currentMonth))
print("Balance: " + str(round(balance,2)))