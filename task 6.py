class MobilePlan:
    def __init__(self, name, monthly_cost, data_limit,
                 call_limit, sms_limit, validity,
                 extra_data_rate, extra_call_rate, extra_sms_rate):

        self.name = name
        self.monthly_cost = monthly_cost
        self.data_limit = data_limit      # GB
        self.call_limit = call_limit      # Minutes
        self.sms_limit = sms_limit
        self.validity = validity          # Days

        self.extra_data_rate = extra_data_rate
        self.extra_call_rate = extra_call_rate
        self.extra_sms_rate = extra_sms_rate

    def calculate_total_cost(self, data_used, calls_used, sms_used):

        extra_data = max(0, data_used - self.data_limit)
        extra_calls = max(0, calls_used - self.call_limit)
        extra_sms = max(0, sms_used - self.sms_limit)

        excess_charge = (
            extra_data * self.extra_data_rate +
            extra_calls * self.extra_call_rate +
            extra_sms * self.extra_sms_rate
        )

        total_cost = self.monthly_cost + excess_charge

        return total_cost, excess_charge


def find_best_plan(plans, data_used, calls_used,
                   sms_used, required_validity, budget):

    eligible_plans = []

    print("\nMOBILE PLAN COMPARISON")
    print("=" * 80)
    print(
        f"{'Plan':15}{'Base Cost':12}"
        f"{'Excess Charge':15}{'Total Cost':15}"
    )
    print("-" * 80)

    for plan in plans:

        if plan.validity < required_validity:
            continue

        total_cost, excess_charge = plan.calculate_total_cost(
            data_used,
            calls_used,
            sms_used
        )

        print(
            f"{plan.name:15}₹{plan.monthly_cost:<10.2f}"
            f"₹{excess_charge:<13.2f}"
            f"₹{total_cost:<10.2f}"
        )

        if total_cost <= budget:
            eligible_plans.append((plan, total_cost))

    print("-" * 80)

    if not eligible_plans:
        print("\nNo plan satisfies the given budget and validity constraints.")
        return

    best_plan = min(eligible_plans, key=lambda x: x[1])

    print("\nMOST ECONOMICAL ELIGIBLE PLAN")
    print("=" * 80)
    print(f"Plan Name      : {best_plan[0].name}")
    print(f"Validity       : {best_plan[0].validity} Days")
    print(f"Total Cost     : ₹{best_plan[1]:.2f}")
    print(f"Budget Limit   : ₹{budget}")
    print("=" * 80)


# Available Mobile Plans
plans = [
    MobilePlan(
        "Basic",
        249,
        20,
        500,
        100,
        28,
        10,     # ₹10 per GB
        0.5,    # ₹0.5 per minute
        0.2     # ₹0.2 per SMS
    ),

    MobilePlan(
        "Standard",
        399,
        40,
        1000,
        200,
        28,
        8,
        0.4,
        0.15
    ),

    MobilePlan(
        "Premium",
        599,
        80,
        2000,
        500,
        56,
        5,
        0.2,
        0.1
    ),

    MobilePlan(
        "Unlimited",
        799,
        150,
        5000,
        1000,
        84,
        0,
        0,
        0
    )
]


# Customer Usage Details
data_used = 50      # GB
calls_used = 1200   # Minutes
sms_used = 250
required_validity = 28
budget = 800

find_best_plan(
    plans,
    data_used,
    calls_used,
    sms_used,
    required_validity,
    budget
)