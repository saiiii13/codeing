class BankAccount:
    # TODO: Add class variable interest_rate set to 0.02 (2%)
    interest_rate = 0.02
    def __init__(self, account_holder, balance):
        # TODO: Initialize instance variables:
        self.account_holder = account_holder
        self.balance = balance
        pass
    
    def display_info(self):
        # TODO: Print account information in this exact format:
        print(f"")
        # "Balance: $[balance]"
        # "Interest Rate: [interest_rate]%"
        # Don't forget to multiply interest_rate by 100 for percentage display
        # Add a blank line after the information
        pass
  