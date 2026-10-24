class ManufacturingProduct:
    def __init__(
        self,
        product_name,
        units_produced,
        material_cost_per_unit,
        labour_cost_per_unit,
        machine_cost,
        wastage_percentage,
        selling_price_per_unit,
        profit_target
    ):
        self.product_name = product_name
        self.units_produced = units_produced
        self.material_cost_per_unit = material_cost_per_unit
        self.labour_cost_per_unit = labour_cost_per_unit
        self.machine_cost = machine_cost
        self.wastage_percentage = wastage_percentage
        self.selling_price_per_unit = selling_price_per_unit
        self.profit_target = profit_target

    def calculate_costs(self):
        material_cost = (
            self.units_produced *
            self.material_cost_per_unit
        )

        labour_cost = (
            self.units_produced *
            self.labour_cost_per_unit
        )

        wastage_cost = (
            material_cost *
            self.wastage_percentage / 100
        )

        total_cost = (
            material_cost +
            labour_cost +
            wastage_cost +
            self.machine_cost
        )

        return material_cost, labour_cost, wastage_cost, total_cost

    def calculate_profitability(self):
        material_cost, labour_cost, wastage_cost, total_cost = self.calculate_costs()

        revenue = (
            self.units_produced *
            self.selling_price_per_unit
        )

        profit = revenue - total_cost

        meets_target = profit >= self.profit_target

        return {
            "material_cost": material_cost,
            "labour_cost": labour_cost,
            "wastage_cost": wastage_cost,
            "machine_cost": self.machine_cost,
            "total_cost": total_cost,
            "revenue": revenue,
            "profit": profit,
            "meets_target": meets_target
        }

    def display_report(self):
        result = self.calculate_profitability()

        print("\n" + "=" * 70)
        print("      MANUFACTURING COST & PROFITABILITY REPORT")
        print("=" * 70)

        print(f"Product Name           : {self.product_name}")
        print(f"Units Produced         : {self.units_produced}")

        print("\nCOST BREAKDOWN")
        print("-" * 70)
        print(f"Material Cost          : ₹{result['material_cost']:.2f}")
        print(f"Labour Cost            : ₹{result['labour_cost']:.2f}")
        print(f"Wastage Cost           : ₹{result['wastage_cost']:.2f}")
        print(f"Machine Cost           : ₹{result['machine_cost']:.2f}")
        print(f"Total Manufacturing Cost: ₹{result['total_cost']:.2f}")

        print("\nREVENUE & PROFIT")
        print("-" * 70)
        print(f"Revenue                : ₹{result['revenue']:.2f}")
        print(f"Profit/Loss            : ₹{result['profit']:.2f}")

        print("\nTARGET ANALYSIS")
        print("-" * 70)
        print(f"Profit Target          : ₹{self.profit_target:.2f}")

        if result['meets_target']:
            print("Status                 : TARGET ACHIEVED ✅")
        else:
            print("Status                 : TARGET NOT ACHIEVED ❌")

        print("=" * 70)


# Sample Data
product = ManufacturingProduct(
    product_name="Steel Chair",
    units_produced=500,
    material_cost_per_unit=800,
    labour_cost_per_unit=250,
    machine_cost=50000,
    wastage_percentage=5,
    selling_price_per_unit=1300,
    profit_target=100000
)

# Generate Report
product.display_report()