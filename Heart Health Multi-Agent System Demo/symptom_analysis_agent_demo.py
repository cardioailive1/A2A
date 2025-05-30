def analyze_symptoms(symptoms: str) -> list[str]:
    """
    Analyzes user-provided symptoms to identify potential conditions
    (simplified for heart attack and heart failure demo).

    Args:
        symptoms: A string containing the user's symptoms.

    Returns:
        A list of potential conditions.
    """
    potential_conditions = []
    symptoms_lower = symptoms.lower()

    if "palpitation" in symptoms_lower:
        potential_conditions.append("Cardiac Arrhythmia")

    # Add more symptom checks here for other conditions
    # Example for Heart Attack (simplified):
    if any(word in symptoms_lower for word in ["chest pain", "shortness of breath", "arm pain"]):
        if "Heart Attack" not in potential_conditions:
            potential_conditions.append("Heart Attack")

    # Example for Heart Failure (simplified):
    if any(word in symptoms_lower for word in ["swelling", "fatigue", "difficulty breathing"]):
        if "Heart Failure" not in potential_conditions:
            potential_conditions.append("Heart Failure")
    #