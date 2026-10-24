class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def subtotal(self):
        return self.price * self.quantity


class RetailBilling:
    def __init__(self):
        self.products = []

        # Tax Rates by Category (%)
        self.tax_rates = {
            "Grocery": 5,
            "Electronics": 18,
            "Clothing": 12,
            "Furniture": 18
        }

        # Maximum Discount Allowed
        self.max_discount = 5000

    def add_product(self, product):
        self.products.append(product)

    def calculate_bill(self):
        total_before_tax = 0
        total_tax = 0

        print("\n" + "=" * 90)
        print(" " * 30 + "RETAIL INVOICE")
        print("=" * 90)

        print(
            f"{'Product':15}"
            f"{'Category':15}"
            f"{'Qty':8}"
            f"{'Price':12}"
            f"{'Subtotal':15}"
            f"{'Tax':10}"
        )

        print("-" * 90)

        for product in self.products:
            subtotal = product.subtotal()

            tax_rate = self.tax_rates.get(product.category, 0)
            tax_amount = subtotal * tax_rate / 100

            total_before_tax += subtotal
            total_tax += tax_amount

            print(
                f"{product.name:15}"
                f"{product.category:15}"
                f"{product.quantity:<8}"
                f"₹{product.price:<10.2f}"
                f"₹{subtotal:<13.2f}"
                f"₹{tax_amount:<8.2f}"
            )

        gross_amount = total_before_tax + total_tax

        # Threshold Discounts
        if gross_amount >= 50000:
            discount = gross_amount * 0.15
        elif gross_amount >= 25000:
            discount = gross_amount * 0.10
        elif gross_amount >= 10000:
            discount = gross_amount * 0.05
        else:
            discount = 0

        # Enforce Maximum Discount Limit
        discount = min(discount, self.max_discount)

        net_amount = gross_amount - discount

        print("-" * 90)
        print(f"{'Total Product Value':50} ₹{total_before_tax:.2f}")
        print(f"{'Total Tax':50} ₹{total_tax:.2f}")
        print(f"{'Gross Amount':50} ₹{gross_amount:.2f}")
        print(f"{'Discount Applied':50} ₹{discount:.2f}")
        print(f"{'Net Payable':50} ₹{net_amount:.2f}")
        print("=" * 90)


# Sample Products
billing = RetailBilling()

billing.add_product(
    Product("Rice", "Grocery", 60, 20)
)

billing.add_product(
    Product("Laptop", "Electronics", 45000, 1)
)

billing.add_product(
    Product("Shirt", "Clothing", 1200, 3)
)

billing.add_product(
    Product("Chair", "Furniture", 3000, 2)
)

# Generate Invoice
billing.calculate_bill()