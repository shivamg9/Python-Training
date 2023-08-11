# Saurabh needs to withdraw X Rs. from an ATM. 
# The transaction will succeed only if X is an odd number,
# and Saurabh's account balance has enough cash to perform the withdrawal transaction (including bank charges). 
# For each successful withdrawal the bank charges 10.50 Rs. 
# Calculate Saurabh's account balance after an attempted transaction. 

# Input: 
# - Saurabh's initial account balance 
# - Withdrawal amount 

# Output 
# - Amount present in Saurabh's account after withdrawal. 
# - Error message, if the withdrawal did not match transaction criteria. 


initial_balance=float(input("initial account balance : "))
withdraw_amount=float(input("withdrawal amount : "))

if initial_balance>=10.5+withdraw_amount:
    print(f"amount present : {initial_balance-withdraw_amount-10.5}")
else:
    print("error: insufficient balance")