# echo_demo.py

import random
import numpy as np
import matplotlib.pyplot as plt

# Simulate more realistic ECG data
def simulate_ecg_data():
    """
    Simulates realistic ECG data with potential patterns for STEMI, NSTEMI, or Unstable Angina.
    Includes different leads and voltage values over time.
    """
    # Define leads
    leads = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
    data = {lead: [] for lead in leads}

    # Simulate normal sinus rhythm as a base
    time = np.linspace(0, 2, 200) # 2 seconds of data
    qrs_duration = 0.08
    pr_interval = 0.16
    qt_interval = 0.40

    for t in time:
        # Simulate P wave (simplified)
        p_wave = 0.1 * np.sin(np.pi * t / pr_interval) if 0 <= t < pr_interval else 0

        # Simulate QRS complex (simplified)
        qrs = 0
        if pr_interval <= t < pr_interval + qrs_duration:
            qrs = -1.0 * np.exp(-(t - pr_interval - qrs_duration/2)**2 / 0.001) # Q wave
            qrs += 2.0 * np.exp(-(t - pr_interval - qrs_duration/2)**2 / 0.0005) # R wave
            qrs -= 0.5 * np.exp(-(t - pr_interval - qrs_duration/2)**2 / 0.001) # S wave


        # Simulate T wave (simplified)
        t_wave = 0
        if pr_interval + qrs_duration <= t < qt_interval:
             t_wave = 0.3 * np.sin(np.pi * (t - (pr_interval + qrs_duration)) / (qt_interval - (pr_interval + qrs_duration)))

        # Combine components
        voltage = p_wave + qrs + t_wave

        # Add some noise
        voltage += random.gauss(0, 0.05)

        for lead in leads:
            # Apply lead-specific variations (simplified)
            lead_voltage = voltage
            if lead in ['II', 'III', 'aVF']: # Inferior leads
                lead_voltage += 0.1 * np.sin(np.pi * t / 1) if 0.4 <= t < 0.6 else 0 # Simulate minor ST segment
            elif lead in ['V2', 'V3']: # Anterior leads
                 lead_voltage += 0.2 * np.sin(np.pi * t / 1) if 0.4 <= t < 0.6 else 0 # Simulate minor ST segment
            elif lead in ['V4', 'V5', 'V6']: # Lateral leads
                lead_voltage -= 0.05 * np.sin(np.pi * t / 1) if 0.4 <= t < 0.6 else 0 # Simulate minor ST segment

            data[lead].append(lead_voltage)

    # Introduce potential abnormalities
    abnormality_type = random.choice(['STEMI', 'NSTEMI', 'Unstable Angina', 'None'])
    if abnormality_type == 'STEMI':
        # Simulate ST elevation in specific leads
        stemi_leads = random.choice([['V2', 'V3'], ['II', 'III', 'aVF'], ['I', 'aVL'], ['V4'], ['V5', 'V6']]) # Anterior, Inferior, Lateral, Anterior, Lateral
        for lead in stemi_leads:
            if lead in data:
                for i in range(int(0.4 * len(time)), int(0.6 * len(time))): # Simulate ST elevation over a segment
                    data[lead][i] += random.uniform(0.1, 0.5) # Add significant elevation

    elif abnormality_type == 'NSTEMI' or abnormality_type == 'Unstable Angina':
        # Simulate ST depression or T-wave inversion
        abnormal_leads = random.sample(leads, random.randint(2, 5))
        for lead in abnormal_leads:
            if lead in data:
                for i in range(int(0.4 * len(time)), int(0.7 * len(time))): # Simulate ST depression or T-wave inversion over a segment
                    if random.random() < 0.5: # 50% chance of depression vs inversion
                         data[lead][i] -= random.uniform(0.05, 0.2) # Simulate depression
                    else:
                        data[lead][i] *= -1 # Simulate inversion

    return data, abnormality_type


# Analyze simulated ECG patterns
def analyze_ecg_patterns(ecg_data):
    """
    Analyzes simulated ECG data to identify patterns indicative of STEMI, NSTEMI, or Unstable Angina.
    (Simplified analysis based on simulated data characteristics)
    """
    analysis_results = {
        'STEMI': {'detected': False, 'leads': []},
        'NSTEMI': {'detected': False, 'leads': []},
        'Unstable Angina': {'detected': False, 'leads': []}
    }

    # Analyze each lead for abnormalities
    for lead, voltages in ecg_data.items():
        # Simplified detection based on simulated patterns
        st_segment = voltages[int(0.4 * len(voltages)):int(0.6 * len(voltages))]
        t_wave_segment = voltages[int(0.6 * len(voltages)):int(0.7 * len(voltages))]

        # Check for significant ST elevation (indicative of STEMI)
        if np.mean(st_segment) > 0.15: # Threshold for elevation
             analysis_results['STEMI']['detected'] = True
             analysis_results['STEMI']['leads'].append(lead)
        # Check for significant ST depression or T-wave inversion (indicative of NSTEMI or Unstable Angina)
        elif np.mean(st_segment) < -0.05 or np.mean(t_wave_segment) < -0.1: # Thresholds for depression/inversion
             # Differentiate between NSTEMI and Unstable Angina based on a simulated factor
             if random.random() < 0.7: # Simulate higher chance of NSTEMI if abnormalities detected
                 analysis_results['NSTEMI']['detected'] = True
                 analysis_results['NSTEMI']['leads'].append(lead)
             else:
                 analysis_results['Unstable Angina']['detected'] = True
                 analysis_results['Unstable Angina']['leads'].append(lead)


    return analysis_results

# Simulate echocardiogram analysis (from echo_demo.py)
def simulate_echocardiogram_data():
    """
    Simulates echocardiogram analysis results.
    """
    echocardiogram_results = {
        'ejection_fraction': random.uniform(30, 65),  # Simulate ejection fraction
        'wall_motion': random.choice(['Normal', 'Hypokinetic', 'Akinetic']), # Simulate wall motion
        'regional_wall_motion_abnormalities': random.choice([True, False]) # Simulate regional wall motion abnormalities
    }
    print(f"Simulated Echocardiogram Data: {echocardiogram_results}")
    return echocardiogram_results


# Dummy diagnostic and treatment planning functions (replace with actual agent calls)
def diagnose(patient_data, ecg_analysis_results=None, echocardiogram_data=None):
    """
    Simplified diagnostic function that takes ECG and echocardiogram data.
    """
    diagnosis = "Undetermined"
    print(f"Diagnostic Agent received patient data: {patient_data}")
    print(f"Diagnostic Agent received ECG analysis results: {ecg_analysis_results}")
    print(f"Diagnostic Agent received echocardiogram data: {echocardiogram_data}")

    if ecg_analysis_results and ecg_analysis_results.get('STEMI', {}).get('detected'):
        diagnosis = "STEMI (ST-Elevation Myocardial Infarction)"
        print(f"Based on ECG showing STEMI in leads {ecg_analysis_results['STEMI']['leads']}")
    elif ecg_analysis_results and ecg_analysis_results.get('NSTEMI', {}).get('detected'):
        diagnosis = "NSTEMI (Non-ST-Elevation Myocardial Infarction)"
        print(f"Based on ECG showing NSTEMI patterns in leads {ecg_analysis_results['NSTEMI']['leads']}")
    elif ecg_analysis_results and ecg_analysis_results.get('Unstable Angina', {}).get('detected'):
        diagnosis = "Unstable Angina"
        print(f"Based on ECG showing Unstable Angina patterns in leads {ecg_analysis_results['Unstable Angina']['leads']}")
    elif echocardiogram_data and echocardiogram_data.get('ejection_fraction') is not None and echocardiogram_data['ejection_fraction'] < 40:
        diagnosis = "Heart Failure (likely reduced ejection fraction)"
        print(f"Based on echocardiogram showing low ejection fraction: {echocardiogram_data['ejection_fraction']}%")
    elif echocardiogram_data and echocardiogram_data.get('regional_wall_motion_abnormalities'):
        diagnosis = "Possible Myocardial Ischemia/Infarction (based on wall motion abnormalities)"
        print("Based on echocardiogram showing regional wall motion abnormalities.")


    print(f"Diagnostic Agent determined diagnosis: {diagnosis}")
    return diagnosis

def plan_treatment(diagnosis, patient_data, echocardiogram_data=None):
    """
    Simplified treatment planning function that considers echocardiogram data.
    """
    treatment_plan = "No specific treatment plan determined."
    print(f"Treatment Planning Agent received diagnosis: {diagnosis}")
    print(f"Treatment Planning Agent received patient data: {patient_data}")
    print(f"Treatment Planning Agent received echocardiogram data: {echocardiogram_data}")


    if "STEMI" in diagnosis:
        treatment_plan = "Suggested Treatment Plan for STEMI:\n- Immediate reperfusion therapy (PCI or fibrinolysis)\n- Medications (aspirin, P2Y12 inhibitors, anticoagulants, beta-blockers, statins)"
    elif "NSTEMI" in diagnosis or "Unstable Angina" in diagnosis:
        treatment_plan = "Suggested Treatment Plan for NSTEMI/Unstable Angina:\n- Medical management (aspirin, P2Y12 inhibitors, anticoagulants, beta-blockers, statins)\n- Risk stratification and potential invasive strategy"
    elif "Heart Failure" in diagnosis:
        treatment_plan = "Suggested Treatment Plan for Heart Failure:\n- Medications to manage symptoms (ACE inhibitors, beta-blockers, diuretics)\n- Lifestyle changes (sodium restriction, fluid management)"
        if echocardiogram_data and echocardiogram_data.get('ejection_fraction') is not None and echocardiogram_data['ejection_fraction'] < 35:
             treatment_plan += "\n- Consider advanced heart failure therapies (e.g., ICD, CRT, transplant evaluation)"

    elif "Possible Myocardial Ischemia/Infarction" in diagnosis:
         treatment_plan = "Suggested Treatment Plan for Possible Myocardial Ischemia/Infarction:\n- Further investigation (e.g., angiography)\n- Medical management as indicated by findings"

    print(f"Treatment Planning Agent suggested plan: {treatment_plan}")
    return treatment_plan

# Running the demo with echocardiogram and enhanced ECG analysis
def run_echo_demo():
    print("--- Running Echocardiogram and Enhanced ECG Demo ---")

    # Simulate patient data
    patient_data = {
        'age': 65,
        'has_history_heart_disease': True,
        'symptoms': 'Chest pain, shortness of breath',
        'troponin_level': random.choice(['normal', 'elevated']) # Simulate troponin
    }
    print(f"Simulated Patient Data: {patient_data}")

    # Simulate ECG data and analyze patterns
    ecg_data, simulated_ecg_condition = simulate_ecg_data()
    ecg_analysis_results = analyze_ecg_patterns(ecg_data)

    print(f"\nSimulated ECG condition: {simulated_ecg_condition}")
    print(f"Analyzed ECG Patterns: {ecg_analysis_results}")

    # Simulate echocardiogram data
    echocardiogram_data = simulate_echocardiogram_data()
    print(f"\nSimulated Echocardiogram Data: {echocardiogram_data}")


    # Step 1: Diagnostic Agent
    print("\n--- Engaging Diagnostic Agent ---")
    diagnosis = diagnose(patient_data, ecg_analysis_results=ecg_analysis_results, echocardiogram_data=echocardiogram_data)
    print(f"Diagnosis: {diagnosis}")

    # Step 2: Treatment Planning Agent
    print("\n--- Engaging Treatment Planning Agent ---")
    treatment_plan = plan_treatment(diagnosis, patient_data, echocardiogram_data=echocardiogram_data)
    print(f"Treatment Plan:\n{treatment_plan}")

    print("\n--- Demo Finished ---")

if __name__ == '__main__':
    run_echo_demo()