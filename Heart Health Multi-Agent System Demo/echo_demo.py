# echocardiogram_integration_demo.py

import json
import time
from typing import Dict, Any

# Assume these are imports from your existing system
# from diagnostic_agent_demo import diagnose as original_diagnose
# from treatment_planning_agent_demo import treatment_planning as original_treatment_planning

# --- Simulated Echocardiogram Analysis ---

def simulate_echocardiogram_analysis() -> Dict[str, Any]:
    """
    Simulates the analysis of echocardiogram data and returns structured findings.
    In a real system, this would involve processing actual image data
    or receiving structured data from an analysis system.

    Returns:
        Dict[str, Any]: A dictionary containing simulated echocardiogram findings.
    """
    print("Simulating echocardiogram analysis...")
    # Simple simulation based on age and symptoms
    simulated_results = {
        "ejection_fraction": "Normal" if patient_data.get("age", 50) < 60 and "shortness of breath" not in patient_data.get("symptoms", "").lower() and patient_data.get("bmi", 25) < 30 else "Reduced",
        "valve_function": "Normal",
        "chamber_size": "Normal",
        "regional_wall_motion_abnormalities": True if patient_data.get("age", 50) > 65 and "chest pain" in patient_data.get("symptoms", "").lower() else False
    }

    if patient_data.get("age", 50) > 75 and "murmur" in patient_data.get("symptoms", "").lower():
        simulated_results["valve_function"] = "Abnormal (e.g., Aortic Stenosis)"
    elif patient_data.get("age", 50) > 65 and "shortness of breath" in patient_data.get("symptoms", "").lower():
        simulated_results["valve_function"] = "Abnormal (e.g., Aortic Regurgitation)"
    elif "murmur" in patient_data.get("symptoms", "").lower():
         simulated_results["valve_function"] = "Abnormal (e.g., Mitral Regurgitation)"

    if simulated_results["ejection_fraction"] == "Reduced" and patient_data.get("bmi", 25) >= 30:
        simulated_results["chamber_size"] = "Enlarged"

    print(f"Echocardiogram results: {simulated_results}")
    return simulated_results

# --- Modified Agent Functions (Simulated) ---

# We'll create modified versions here to avoid altering the original files
# In a real implementation, you would modify the actual files.

def diagnose_with_echo(patient_data: Dict[str, Any], echo_data: Dict[str, Any]) -> str:
    """
    Simulates the diagnostic agent considering patient data and echocardiogram results.
    """
    print("\nDiagnostic Agent (with Echocardiogram Data):")
    diagnosis = "Initial assessment based on symptoms."

    if echo_data.get("ejection_fraction") == "Reduced" and echo_data.get("chamber_size") == "Enlarged":
        diagnosis = "Possible Dilated Cardiomyopathy and Heart Failure."
    elif echo_data.get("valve_function") == "Abnormal (e.g., Aortic Stenosis)":
        diagnosis = "Possible Aortic Stenosis. Further evaluation needed."
    elif echo_data.get("valve_function") == "Abnormal (e.g., Aortic Regurgitation)":
        diagnosis = "Possible Aortic Regurgitation. Further evaluation needed."
    elif echo_data.get("valve_function") == "Abnormal (e.g., Mitral Regurgitation)":
        diagnosis = "Possible Mitral Regurgitation. Further evaluation needed."
    elif echo_data.get("ejection_fraction") == "Reduced":
        diagnosis = "Reduced ejection fraction detected. Investigate underlying cause (e.g., Heart Failure, Cardiomyopathy)."
    elif echo_data.get("chamber_size") == "Enlarged":
        diagnosis = "Enlarged heart chambers detected. Investigate underlying cause (e.g., Heart Failure, Cardiomyopathy)."
    elif echo_data.get("regional_wall_motion_abnormalities"):
        diagnosis = "Regional wall motion abnormalities detected. Suggests possible ischemic heart disease or prior infarction."

    else:
        diagnosis += " Echocardiogram results are largely normal, refining diagnosis based on symptoms."

    # Combine with some basic symptom logic (simplified)
    if "chest pain" in patient_data.get("symptoms", "").lower() and echo_data.get("ejection_fraction") == "Normal":
        diagnosis += " Consider angina despite normal ejection fraction."

    final_diagnosis = f"Diagnosis: {diagnosis}"
    print(final_diagnosis)
    return final_diagnosis

def treatment_planning_with_echo(diagnosis: str, echo_data: Dict[str, Any]) -> str:
    """
    Simulates the treatment planning agent considering diagnosis and echocardiogram results.
    """
    print("\nTreatment Planning Agent (with Echocardiogram Data):")
    treatment_plan = "General recommendations based on diagnosis."

    if "Dilated Cardiomyopathy" in diagnosis or "Heart Failure" in diagnosis:
        treatment_plan = "Management for Heart Failure, including medications (ACE inhibitors, beta-blockers, diuretics), lifestyle changes, and potentially devices."
    elif "Aortic Stenosis" in diagnosis:
        treatment_plan = "Management for Aortic Stenosis. Severe cases may require valve replacement (TAVR or SAVR)."
    elif "Aortic Regurgitation" in diagnosis:
        treatment_plan = "Management for Aortic Regurgitation. Severe cases may require valve repair or replacement."
    elif "Mitral Regurgitation" in diagnosis:
         treatment_plan = "Management for Mitral Regurgitation. Severe cases may require valve repair or replacement."
    elif echo_data.get("ejection_fraction") == "Reduced":
        treatment_plan = "Investigate cause of reduced ejection fraction. May require heart failure medications."
    elif echo_data.get("chamber_size") == "Enlarged":
         treatment_plan = "Investigate cause of enlarged chambers. May require heart failure medications or other interventions."
    elif echo_data.get("regional_wall_motion_abnormalities"):
         treatment_plan = "Further investigation for ischemic heart disease (e.g., angiography). Medical management for coronary artery disease may be needed."
    elif "heart failure" in diagnosis.lower() or echo_data.get("ejection_fraction") == "Reduced":
        treatment_plan = "Recommend medications for heart failure (e.g., ACE inhibitors, beta-blockers)."
        if echo_data.get("chamber_size") == "Enlarged": # This might be redundant with the Cardiomyopathy/Heart Failure case above, consider refining logic
            treatment_plan += " Consider diuretics."
    else:
        treatment_plan += " Focus on managing primary symptoms and risk factors."

    final_plan = f"Treatment Plan: {treatment_plan}"
    print(final_plan)
    return final_plan

# --- Updated Demo Flow ---

def run_echo_integration_demo():
    """
    Runs a demo scenario incorporating echocardiogram data into the agent workflow.
    """
    print("--- Starting Echocardiogram Integration Demo ---")

    # Simulate patient data
    patient_data = {
        "age": 70,
        "gender": "Male",
        "symptoms": "Shortness of breath, fatigue, ankle swelling",
        "medical_history": "Hypertension",
        "bmi": 32
    }
    print("\nPatient Data:", json.dumps(patient_data, indent=2))

    # Simulate echocardiogram analysis
    echocardiogram_results = simulate_echocardiogram_analysis()

    # Pass data to modified diagnostic agent
    diagnosis = diagnose_with_echo(patient_data, echocardiogram_results)

    # Pass diagnosis and echo data to modified treatment planning agent
    treatment_plan = treatment_planning_with_echo(diagnosis, echocardiogram_results)

    print("\n--- Demo Complete ---")
    print("Final Diagnosis:", diagnosis)
    print("Final Treatment Plan:", treatment_plan)

if __name__ == "__main__":
    run_echo_integration_demo()