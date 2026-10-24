class Patient:
    def __init__(self, patient_id, name, consultation_fee,
                 diagnostic_charges, treatment_charges,
                 patient_type):
        self.patient_id = patient_id
        self.name = name
        self.consultation_fee = consultation_fee
        self.diagnostic_charges = diagnostic_charges
        self.treatment_charges = treatment_charges
        self.patient_type = patient_type

    def validate_charges(self):
        charges = [
            self.consultation_fee,
            self.diagnostic_charges,
            self.treatment_charges
        ]

        return all(charge >= 0 for charge in charges)

    def calculate_bill(self):
        if not self.validate_charges():
            raise ValueError("Invalid charge entered. Charges cannot be negative.")

        total = (
            self.consultation_fee +
            self.diagnostic_charges +
            self.treatment_charges
        )

        concession = 0

        # Payment Policies
        if self.patient_type.lower() == "senior citizen":
            concession = total * 0.20

        elif self.patient_type.lower() == "insurance":
            concession = total * 0.15

        elif self.patient_type.lower() == "employee":
            concession = total * 0.25

        elif self.patient_type.lower() == "economically weaker":
            concession = total * 0.30

        final_bill = total - concession

        return total, concession, final_bill

    def classify_patient(self):
        return self.patient_type


def generate_report(patients):
    print("\nHOSPITAL BILLING REPORT")
    print("=" * 70)

    for patient in patients:
        try:
            total, concession, final_bill = patient.calculate_bill()

            print(f"\nPatient ID      : {patient.patient_id}")
            print(f"Patient Name    : {patient.name}")
            print(f"Category        : {patient.classify_patient()}")
            print(f"Consultation    : ₹{patient.consultation_fee:.2f}")
            print(f"Diagnostics     : ₹{patient.diagnostic_charges:.2f}")
            print(f"Treatment       : ₹{patient.treatment_charges:.2f}")
            print(f"Gross Bill      : ₹{total:.2f}")
            print(f"Concession      : ₹{concession:.2f}")
            print(f"Net Payable     : ₹{final_bill:.2f}")
            print("-" * 70)

        except ValueError as e:
            print(f"Error for {patient.name}: {e}")


# Sample Patient Data
patients = [
    Patient(
        101,
        "Rahul",
        500,
        1500,
        4000,
        "Insurance"
    ),
    Patient(
        102,
        "Priya",
        500,
        1000,
        2500,
        "Senior Citizen"
    ),
    Patient(
        103,
        "Kiran",
        500,
        2000,
        5000,
        "Employee"
    ),
    Patient(
        104,
        "Anjali",
        500,
        800,
        1500,
        "Economically Weaker"
    )
]

generate_report(patients)