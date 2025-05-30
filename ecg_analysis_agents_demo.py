import random

def analyze_ecg(ecg_data):
    """
    Simplified ECG Analysis Agent for the demo.
    Simulates the detection of STEMI, NSTEMI, and Unstable Angina.

    Args:
        ecg_data (dict): Simulated ECG data (can be any format for this demo).

    Returns:
        dict: A dictionary indicating detected conditions.
    """
    print("ECG Analysis Agent: Analyzing ECG data...")

    # Simplified simulation of ECG analysis
    # In a real system, this would involve complex signal processing
    # We'll use random chance or simple rules for the demo

    detected_conditions = {
        "STEMI": False,
        "NSTEMI": False,
        "Unstable Angina": False
    }

    # Example simplified logic (can be expanded)
    # This is NOT based on actual ECG analysis, purely for demo purposes
    if random.random() < 0.3: # 30% chance of simulating a STEMI detection
        detected_conditions["STEMI"] = True
    elif random.random() < 0.4: # 40% chance of simulating an NSTEMI detection
        detected_conditions["NSTEMI"] = True
    elif random.random() < 0.5: # 50% chance of simulating Unstable Angina detection
        detected_conditions["Unstable Angina"] = True

    # Ensure only one type of acute coronary syndrome is detected at a time
    if detected_conditions["STEMI"]:
        detected_conditions["NSTEMI"] = False
        detected_conditions["Unstable Angina"] = False
    elif detected_conditions["NSTEMI"]:
         detected_conditions["Unstable Angina"] = False


    print(f"ECG Analysis Agent: Detected conditions: {detected_conditions}")

    return detected_conditions

# Placeholder for simulated ECG data structure
# In a real scenario, this would be actual signal data or processed features
# For the demo, it can be a simple dictionary or even None
def get_simulated_ecg_data():
    """Simulates obtaining ECG data."""
    print("Simulating getting ECG data...")
    # In a real application, this would load or receive actual ECG data
    return {"lead_v1": [random.random() for _ in range(100)],
            "lead_v2": [random.random() for _ in range(100)]} # Placeholder data

if __name__ == '__main__':
    # Example usage of the agent
    simulated_data = get_simulated_ecg_data()
    results = analyze_ecg(simulated_data)
    print(f"Analysis Results: {results}")