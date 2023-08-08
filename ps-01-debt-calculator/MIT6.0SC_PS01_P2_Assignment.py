initialBalance = float(input("Enter the outstanding balance on your credit card: "))
interestRate = float(input("Enter the annual credit card interest rate as a decimal: "))

monthlyInterestRate = interestRate/12
currentMonthlyPayment = 10


balance = initialBalance

while (balance > 0 and currentMonthlyPayment < initialBalance):
	
	currentMonth = 0
	balance = initialBalance

	while (currentMonth < 12 and balance > 0):
		balance = round(balance * (1 + monthlyInterestRate) - currentMonthlyPayment, 2)
		currentMonth += 1
		currentMonthlyPayment += 10
		print("balance: " + str(balance))

print("RESULT")
print("Montly payment to pay off debt in 1 year: " + str(currentMonthlyPayment))
print("Number of months needed: " + str(currentMonth))
print("Balance: " + str(balance))