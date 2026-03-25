class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class BillingSystem:
    def __init__(self):
        self.cart = []
        self.transactions = []

    def scan_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        product = Product(name, price)
        self.cart.append(product)
        print("Product added to cart")

    def apply_discount(self):
        discount = float(input("Enter discount percentage: "))
        total = sum(p.price for p in self.cart)
        discount_amount = total * discount / 100
        total = total - discount_amount
        return total

    def generate_bill(self):
        print("\n------ BILL ------")
        total = 0
        for p in self.cart:
            print(p.name, ":", p.price)
            total += p.price

        print("Total before discount:", total)
        choice = input("Apply discount? (yes/no): ")

        if choice == "yes":
            total = self.apply_discount()

        print("Final Total:", total)
        self.transactions.append(total)
        self.cart.clear()

    def view_transactions(self):
        print("\nTransactions:")
        for t in self.transactions:
            print("Bill Amount:", t)


bill = BillingSystem()

while True:
    print("\n1. Scan Product")
    print("2. Generate Bill")
    print("3. View Transactions")
    print("4. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        bill.scan_product()
    elif ch == "2":
        bill.generate_bill()
    elif ch == "3":
        bill.view_transactions()
    elif ch == "4":
        print("Program Ended")
        break
    else:
        print("Invalid choice")