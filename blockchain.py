import hashlib

# Initialize an empty hospital ledger (a dictionary where keys are patient names)
hospital_ledger_advanced = {}

# Function to generate a hash for a visit record
def generate_hash(patient_name, treatment, cost, date_of_visit):
    # Combine all visit details into one string
    visit_data = patient_name + treatment + str(cost) + date_of_visit
    # Generate the SHA-256 hash of the visit data
    visit_hash = hashlib.sha256(visit_data.encode()).hexdigest()
    return visit_hash

# Function to add or update patient visits
def add_patient_visit_advanced():
    # Get patient details from the user
    patient_name = input("Enter the patient's name: ")
    treatment = input("Enter the treatment received: ")
    cost = float(input("Enter the cost of the treatment: $"))
    date_of_visit = input("Enter the date of visit (YYYY-MM-DD): ")

    # Generate a hash for this visit record
    visit_hash = generate_hash(patient_name, treatment, cost, date_of_visit)

    # Create a dictionary for the visit with the hash
    visit = {
        "patient_name": patient_name,
        "treatment": treatment,
        "cost": cost,
        "date_of_visit": date_of_visit,
        "visit_hash": visit_hash  # Store the hash to verify data integrity
    }

    # Add the visit to the patient's list of visits
    if patient_name not in hospital_ledger_advanced:
        hospital_ledger_advanced[patient_name] = []

    hospital_ledger_advanced[patient_name].append(visit)
    print(f"Visit added for {patient_name} on {date_of_visit} for treatment {treatment} costing ${cost}.")
    print(f"Visit hash: {visit_hash}")

# Ask the user to add visits
add_patient_visit_advanced()
add_patient_visit_advanced()

# Display the advanced hospital ledger
print("\nAdvanced Hospital Ledger:")
for patient, visits in hospital_ledger_advanced.items():
    print(f"\nPatient: {patient}")
    for visit in visits:
        print(f"  Treatment: {visit['treatment']}, Cost: ${visit['cost']}, Date: {visit['date_of_visit']}, Hash: {visit['visit_hash']}")
