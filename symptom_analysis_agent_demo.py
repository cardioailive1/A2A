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

    # Simple keyword matching for demo purposes
    # Symptoms for Heart Attack
    if "chest pain" in symptoms_lower or "discomfort" in symptoms_lower:
        potential_conditions.append("Heart Attack")

    # Symptoms for Heart Failure, also considering other conditions
    if "shortness of breath" in symptoms_lower or "difficulty breathing" in symptoms_lower:
        potential_conditions.append("Heart Failure")
        potential_conditions.append("Aortic Stenosis") # Can cause shortness of breath
        potential_conditions.append("Aortic Regurgitation") # Can cause shortness of breath
        potential_conditions.append("Mitral Regurgitation") # Can cause shortness of breath
        potential_conditions.append("Dilated Cardiomyopathy") # Can cause shortness of breath

    if "fatigue" in symptoms_lower or "tiredness" in symptoms_lower:
        potential_conditions.append("Heart Failure") # Fatigue is a symptom of heart failure
        potential_conditions.append("Aortic Regurgitation") # Can cause fatigue
        potential_conditions.append("Mitral Regurgitation") # Can cause fatigue
        potential_conditions.append("Dilated Cardiomyopathy") # Can cause fatigue

    if "swelling" in symptoms_lower or "edema" in symptoms_lower:
        potential_conditions.append("Heart Failure") # Swelling is a symptom of heart failure
        potential_conditions.append("Mitral Regurgitation") # Can cause swelling
        potential_conditions.append("Dilated Cardiomyopathy") # Can cause swelling

    # Specific symptoms for other conditions
    if "dizziness" in symptoms_lower or "syncope" in symptoms_lower:
        potential_conditions.append("Aortic Stenosis")
    if "bounding pulse" in symptoms_lower:
        potential_conditions.append("Aortic Regurgitation")
    if "palpitations" in symptoms_lower or "irregular heartbeat" in symptoms_lower:
        potential_conditions.append("Mitral Regurgitation")
        potential_conditions.append("Dilated Cardiomyopathy")

    if "palpitation" in symptoms_lower:
        potential_conditions.append("Cardiac Arrhythmia")


    # Remove duplicates
    potential_conditions = list(set(potential_conditions))

    print(f"Symptom Analysis Agent: Analyzing symptoms: '{symptoms}'")
    print(f"Symptom Analysis Agent: Identified potential conditions: {potential_conditions}")

    return potential_conditions

if __name__ == '__main__':
    # Example usage
    test_symptoms_1 = "I have severe chest pain and a little shortness of breath."
    conditions_1 = analyze_symptoms(test_symptoms_1)
    print(f"Results for '{test_symptoms_1}': {conditions_1}\n")

    test_symptoms_2 = "I've been experiencing fatigue and swelling in my ankles."
    conditions_2 = analyze_symptoms(test_symptoms_2)
    print(f"Results for '{test_symptoms_2}': {conditions_2}\n")

    test_symptoms_3 = "Just a headache."
    conditions_3 = analyze_symptoms(test_symptoms_3)
    print(f"Results for '{test_symptoms_3}': {conditions_3}\n")