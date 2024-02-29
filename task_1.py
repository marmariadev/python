# Simulate deposit and withdrawal operations in an ATM.

balance = 1000
operation = input("Choose operation: Deposit (D) or Withdraw (W)? ").upper()

if operation == "D":
    amount = float(input("Amount to deposit: "))
    balance += amount
    print(f"New balance: ${balance}")
elif operation == "W":
    amount = float(input("Amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print(f"New balance: ${balance}")
else:
    print("Invalid operation.")