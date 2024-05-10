#lab 9 revamp
#Logic File
class Account:
    def __init__(self, name: str, balance: int=0) -> None:
        '''
        Creates and sets the instance variables
        :param name: Name of account creator
        :param balance: Default balance information put into the account from the creator
        '''
        self.__account_name: str = name
        self.__account_balance: int = balance
        self.set_balance(self.__account_balance)
    def deposit(self, amount: float) -> bool:
        '''
        Deposits an input amount into the account
        :param amount: Amount of money to be deposited, expected to be float
        :return: Boolean value
        '''
        if amount > 0.00:
            self.__account_balance += amount
            return True
        return False
    def withdraw(self, amount: float) -> bool:
        '''
        Withdraws input amount of money from the account
        :param amount: Expected float value to be removed from account
        :return: Boolean value
        '''
        if (amount > 0):
            if (amount < self.__account_balance):
                if (amount != self.__account_balance):
                    self.__account_balance -= amount
                    return True
        return False
    def get_balance(self) -> float:
        '''
        Gets the current balance of account
        :return: Balance of the account, converted to float
        '''
        return float(self.__account_balance)
    def get_name(self) -> str:
        '''
        Gets the name of the account holder
        :return: Name of the account holder, converted to string
        '''
        return str(self.__account_name)
    def set_balance(self, value: float) -> None:
        '''
        Quickly sets the balance to the value parameter. If the value is less than 0, set the balance to just 0.
        Otherwise, set the balance to the value
        :param value: Float variable to set the account balance to
        :return: None
        '''
        value = float(value)
        if value < 0.00:
            self.__account_balance = 0.00
        else:
            self.__account_balance = float(value)
    def set_name(self, value: str) -> None:
        '''
        Set the name of the account creator to the string value.
        :param value: String parameter to set account name to
        :return: None
        '''
        self.__account_name = str(value)
    def __str__(self) -> str:
        '''
        Display information about name of account holder and their respective balance.
        :return: Formatted string of account name and account balance
        '''
        return f'Account name = {Account.get_name(self)}, Account balance = {Account.get_balance(self):.2f}'


