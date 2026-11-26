"""Maverick Health AI - simple educational console demonstration.
This is a rule-based coursework prototype, not a medical diagnosis tool.
"""

training_data = {
    "urban": 900,
    "rural": 150,
    "elderly": 200,
    "children": 120,
}

MIN_DATA = 300
MIN_CONFIDENCE = 80


def check_case(name, prediction, confidence, group, consent):
    warnings = []

    if confidence < MIN_CONFIDENCE:
        warnings.append("Low confidence: the AI may be wrong")

    if training_data[group] < MIN_DATA:
        warnings.append("Bias risk: little data for this patient group")

    if consent != "yes":
        warnings.append("Privacy risk: patient consent was not given")

    if len(warnings) == 0:
        decision = "Approved (doctor still signs off)"
    elif len(warnings) == 1:
        decision = "Needs human review"
    else:
        decision = "High risk: doctor must review"

    print("\n--- Case Result ---")
    print("Patient:", name)
    print("Prediction entered:", prediction)
    print("Decision:", decision)
    if warnings:
        for warning in warnings:
            print("-", warning)
    else:
        print("No safety warnings")
    print("Note: This demonstration does not diagnose a patient.")


def main():
    print("Maverick Health AI - Console Demo")
    print("Available groups:", ", ".join(training_data.keys()))
    print("Illustrative group record counts:", training_data)

    while True:
        name = input("\nPatient name (or type exit): ").strip()
        if name.lower() == "exit":
            break

        prediction = input("AI prediction label: ").strip()
        try:
            confidence = float(input("AI confidence (0-100): "))
            if confidence < 0 or confidence > 100:
                print("Please enter a confidence from 0 to 100.")
                continue
        except ValueError:
            print("Please enter a valid number for confidence.")
            continue

        group = input("Patient group (urban/rural/elderly/children): ").strip().lower()
        if group not in training_data:
            print("Unknown group. Please use one of the listed groups.")
            continue

        consent = input("Has the patient given consent? (yes/no): ").strip().lower()
        if consent not in ["yes", "no"]:
            print("Please enter yes or no for consent.")
            continue

        check_case(name, prediction, confidence, group, consent)


if __name__ == "__main__":
    main()
