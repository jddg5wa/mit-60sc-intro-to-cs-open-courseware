outstandingBalance = float(input("Enter the outstanding balance on your credit card: "))
interestRate = float(input("Enter the annual credit card interest rate as a decimal: "))
minPaymentRate = float(input("Enter the minimum monthly payment rate as a decimal: "))

monthlyInterestRate = interestRate/12

currentMonth = 1

totalAmountPaid = 0

while (currentMonth <= 12):

	minPayment = round(minPaymentRate * outstandingBalance, 2)

	totalAmountPaid = round(totalAmountPaid + minPayment, 2)

	interestPaid = round(monthlyInterestRate * outstandingBalance, 2)
	
	principlePaid = round(minPayment - interestPaid, 2)
	
	outstandingBalance = round(outstandingBalance - principlePaid, 2)


	print("Month: " + str(currentMonth))
	print("Minimum Monthly Payment: " + str(minPayment))
	print("Priciple Paid: " + str(principlePaid))
	print("Remaining Balance: " + str(outstandingBalance))

	currentMonth += 1

print("RESULT")
print("Total Amount Paid: " + str(totalAmountPaid))
print("Remaining Balance: " + str(outstandingBalance))

