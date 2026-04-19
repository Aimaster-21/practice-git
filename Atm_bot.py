class AtmBot:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_choice = input("""
    How can I help you
    1.Press 1 to create a pin
    2.Press 2 to change the pin
    3.Press 3 to check the balance
    4.Press 4 to withdraw
    5.Press 5 to exit""")

        if user_choice == '1':
            self.create_pin()
        elif user_choice == '2':
            self.change_pin()
        elif user_choice == '3':
            self.check_balance()
        elif user_choice == '4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input('Enter the pin: ')
        self.pin = user_pin
        user_balance = int(input('Enter the balance: '))
        self.balance = user_balance
        print('Pin created successfully')
        self.menu()

    def change_pin(self):
        old_pin = input('Enter old pin: ')
        if old_pin == self.pin:
            new_pin = input('Enter the new pin: ')
            self.pin = new_pin
            print('Pin changed successfully')
        else:
            print('Incorrect old pin. Cannot change pin.')
        self.menu()

    def check_balance(self):
        user_pin = input('Enter your pin: ')
        if user_pin == self.pin:
            print('Your balance:', self.balance)
        else:
            print('Incorrect pin!')
        self.menu()

    def withdraw(self):
        user_pin = input('Enter the pin: ')
        if user_pin == self.pin:
            amount = int(input('Enter the amount: '))
            if amount <= self.balance:
                self.balance = self.balance - amount  #
                print('Withdrawn successfully. Balance is', self.balance)
            else:
                print('Insufficient balance!')
        else:
            print('Incorrect pin!')  # 
        self.menu()

obj = AtmBot()