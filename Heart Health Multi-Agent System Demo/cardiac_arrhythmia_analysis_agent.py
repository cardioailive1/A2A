import random

def analyze_arrhythmia(ecg_data, patient_data):
    """
    Analyzes ECG data for indicators of cardiac arrhythmia, considering patient data.
    This is a simplified example for demonstration purposes.

    Args:
        ecg_data (dict): A dictionary containing simulated ECG data.
                         Expected keys: 'heart_rate' (int), 'rhythm' (str, e.g., 'regular', 'irregular').
        patient_data (dict): A dictionary containing simulated patient data.
                         Expected keys: 'age' (int), 'has_palpitations' (bool), 'symptoms' (str).

    Returns:
        dict: A dictionary with arrhythmia analysis results.
              Keys: 'arrhythmia_detected' (bool), 'arrhythmia_type' (str or None).
    """
    analysis_results = {
        'arrhythmia_detected': False,
        'arrhythmia_type': None
    }

    heart_rate = ecg_data.get('heart_rate')
    rhythm = ecg_data.get('rhythm', '').lower()
    age = patient_data.get('age', 0)
    symptoms = patient_data.get('symptoms', '').lower()

    # Simplified logic for detecting arrhythmia
    # Tachycardia: Heart rate > 100 bpm
    if heart_rate is not None and heart_rate > 100:
        analysis_results['arrhythmia_detected'] = True
        analysis_results['arrhythmia_type'] = 'Tachycardia'

    # Bradycardia: Heart rate < 60 bpm
    if heart_rate is not None and heart_rate < 60:
        analysis_results['arrhythmia_detected'] = True
        if analysis_results['arrhythmia_type']:
            analysis_results['arrhythmia_type'] += ' and Bradycardia'
        else:
            analysis_results['arrhythmia_type'] = 'Bradycardia'

    # Irregular Rhythm
    if rhythm == 'irregular':
        analysis_results['arrhythmia_detected'] = True
        if analysis_results['arrhythmia_type']:
            analysis_results['arrhythmia_type'] += ' and Irregular Rhythm'
        else:
            analysis_results['arrhythmia_type'] = 'Irregular Rhythm'

    # Possible Supraventricular Tachycardia (SVT) - often fast heart rate and palpitations
    if heart_rate is not None and heart_rate > 150 and 'palpitations' in symptoms:
        analysis_results['arrhythmia_detected'] = True
        if analysis_results['arrhythmia_type'] is None:
            analysis_results['arrhythmia_type'] = 'Possible Supraventricular Tachycardia'
        elif 'Possible Supraventricular Tachycardia' not in analysis_results['arrhythmia_type']:
            analysis_results['arrhythmia_type'] += ' and Possible Supraventricular Tachycardia'

    # Atrial Fibrillation (AFib) - often irregular rhythm and palpitations
    if rhythm == 'irregular' and 'palpitations' in symptoms:
        analysis_results['arrhythmia_detected'] = True
        if analysis_results['arrhythmia_type'] is None:
            analysis_results['arrhythmia_type'] = 'Atrial Fibrillation'
        elif 'Atrial Fibrillation' not in analysis_results['arrhythmia_type']:
            analysis_results['arrhythmia_type'] += ' and Atrial Fibrillation'

    # Possible Significant Bradycardia - very slow heart rate, especially in older adults
    if heart_rate is not None and heart_rate < 40 and age > 70:
        analysis_results['arrhythmia_detected'] = True
        if analysis_results['arrhythmia_type'] and 'Bradycardia' not in analysis_results['arrhythmia_type']:
            analysis_results['arrhythmia_type'] += ' and Possible Significant Bradycardia'
        elif not analysis_results['arrhythmia_type']:
             analysis_results['arrhythmia_detected'] = True
             analysis_results['arrhythmia_type'] = 'Possible Significant Bradycardia'

    # Add a random chance for detection for demo purposes if no clear indicators
    if not analysis_results['arrhythmia_detected'] and random.random() < 0.05: # 5% chance
         analysis_results['arrhythmia_detected'] = True
         analysis_results['arrhythmia_type'] = 'Indeterminate Arrhythmia (Subtle Signs or Random)'

    return analysis_results

if __name__ == '__main__':
    # Example Usage
    ecg_data_1 = {'heart_rate': 75, 'rhythm': 'regular'}
    patient_data_1 = {'age': 55, 'has_palpitations': False}
    analysis_1 = analyze_arrhythmia(ecg_data_1, patient_data_1)
    print(f"Analysis 1: {analysis_1}")

    ecg_data_2 = {'heart_rate': 120, 'rhythm': 'irregular'}
    patient_data_2 = {'age': 65, 'has_palpitations': True}
    analysis_2 = analyze_arrhythmia(ecg_data_2, patient_data_2)
    print(f"Analysis 2: {analysis_2}")

    ecg_data_3 = {'heart_rate': 50, 'rhythm': 'regular'}
    patient_data_3 = {'age': 75, 'has_palpitations': False}
    analysis_3 = analyze_arrhythmia(ecg_data_3, patient_data_3)
    print(f"Analysis 3: {analysis_3}")

    ecg_data_4 = {'heart_rate': 160, 'rhythm': 'regular'}
    patient_data_4 = {'age': 30, 'has_palpitations': True}
    analysis_4 = analyze_arrhythmia(ecg_data_4, patient_data_4)
    print(f"Analysis 4: {analysis_4}")