# orchestration_service_demo.py

from symptom_analysis_agent_demo import analyze_symptoms
from cardiac_arrhythmia_analysis_agent import analyze_arrhythmia

# Placeholder for Diagnostic Agent
def diagnose_placeholder(potential_conditions, patient_data, echo_analysis=None):
    """Placeholder for Diagnostic Agent."""
    print(f"Orchestration: Sending potential conditions and patient data for diagnosis: {potential_conditions}, {patient_data}")
    # Simplified logic: based on potential conditions and basic patient data
    diagnosis = "Undetermined"
    # Include ECG analysis results in diagnosis logic
    ecg_results = patient_data.get("ecg_analysis", {})

    if "Heart Attack" in potential_conditions:
        if ecg_results.get("STEMI"):
            diagnosis = "STEMI (ST-Elevation Myocardial Infarction)"
        elif ecg_results.get("NSTEMI"):
            diagnosis = "NSTEMI (Non-ST-Elevation Myocardial Infarction)"
    elif "Heart Failure" in potential_conditions:
        # Check for signs of heart failure based on echo or patient data
        if echo_analysis and echo_analysis.get("ejection_fraction") == "Reduced":
            diagnosis = "Heart Failure with Reduced Ejection Fraction (HFrEF)"
        elif echo_analysis and echo_analysis.get("chamber_size") == "Enlarged":
            diagnosis = "Heart Failure (likely due to chamber enlargement)"
        elif patient_data.get("has_history", False): # Fallback if no echo or echo normal but symptoms present
            diagnosis = "Heart Failure (clinical suspicion)" # Indent this line correctly
    elif potential_conditions and "Unknown" not in potential_conditions:
        # If Cardiac Arrhythmia is a potential condition, refine diagnosis if arrhythmia analysis available
        if "Cardiac Arrhythmia" in potential_conditions and patient_data.get("cardiac_arrhythmia_analysis"):
            arrhythmia_results = patient_data["cardiac_arrhythmia_analysis"]
            if arrhythmia_results.get("arrhythmia_detected"):
                arrhythmia_type = arrhythmia_results.get('arrhythmia_type', 'Undetermined Type')
                # Check for specific subtypes if available
                if arrhythmia_results.get("Afib"):
                    diagnosis = "Cardiac Arrhythmia: Atrial Fibrillation (Afib)"
                elif arrhythmia_results.get("SVT"):
                    diagnosis = "Cardiac Arrhythmia: Supraventricular Tachycardia (SVT)"
                elif arrhythmia_results.get("VT"):
                    diagnosis = "Cardiac Arrhythmia: Ventricular Tachycardia (VT)"
                elif arrhythmia_results.get("VFib"):
                    diagnosis = "Cardiac Arrhythmia: Ventricular Fibrillation (VFib)"
                else:
                    diagnosis = f"Cardiac Arrhythmia: {arrhythmia_type}"
            else:
                diagnosis = "Cardiac Arrhythmia (no specific type detected by analysis)"
         diagnosis = f"Investigate: {', '.join(potential_conditions)}"
    else:
        diagnosis = "Further evaluation needed"


    print(f"Orchestration: Received diagnosis: {diagnosis}")
    return diagnosis

def plan_treatment_placeholder(diagnosis, patient_data, echo_analysis=None):
    """Placeholder for Treatment Planning Agent."""
    print(f"Orchestration: Sending diagnosis and patient data for treatment planning: {diagnosis}, {patient_data}")
    # Simplified logic: based on diagnosis
    treatment_plan = "Consult a medical professional for a personalized plan."
    if "Heart Attack" in diagnosis:
        treatment_plan = "Seek immediate medical attention. Treatment is critical and depends on the type of heart attack. May include medication (aspirin, nitroglycerin), angioplasty, or bypass surgery."
    elif "STEMI" in diagnosis:
        treatment_plan = "Immediate reperfusion therapy (PCI or fibrinolysis) is crucial for STEMI. Also includes medications (aspirin, heparin, antiplatelets)."
    elif "NSTEMI" in diagnosis or "Unstable Angina" in diagnosis:
        treatment_plan = "Medical management with antiplatelets, anticoagulants, and other medications. May require angiography and intervention."
    elif "Heart Failure" in diagnosis: # Keep general Heart Failure treatment for cases not linked to acute MI in this demo
        if echo_analysis and echo_analysis.get("ejection_fraction") == "Reduced":
            treatment_plan = "Treatment for HFrEF includes ACE inhibitors, beta-blockers, MRAs, and potentially ARNI or SGLT2 inhibitors. Consider device therapy if indicated."
        elif echo_analysis and echo_analysis.get("chamber_size") == "Enlarged":
            treatment_plan = "Focus on managing underlying cause of enlargement. Treatment may include medications to reduce workload and fluid (diuretics). Consider devices."
        # Fallback for clinical suspicion or other types not explicitly handled
        treatment_plan = "Treatment may include lifestyle changes (diet, exercise), medication (ACE inhibitors, beta-blockers), and potentially devices (pacemaker, defibrillator)."
    elif "Cardiac Arrhythmia" in diagnosis:
        if "Afib" in diagnosis:
            treatment_plan = "Treatment for Atrial Fibrillation may include rate control or rhythm control medications, anticoagulation to prevent stroke, and lifestyle changes."
        elif "SVT" in diagnosis or "VT" in diagnosis or "VFib" in diagnosis:
             treatment_plan = "Treatment for HFrEF includes ACE inhibitors, beta-blockers, MRAs, and potentially ARNI or SGLT2 inhibitors. Consider device therapy if indicated."
        elif echo_analysis and echo_analysis.get("chamber_size") == "Enlarged":
             treatment_plan = "Focus on managing underlying cause of enlargement. Treatment may include medications to reduce workload and fluid (diuretics). Consider devices."
        # Fallback for clinical suspicion or other types not explicitly handled
        treatment_plan = "Treatment may include lifestyle changes (diet, exercise), medication (ACE inhibitors, beta-blockers), and potentially devices (pacemaker, defibrillator)."

    print(f"Orchestration: Received treatment plan: {treatment_plan}")
    return treatment_plan


class OrchestrationServiceDemo:
    def process_symptoms(self, symptoms):
        """
        Orchestrates the agent interactions to process symptoms, optionally analyze ECG,
        diagnose (including heart attack subtypes), and plan treatment.
        """
        print("\n--- Orchestration Service: Starting symptom processing ---")

        # Simplified in-memory patient data for the demo
        patient_data = {
            "age": 55,
            "has_history": True, # Simulate a patient with a relevant medical history
            "ecg_data": "simulated_ecg_waveform" # Simulate presence of ECG data
        }
        print(f"Orchestration: Using simplified patient data: {patient_data}")

        # Placeholder for ECG analysis agent (define this function separately)
        def analyze_ecg_placeholder(ecg_data):
            print(f"Orchestration: Sending simulated ECG data for analysis: {ecg_data}")
            # Simplified logic for demo: simulate detection based on keywords or assumptions
            # In a real scenario, this would involve complex signal processing and ML models
            if "chest pain" in symptoms.lower(): # Simple coupling to symptoms for demo
                 return {"STEMI": True, "NSTEMI": False, "Unstable Angina": False}
            return {"STEMI": False, "NSTEMI": False, "Unstable Angina": False}

        # Placeholder for Echocardiogram Analysis Agent
        def analyze_echo_placeholder(echo_data):
            print(f"Orchestration: Sending simulated Echo data for analysis: {echo_data}")
            # Simplified logic for demo: simulate results
            return {
                "ejection_fraction": "Reduced" if "shortness of breath" in symptoms.lower() and patient_data.get("age", 50) > 60 else "Normal",
                "valve_function": "Normal",
                "chamber_size": "Enlarged" if patient_data.get("bmi", 25) > 30 else "Normal",
                "regional_wall_motion_abnormalities": False
            }

        # 1. Call Symptom Analysis Agent
        print(f"Orchestration: Sending symptoms for analysis: {symptoms}")
        potential_conditions = analyze_symptoms(symptoms)
        print(f"Orchestration: Received potential conditions from symptom analysis: {potential_conditions}")

        # 2. Optional: Call ECG Analysis Agent if heart attack is suspected
        ecg_analysis_results = {}
        if "Heart Attack" in potential_conditions and patient_data.get("ecg_data"):
            print("Orchestration: Potential heart attack detected, proceeding with ECG analysis...")
            ecg_analysis_results = analyze_ecg_placeholder(patient_data["ecg_data"])
            patient_data["ecg_analysis"] = ecg_analysis_results # Add results to patient data
            print(f"Orchestration: Received ECG analysis results: {ecg_analysis_results}")

        # 3. Optional: Call Echocardiogram Analysis Agent if heart failure is suspected
        echo_analysis_results = {}
        if "Heart Failure" in potential_conditions:
            print("Orchestration: Potential heart failure detected, proceeding with Echocardiogram analysis...")
            # Simulate some echo data if needed, or pass None if not available
            echo_analysis_results = analyze_echo_placeholder("simulated_echo_data")
            patient_data["echo_analysis"] = echo_analysis_results # Add results to patient data
            print(f"Orchestration: Received Echo analysis results: {echo_analysis_results}")

        # Optional: Call Cardiac Arrhythmia Analysis Agent if cardiac arrhythmia is suspected
        arrhythmia_analysis_results = {}
        if "Cardiac Arrhythmia" in potential_conditions and patient_data.get("ecg_data_for_arrhythmia"): # Use specific key for arrhythmia data
            print("Orchestration: Potential cardiac arrhythmia detected, proceeding with ECG data analysis for arrhythmia...")
            # Assuming patient_data contains relevant info for arrhythmia analysis (like age, symptoms)
            # Ensure analyze_arrhythmia is called with appropriate data
            cardiac_arrhythmia_analysis_results = analyze_arrhythmia(patient_data.get("ecg_data_for_arrhythmia", {}), patient_data)
            patient_data["cardiac_arrhythmia_analysis"] = cardiac_arrhythmia_analysis_results # Add results to patient data
            print(f"Orchestration: Received Cardiac Arrhythmia analysis results: {cardiac_arrhythmia_analysis_results}")

        # 4. Call Diagnostic Agent (including potential ECG and Echo results)
        diagnosis = diagnose_placeholder(potential_conditions, patient_data, echo_analysis=echo_analysis_results, arrhythmia_analysis=cardiac_arrhythmia_analysis_results)

        # 5. Call Treatment Planning Agent (including potential ECG and Echo results)
        treatment_plan = plan_treatment_placeholder(diagnosis, patient_data, echo_analysis=echo_analysis_results)

        print("--- Orchestration Service: Symptom processing finished ---\n")

        return {
            "diagnosis": diagnosis,
            "treatment_plan": treatment_plan
        }

if __name__ == "__main__":
    # Example usage (for testing the orchestration logic directly)
    test_symptoms = "chest pain and shortness of breath"
    orchestrator = OrchestrationServiceDemo()
    result = orchestrator.process_symptoms(test_symptoms)
    print("Demo Orchestration Result:")
    print(f"Diagnosis: {result['diagnosis']}")
    print(f"Treatment Plan: {result['treatment_plan']}")

    print("\n--- Another test case ---")
    test_symptoms_2 = "fatigue and swollen ankles"
    result_2 = orchestrator.process_symptoms(test_symptoms_2)
    print("Demo Orchestration Result:")
    print(f"Diagnosis: {result_2['diagnosis']}")
    print(f"Treatment Plan: {result_2['treatment_plan']}")