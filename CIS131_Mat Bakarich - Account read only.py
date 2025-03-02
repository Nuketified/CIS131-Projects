# Module 5 Assignment
# Mat Bakarich 
# Feb 27, 2025

"""Account class definition."""
from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance."""

    def __init__(self, name, balance):
        """Initialize an Account object."""

        # if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')

        self.__name = name
        self.__balance = balance

    def deposit(self, amount):
        """Deposit money to the account."""

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self.__balance += amount
    
    def details(self):
        """Print the account details and balance."""
        print(self.__name)
        print(self.__balance)


