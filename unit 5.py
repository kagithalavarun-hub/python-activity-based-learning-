class Employee:
    def __init__(self, emp_id, name, basic_pay,
                 allowances, overtime_pay, incentives):
        self.emp_id = emp_id
        self.name = name
        self.basic_pay = basic_pay
        self.allowances = allowances
        self.overtime_pay = overtime_pay
        self.incentives = incentives

    # Calculate Gross Salary
    def calculate_gross_salary(self):
        return (self.basic_pay +
                self.allowances +
                self.overtime_pay +
                self.incentives)

    # Calculate Deductions
    def calculate_deductions(self):
        gross_salary = self.calculate_gross_salary()

        # Provident Fund (12% of Basic Pay)
        pf = self.basic_pay * 0.12

        # Professional Tax
        pt = 200

        # Progressive Income Tax
        if gross_salary <= 30000:
            income_tax = gross_salary * 0.05
        elif gross_salary <= 60000:
            income_tax = gross_salary * 0.10
        else:
            income_tax = gross_salary * 0.15

        total_deductions = pf + pt + income_tax

        return pf, pt, income_tax, total_deductions

    # Calculate Net Salary
    def calculate_net_salary(self):
        gross = self.calculate_gross_salary()
        _, _, _, deductions = self.calculate_deductions()

        return gross - deductions

    # Generate Salary Statement
    def generate_salary_statement(self):
        gross = self.calculate_gross_salary()
        pf, pt, income_tax, total_deductions = self.calculate_deductions()
        net_salary = self.calculate_net_salary()

        print("\n" + "=" * 60)
        print("            EMPLOYEE SALARY STATEMENT")
        print("=" * 60)
        print(f"Employee ID      : {self.emp_id}")
        print(f"Employee Name    : {self.name}")
        print("-" * 60)
        print(f"Basic Pay        : ₹{self.basic_pay:,.2f}")
        print(f"Allowances       : ₹{self.allowances:,.2f}")
        print(f"Overtime Pay     : ₹{self.overtime_pay:,.2f}")
        print(f"Incentives       : ₹{self.incentives:,.2f}")
        print("-" * 60)
        print(f"Gross Salary     : ₹{gross:,.2f}")
        print("-" * 60)
        print("DEDUCTIONS")
        print(f"Provident Fund   : ₹{pf:,.2f}")
        print(f"Professional Tax : ₹{pt:,.2f}")
        print(f"Income Tax       : ₹{income_tax:,.2f}")
        print(f"Total Deductions : ₹{total_deductions:,.2f}")
        print("-" * 60)
        print(f"Net Salary       : ₹{net_salary:,.2f}")
        print("=" * 60)


# Sample Employee Records
employees = [
    Employee(101, "Rahul", 40000, 8000, 3000, 5000),
    Employee(102, "Priya", 25000, 5000, 2000, 3000),
    Employee(103, "Anjali", 60000, 12000, 5000, 7000)
]

# Generate Payroll Report
for emp in employees:
    emp.generate_salary_statement()