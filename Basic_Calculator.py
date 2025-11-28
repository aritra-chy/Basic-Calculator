class calculator:

    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        if b == 0:
            return "Cannot divide by zero"
        return a/b

    def get_number(self,message):
        while True:
            try:
                num = float(input(message))
                return num
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    def menu(self):
        print("\n----- CALCULATOR MENU -----")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

    def run(self):
        while True:
            self.menu()
            choice = input("Choose an option (1-5): ")

            if choice == '5':
                print("Thanks For Using The Calculator!")
                break

            if choice not in ['1', '2', '3', '4']:
                print("Invalid Option! Please select a valid option(1-5).")
                continue

            num1 = self.get_number("Enter first number: ")
            num2 = self.get_number("Enter second number: ")

            if choice == '1':
                result = self.add(num1, num2)
                print(f"{num1} + {num2} = {result}")

            elif choice == '2':
                result = self.sub(num1, num2)
                print(f"{num1} - {num2} = {result}")

            elif choice == '3':
                result = self.mul(num1, num2)
                print(f"{num1} * {num2} = {result}")

            elif choice == '4':
                result = self.div(num1, num2)
                print(f"{num1} / {num2} = {result}")


calc = calculator()
calc.run()