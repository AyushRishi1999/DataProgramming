name = input("Enter employee's name : ")
hours = eval(input("Enter number of hours worked in a week : "))
payRate = eval(input("Enter hourly pay rate : "))
federalTax = eval(input("Enter federal tax withholding rate : "))
stateTax = eval(input("Enter state tax withholding rate : "))

grossPay = hours*payRate
federalWithhold = federalTax*grossPay
stateWithhold = stateTax*grossPay

print("Employee Name :", name)
print("Hours Worked:", hours)
print("Pay Rate: $"+str(payRate))
print("Gross Pay: $"+str(grossPay))
print("Deductions:")
print("\tFederal Withholding ("+str(float(federalTax))+"%): $"+str(federalWithhold))
print("\tState Withholding ("+str(float(stateTax))+"%): $"+str(stateWithhold))
print("\tTotal Deduction: $"+str(federalWithhold+stateWithhold))
print("Net Pay: $"+str(round(grossPay-federalWithhold-stateWithhold,2)))