# demo.py

from orchestration_service_demo import OrchestrationServiceDemo

def run_demo():
    """
    Runs the multi-agent system demo for heart attack and heart failure.
    """
    print("Welcome to the Heart Health Multi-Agent System Demo.")
    print("Please describe your symptoms.")

    symptoms = input("Enter symptoms: ")

    # Initialize the simplified Orchestration Service
    orchestration_service = OrchestrationServiceDemo()

    # Process the symptoms through the orchestration service
    results = orchestration_service.process_symptoms(symptoms)
    diagnosis = results.get("diagnosis", "N/A")
    treatment_plan = results.get("treatment_plan", "N/A")

    # Display the results
    print("\n--- Diagnosis and Treatment Plan ---")
    print(f"Diagnosis: {diagnosis}")
    print(f"Recommended Treatment: {treatment_plan}")
    print("------------------------------------")

if __name__ == "__main__":
    run_demo()