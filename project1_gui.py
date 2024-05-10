#gui file
from tkinter import *
import csv
from project1_functions import *

class GUI:
    def __init__(self, window):
        '''
        Initialize the GUI
        :param window: Instance GUI
        '''
        self.__window = window
        self.__atm_accounts = []

        self.__frame1 = Frame(self.__window)
        self.__frame2 = Frame(self.__window)
        self.__frame3 = Frame(self.__window)
        self.__frame4 = Frame(self.__window)
        self.__frame5 = Frame(self.__window)
        self.__frame6 = Frame(self.__window)
        self.__frame7 = Frame(self.__window)
        self.__frame8 = Frame(self.__window)
        self.__frame9 = Frame(self.__window)
        self.__frame10 = Frame(self.__window)
        self.__name_label = Label(self.__frame1, text='Name')
        self.__name_entry = Entry(self.__frame1)
        self.__password_label = Label(self.__frame2, text='Password')
        self.__password_entry = Entry(self.__frame2, show="*")
        self.__search_button = Button(self.__frame3, text='Search', command=self.search_press)
        self.__status_label = Label(self.__frame4, text='Hello ')
        self.__welcome_label = Label(self.__frame5, text='What would you like to do?')
        self.__choices = ['Withdraw', 'Deposit']
        self.__x = IntVar(value=-1)
        for i in range(len(self.__choices)): #RADIO BUTTONS
            self.__radiobutton = Radiobutton(self.__frame6, text=self.__choices[i], variable=self.__x, value=i)
            self.__radiobutton.pack(side=TOP, padx=10)

        self.__amount_label = Label(self.__frame7, text='Amount:')
        self.__amount_entry = Entry(self.__frame7)
        self.__balance_label = Label(self.__frame8, text='Your account balance is: ')
        self.__enter_button = Button(self.__frame9, text='ENTER', command=self.enter_press)
        self.__exit_button = Button(self.__frame10, text='EXIT', command=self.exit_press)

        #packing
        self.__frame1.pack(fill=X, padx=20, pady=5)
        self.__frame2.pack(fill=X, padx=20, pady=5)
        self.__frame3.pack(fill=X, padx=20, pady=20)
        self.__frame4.pack(fill=X, padx=20, pady=5)
        self.__frame5.pack(fill=X, padx=20, pady=10, side=TOP)
        self.__frame6.pack(fill=X, padx=20, pady=10, side=TOP)
        self.__frame7.pack(fill=X, padx=20, pady=10)
        self.__frame8.pack(fill=X, padx=20, pady=10)
        self.__frame9.pack(fill=X, padx=20, pady=30)
        self.__frame10.pack(fill=X, padx=20, pady=10)
        self.__name_label.pack()
        self.__name_entry.pack()
        self.__password_label.pack()
        self.__password_entry.pack()
        self.__search_button.pack()
        self.__status_label.pack()
        self.__welcome_label.pack_forget()
        self.__status_label.pack_forget()
        self.__amount_label.pack(padx=5, fill=X, expand=True)
        self.__amount_entry.pack(padx=1)
        self.__balance_label.pack_forget()
        self.__enter_button.pack()
        self.__exit_button.pack()

    def search_press(self) -> None:
        """
        Modify the status, welcome, and balance labels when Search button is pressed
        :return: None
        """
        name: str = self.get_name()
        self.__status_label.config(text=f'Hello {name}')
        self.__status_label.pack()
        self.__welcome_label.pack()
        self.__balance_label.config(text=f'Your account balance is:')
        self.__balance_label.pack()
    def enter_press(self):
        """
        When ENTER button is pressed, first check if account name and password exists, also check if password
        is correct. Else, write new account information. Withdraws and deposits money based on amount entry input.
        Updates information in CSV file.
        :return: Only returns to leave the method or function if password is incorrect or if there are insufficient
        funds.
        """
        name: str = self.get_name()
        password: str = self.get_password()
        amount: float = self.get_amount()

        #check
        if not self.check_account_exists(name, password):
            with open('account_data.csv', mode='a', newline='') as myfile:
                writer = csv.writer(myfile)
                writer.writerow([name, password, 0])
        else:
            if not self.check_pass_match(name, password):
                self.__status_label.config(text='Error: Incorrect password')
                return  #wrong pass
            else:
                self.__status_label.config(text=f'Hello {name}')

        currentbalance: float = self.current_balance(name, password)
        account = Account(name, currentbalance)

        if self.__x.get() == 0:#withdraw
            if not account.withdraw(amount):
                self.__status_label.config(text='Error: Insufficient funds')
                return
        elif self.__x.get() == 1: #deposit
            account.deposit(amount)

        self.__balance_label.config(text=f'Your account balance is: {account.get_balance()}')
        self.__balance_label.pack()

        self.update_csv(name, password, account.get_balance())



    def update_csv(self, name: str, password: str, new_balance: float) -> None:
        """
        Updates data in CSV file called "account_data".
        :param name: Name of account
        :param password: Password of account
        :param new_balance: New balance of account
        :return: None
        """
        rows = []
        with open('account_data.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for line in reader:
                if line[0] == name and line[1] == password:
                    line[2] = str(new_balance)
                rows.append(line)

        with open('account_data.csv', mode='w', newline='') as f:
            writer = csv.writer(f)
            for line in rows:
                writer.writerow(line)
    def update_balance(self, name: str, password: str, balance: str) -> None:
        """
        Update balance in account accordingly in the CSV file that is opened.
        :param name: Name of account
        :param password: Password of account
        :param balance: Balance of account
        :return: None
        """
        with open('account_data.csv', mode='r', newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)

        with open('account_data.csv', mode='w', newline='') as f:
            writer = csv.writer(f)
            for x in rows:
                if x[0] == name and x[1] == password:
                    x[2] = balance
                writer.writerow(x)
    def get_amount(self) -> float:
        """
        Grabs amount with getter methods and displays error messages if need be.
        :return: Amount
        """
        try:
            amount = float(self.__amount_entry.get())

        except ValueError:
            self.__status_label.config(text='Error: Amount has to be a number')
            raise ValueError('Amount should be a number.')
        return amount

    def current_balance(self, name: str, password: str) -> float:
        """
        Getter for current balance in CSV file
        :param name: Name of account
        :param password: Password of account
        :return: If the account is not found then return a default balance of zero as a float
        """
        with open('account_data.csv', mode='r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == name and row[1] == password:
                    return float(row[2])
        return 0.0

    def exit_press(self) -> None:
        '''
        Exit the GUI
        :return: None
        '''
        self.__window.quit()

    def get_name(self) -> str:
        '''
        Getter for the input in the name entry on GUI
        :return: The string name for the account
        '''
        return self.__name_entry.get()

    def get_password(self) -> str:
        '''
        Getter for the input in the password entry on the GUI
        :return: String password
        '''
        return self.__password_entry.get()


    def check_account_exists(self, name: str, password: str) -> bool:
        """
        This checks whether the account exists in the CSV
        :param name: Name for account
        :param password: Password for account
        :return: Boolean value that depends on account existence
        """
        with open('account_data.csv', mode='r', newline='') as mycsvfile:
            reader = csv.reader(mycsvfile)
            for row in reader:
                if row[0] == name:
                    return True


        return False



    def check_pass_match(self, name: str, password: str) -> bool:
        """
        Double checks if the password matches with opening file for reading.
        :param name: Name of account
        :param password: Password of account
        :return: Boolean value
        """
        with open('account_data.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == name and row[1] == password:
                    return True
        return False
