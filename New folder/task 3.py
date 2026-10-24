class ElectricityBill:
    def __init__(self, month, units):
        self.month = month
        self.units = units

    def calculate_bill(self):
        units = self.units
        bill = 0

        # Progressive Slab Rates
        if units <= 100:
            bill = units * 1.5

        elif units <= 300:
            bill = (100 * 1.5) + ((units - 100) * 2.5)

        elif units <= 500:
            bill = (100 * 1.5) + (200 * 2.5) + ((units - 300) * 4)

        else:
            bill = (100 * 1.5) + (200 * 2.5) + (200 * 4) + ((units - 500) * 6)

        # Fixed Charge
        fixed_charge = 100
        bill += fixed_charge

        # Surcharge (10% if units exceed 400)
        if units > 400:
            bill += bill * 0.10

        # Rebate (5% for consumption below 150 units)
        if units < 150:
            bill -= bill * 0.05

        return round(bill, 2)


def compare_bills(monthly_data):
    bills = []

    print("\nMONTHLY ELECTRICITY BILL REPORT")
    print("-" * 60)

    for data in monthly_data:
        bill_obj = ElectricityBill(data["month"], data["units"])
        amount = bill_obj.calculate_bill()

        bills.append({
            "month": data["month"],
            "units": data["units"],
            "amount": amount
        })

        print(f"{data['month']:10} Units: {data['units']:4}  Bill: ₹{amount:.2f}")

    print("\nUNUSUAL BILL INCREASE ANALYSIS")
    print("-" * 60)

    for i in range(1, len(bills)):
        previous = bills[i - 1]["amount"]
        current = bills[i]["amount"]

        increase = ((current - previous) / previous) * 100

        print(
            f"{bills[i-1]['month']} -> {bills[i]['month']} : "
            f"{increase:.2f}% change"
        )

        if increase > 20:
            print(
                f"⚠ ALERT: Unusual increase detected in "
                f"{bills[i]['month']} ({increase:.2f}%)"
            )


# Sample Monthly Usage Data
monthly_usage = [
    {"month": "January", "units": 120},
    {"month": "February", "units": 140},
    {"month": "March", "units": 220},
    {"month": "April", "units": 380},
    {"month": "May", "units": 540},
    {"month": "June", "units": 560}
]

compare_bills(monthly_usage)