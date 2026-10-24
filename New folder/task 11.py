import math

print("=== Campus Event Financial Planner ===")

# Input costs
venue_cost = float(input("Enter venue cost: "))
equipment_cost = float(input("Enter equipment cost: "))
catering_cost = float(input("Enter catering cost: "))
transport_cost = float(input("Enter transport cost: "))
certificate_cost = float(input("Enter certificate cost: "))

# Revenue inputs
registration_fee = float(input("Enter registration fee per participant: "))
expected_participants = int(input("Enter expected number of participants: "))
sponsorship_amount = float(input("Enter sponsorship amount: "))

# Total expenses
total_cost = (venue_cost + equipment_cost +
              catering_cost + transport_cost +
              certificate_cost)

# Participant contribution
participant_contribution = registration_fee * expected_participants

# Total revenue
total_revenue = participant_contribution + sponsorship_amount

# Shortfall or surplus
shortfall = total_cost - total_revenue

# Break-even registrations
if registration_fee > 0:
    break_even_registrations = math.ceil(
        max(0, total_cost - sponsorship_amount) / registration_fee
    )
else:
    break_even_registrations = 0

# Results
print("\n===== Financial Summary =====")
print(f"Total Event Cost: ₹{total_cost:,.2f}")
print(f"Participant Contribution: ₹{participant_contribution:,.2f}")
print(f"Sponsorship Amount: ₹{sponsorship_amount:,.2f}")
print(f"Total Revenue: ₹{total_revenue:,.2f}")

if shortfall > 0:
    print(f"Sponsorship Shortfall / Deficit: ₹{shortfall:,.2f}")
else:
    print(f"Surplus: ₹{abs(shortfall):,.2f}")

print(f"Minimum Registrations Needed to Break Even: {break_even_registrations}")