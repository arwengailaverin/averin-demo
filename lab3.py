def check_loan_eligibility(salary, loan_amount):
    #Eligibilty criteria
    min_salary = 30000.00
    max_loan_amount = salary * 10

    if salary < min_salary:
        return False, "Salary is too low."
    elif loan_amount > max_loan_amount:
        return False, "Requested amount is too high."
    else:
        return True, ""

def calculated_repayment(loan_amount, months):
    # Calculate the total repayment with 10% loan interest increase
    interest_rate = 0.10
    total_repayment = loan_amount * (1 + interest_rate)
    monthly_payment = total_repayment / months
    return total_repayment, monthly_payment

def main():
    #Input salary and request loan amount 
    try: 
        salary = float(input("Enter your monthly salary: "))
        loan_amount = float(input("Enter the loan amount you want to request: "))

        #Check for eligibility 
        eligible, message = check_loan_eligibility(salary, loan_amount)

        if eligible:
            months = int(input("Enter number of Months to pay: "))
            total_repayment, monthly_payment = calculated_repayment(loan_amount, months)
            print(f"You're eligible for the loan")
            print(f"Total amount to be repaid: {total_repayment:.2f}")
            print(f"monthly payment over {months} months: {monthly_payment:.2f}")
        else:
            print("Loan not approved", message)
        
    except ValueError:
        print("Please enter valid numbers for salary and loan amount.")
if __name__ == "__main__":
    main()