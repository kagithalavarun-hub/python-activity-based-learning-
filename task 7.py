class Passenger:
    def __init__(self, name, age, distance, travel_class):
        self.name = name
        self.age = age
        self.distance = distance
        self.travel_class = travel_class

    def calculate_base_fare(self):
        # Distance Slabs
        if self.distance <= 100:
            fare = self.distance * 0.8
        elif self.distance <= 500:
            fare = (100 * 0.8) + ((self.distance - 100) * 1.2)
        else:
            fare = (100 * 0.8) + (400 * 1.2) + ((self.distance - 500) * 1.5)

        # Class Multipliers
        class_multiplier = {
            "Sleeper": 1.0,
            "AC3": 1.75,
            "AC2": 2.5
        }

        return fare * class_multiplier[self.travel_class]

    def calculate_concession(self, fare):
        # Age-Based Concessions
        if self.age < 12:
            return fare * 0.50  # 50% concession
        elif self.age >= 60:
            return fare * 0.40  # 40% concession
        else:
            return 0

    def calculate_total_fare(self):
        base_fare = self.calculate_base_fare()

        concession = self.calculate_concession(base_fare)

        reservation_fee = {
            "Sleeper": 20,
            "AC3": 40,
            "AC2": 60
        }

        total_fare = (
            base_fare -
            concession +
            reservation_fee[self.travel_class]
        )

        return round(base_fare, 2), round(concession, 2), round(total_fare, 2)


class Reservation:
    def __init__(self):
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def generate_ticket(self):
        total_amount = 0

        print("\nRAILWAY FARE REPORT")
        print("=" * 80)

        for p in self.passengers:
            base, concession, total = p.calculate_total_fare()

            total_amount += total

            print(f"\nPassenger Name : {p.name}")
            print(f"Age            : {p.age}")
            print(f"Distance       : {p.distance} km")
            print(f"Class          : {p.travel_class}")
            print(f"Base Fare      : ₹{base:.2f}")
            print(f"Concession     : ₹{concession:.2f}")
            print(f"Total Fare     : ₹{total:.2f}")
            print("-" * 50)

        print(f"\nGRAND TOTAL: ₹{total_amount:.2f}")
        print("=" * 80)

    def cancel_ticket(self):
        total_amount = sum(
            p.calculate_total_fare()[2]
            for p in self.passengers
        )

        # Cancellation Rules
        if total_amount <= 500:
            penalty = 50
        elif total_amount <= 2000:
            penalty = 100
        else:
            penalty = total_amount * 0.10

        refund = total_amount - penalty

        print("\nTICKET CANCELLATION DETAILS")
        print("=" * 50)
        print(f"Original Fare       : ₹{total_amount:.2f}")
        print(f"Cancellation Charge : ₹{penalty:.2f}")
        print(f"Refund Amount       : ₹{refund:.2f}")
        print("=" * 50)


# Sample Usage
reservation = Reservation()

reservation.add_passenger(
    Passenger("Rahul", 35, 600, "AC3")
)

reservation.add_passenger(
    Passenger("Priya", 65, 600, "AC3")
)

reservation.add_passenger(
    Passenger("Kiran", 10, 600, "Sleeper")
)

# Generate Ticket
reservation.generate_ticket()

# Cancellation Details
reservation.cancel_ticket()