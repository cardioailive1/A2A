# diagnostic_agent_demo.py

def diagnose(potential_conditions, patient_data, ecg_analysis_results=None, echocardiogram_data=None):
    """
    Simplified Diagnostic Agent for the demo.
    Provides a diagnosis (Heart Attack, Heart Failure, STEMI, NSTEMI,
    Unstable Angina, or Undetermined) based on potential conditions,
    simulated patient data, and ECG analysis results.

    Args:
        potential_conditions (list): A list of potential medical conditions.
        patient_data (dict): A dictionary of simulated patient data
                             (e.g., {'age': 65, 'has_history_heart_disease': True}).
        ecg_analysis_results (dict, optional): A dictionary containing
                                               ECG analysis results
                                               (e.g., {'STEMI': True,
                                               'NSTEMI': False,
                                               'Unstable Angina': False}).
        echocardiogram_data (dict, optional): A dictionary containing
                                               echocardiogram analysis results.
                                               Defaults to None.

    Returns:
        str: The diagnosis ('Heart Attack', 'Heart Failure', 'STEMI',
             'NSTEMI', 'Unstable Angina', 'Heart Failure', or 'Undetermined').
    """
    print(f"Diagnostic Agent received potential conditions: {potential_conditions}")
    print(f"Diagnostic Agent received patient data: {patient_data}")
    print(f"Diagnostic Agent received ECG analysis results: {ecg_analysis_results}")

    # Simplified diagnostic logic for demo purposes
    diagnosis = "Undetermined"

    # Prioritize diagnosis based on detailed ECG analysis if available
    if ecg_analysis_results:
        if ecg_analysis_results.get('STEMI'):
            diagnosis = "STEMI"
            if ecg_analysis_results.get('ST_elevation_leads'):
                diagnosis += f" (ST elevation in {', '.join(ecg_analysis_results['ST_elevation_leads'])})"
                print(f"Diagnostic Agent: ECG analysis indicates STEMI with ST elevation in leads {', '.join(ecg_analysis_results['ST_elevation_leads'])}")
            else:
                print("Diagnostic Agent: ECG analysis indicates STEMI (location undetermined from results).")

        elif ecg_analysis_results.get('NSTEMI'):
            diagnosis = "NSTEMI"
            if ecg_analysis_results.get('ST_depression_leads'):
                 diagnosis += f" (ST depression in {', '.join(ecg_analysis_results['ST_depression_leads'])})"
                 print(f"Diagnostic Agent: ECG analysis indicates NSTEMI with ST depression in leads {', '.join(ecg_analysis_results['ST_depression_leads'])}")
            else:
                print("Diagnostic Agent: ECG analysis indicates NSTEMI (location undetermined from results).")

        elif ecg_analysis_results.get('Unstable Angina'):
            diagnosis = "Unstable Angina"
            if ecg_analysis_results.get('T_wave_inversion_leads'):
                diagnosis += f" (T-wave inversion in {', '.join(ecg_analysis_results['T_wave_inversion_leads'])})"
                print(f"Diagnostic Agent: ECG analysis indicates Unstable Angina with T-wave inversion in leads {', '.join(ecg_analysis_results['T_wave_inversion_leads'])}")
            else:
                 print("Diagnostic Agent: ECG analysis indicates Unstable Angina (location undetermined from results).")

    # Consider echocardiogram data if available and if no specific ECG diagnosis
    if diagnosis == "Undetermined" and echocardiogram_data:
        if echocardiogram_data.get('ejection_fraction') is not None and echocardiogram_data['ejection_fraction'] < 40:
            diagnosis = "Heart Failure"

    # If no specific diagnosis from ECG, consider potential conditions and patient data
    if diagnosis == "Undetermined":
        if "Heart Attack" in potential_conditions:
            # More sophisticated logic would be here in a real system,
            # considering specific symptoms, patient history, and test results.
            if patient_data.get('age', 0) > 50 or patient_data.get('has_history_heart_disease', False):
                 diagnosis = "Heart Attack"
            elif "chest pain" in patient_data.get('symptoms', '').lower() and "shortness of breath" in patient_data.get('symptoms', '').lower():
                 diagnosis = "Heart Attack"


        elif "Heart Failure" in potential_conditions:
             # Again, simplified logic. Real system would use more criteria.
             if patient_data.get('age', 0) > 60 or patient_data.get('has_high_blood_pressure', False):
                 diagnosis = "Heart Failure"
             elif "fatigue" in patient_data.get('symptoms', '').lower() and "swelling in legs" in patient_data.get('symptoms', '').lower():
                 diagnosis = "Heart Failure"


    print(f"Diagnostic Agent determined diagnosis: {diagnosis}")
    return diagnosis

if __name__ == '__main__':
    # Example usage with ECG analysis:
    sample_potential_conditions_ecg = ["Heart Attack", "Angina"]
    sample_patient_data_ecg = {
        'age': 68,
        'has_history_heart_disease': True,
        'symptoms': 'Severe chest pain and shortness of breath'
    }
    sample_ecg_results_stemi = {'STEMI': True, 'NSTEMI': False, 'Unstable Angina': False}
    diagnosis_result_ecg_stemi = diagnose(sample_potential_conditions_ecg, sample_patient_data_ecg, sample_ecg_results_stemi)
    print(f"Demo Diagnosis Result with STEMI ECG: {diagnosis_result_ecg_stemi}")
    print("\\n---")

    sample_ecg_results_nstemi = {'STEMI': False, 'NSTEMI': True, 'Unstable Angina': False, 'ST_depression_leads': ['V4', 'V5', 'V6']}
    diagnosis_result_ecg_nstemi = diagnose(sample_potential_conditions_ecg, sample_patient_data_ecg, sample_ecg_results_nstemi)
    print(f"Demo Diagnosis Result with NSTEMI ECG: {diagnosis_result_ecg_nstemi}")
    print("\\n---")

    sample_ecg_results_ua = {'STEMI': False, 'NSTEMI': False, 'Unstable Angina': True, 'T_wave_inversion_leads': ['I', 'aVL']}
    diagnosis_result_ecg_ua = diagnose(sample_potential_conditions_ecg, sample_patient_data_ecg, sample_ecg_results_ua)
    print(f"Demo Diagnosis Result with Unstable Angina ECG: {diagnosis_result_ecg_ua}")
    print("\\n---")