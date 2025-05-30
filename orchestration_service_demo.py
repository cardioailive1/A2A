# orchestration_service_demo.py

def analyze_symptoms_placeholder(symptoms):
    """Placeholder for Symptom Analysis Agent."""
    print(f"Orchestration: Sending symptoms for analysis: {symptoms}")
    # Simplified logic: map symptoms to potential conditions
    potential_conditions = []
    if "chest pain" in symptoms.lower():
        potential_conditions.append("Heart Attack")
    if "fatigue" in symptoms.lower() or "swollen ankles" in symptoms.lower() or "fatique" in symptoms.lower():
        potential_conditions.append("Heart Failure")
    # Symptoms for Coronary Artery Disease (CAD)
    if "angina" in symptoms.lower() or \
       "chest discomfort" in symptoms.lower() or \
       "fatigue" in symptoms.lower():
        potential_conditions.append("Coronary Artery Disease")
    if "swelling" in symptoms.lower():
        potential_conditions.extend(["Heart Failure", "Mitral Regurgitation", "Dilated Cardiomyopathy"])
    if "shortness of breath" in symptoms.lower():
        potential_conditions.append("Heart Failure")
    if "bounding pulse" in symptoms.lower():
        potential_conditions.append("Aortic Regurgitation")
    if "palpitation" in symptoms.lower() or \
       "palpitations" in symptoms.lower() or \
       "irregular heartbeat" in symptoms.lower():
        potential_conditions.extend(["Mitral Regurgitation", "Dilated Cardiomyopathy", "Cardiac Arrhythmia"])
    if "dizziness" in symptoms.lower() or "syncope" in symptoms.lower():
        potential_conditions.append("Aortic Stenosis")
    if not potential_conditions:
         potential_conditions.append("Unknown")

    print(f"Orchestration: Received potential conditions: {potential_conditions}")
    return potential_conditions

def diagnose_placeholder(potential_conditions, patient_data, echo_analysis=None, ct_scan_analysis=None, mri_analysis=None):
    """Placeholder for Diagnostic Agent."""
    print(f"Orchestration: Sending potential conditions and patient data for diagnosis: {potential_conditions}, {patient_data}")
    # Simplified logic: based on potential conditions and basic patient data
    diagnosis = "Further evaluation needed" # Default to further evaluation
    # Include ECG analysis results in diagnosis logic
    ecg_results = patient_data.get("ecg_analysis", {})

    genetic_variants = patient_data.get("genetic_variants", [])
    if "Heart Attack" in potential_conditions:
        if ecg_results.get("STEMI"):
            diagnosis = "STEMI (ST-Elevation Myocardial Infarction)"
        elif ecg_results.get("NSTEMI"):
            diagnosis = "NSTEMI (Non-ST-Elevation Myocardial Infarction)"
    elif "Coronary Artery Disease" in potential_conditions:
        diagnosis = "Coronary Artery Disease" # More specific diagnosis might be made based on imaging
        if any(variant in genetic_variants for variant in ["9p21.3 variant"]): # Example check
            diagnosis += " (with genetic predisposition)"
    elif "Heart Failure" in potential_conditions:
        if echo_analysis and echo_analysis.get("ejection_fraction") == "Reduced":
            diagnosis = "Heart Failure with Reduced Ejection Fraction (HFrEF)"
            if any(variant in genetic_variants for variant in ["Dilated cardiomyopathy variant"]): # Example check
                diagnosis += " (with genetic predisposition)"
        elif echo_analysis and echo_analysis.get("chamber_size") == "Enlarged":
            diagnosis = "Heart Failure (likely due to chamber enlargement)"
        elif patient_data.get("has_history", False): # Fallback if no echo or echo normal but symptoms present
            if any(variant in genetic_variants for variant in ["Dilated cardiomyopathy variant", "Hypertrophic cardiomyopathy variant"]): # Example check
                diagnosis = "Heart Failure (clinical suspicion, with genetic predisposition)"
            diagnosis = "Heart Failure (clinical suspicion)\""
    elif "Aortic Regurgitation" in potential_conditions:
        aortic_valve_function = echo_analysis.get("aortic_valve_function") if echo_analysis else None
        if aortic_valve_function == "Severe Regurgitation":
            diagnosis = "Severe Aortic Regurgitation"
        elif aortic_valve_function == "Moderate Regurgitation":
            diagnosis = "Moderate Aortic Regurgitation"
        else:
            diagnosis = "Aortic Regurgitation (Mild or Undetermined Severity)"
    elif "Mitral Regurgitation" in potential_conditions:
        valve_function = echo_analysis.get("mitral_valve_function") if echo_analysis else None
        if valve_function == "Severe Regurgitation":
            diagnosis = "Severe Mitral Regurgitation"
        elif valve_function == "Moderate Regurgitation":
            diagnosis = "Moderate Mitral Regurgitation"
        else:
            diagnosis = "Mitral Regurgitation (Mild or Undetermined Severity)"
    elif "Dilated Cardiomyopathy" in potential_conditions:
        ejection_fraction = echo_analysis.get("ejection_fraction") if echo_analysis else None
        chamber_size = echo_analysis.get("chamber_size") if echo_analysis else None
        if ejection_fraction == "Reduced" and chamber_size == "Enlarged":
            diagnosis = "Dilated Cardiomyopathy (with reduced EF and enlarged chambers)"
        else:
            diagnosis = "Dilated Cardiomyopathy" # Or more specific based on Echo if needed
    elif "Aortic Stenosis" in potential_conditions:
        valve_function = echo_analysis.get("valve_function") if echo_analysis else None
        calcium_score = ct_scan_analysis.get("aortic_valve_calcium_score") if ct_scan_analysis else None
        if valve_function == "Severe Stenosis" or (calcium_score is not None and calcium_score > 1500): # Simplified threshold
            diagnosis = "Severe Aortic Stenosis"
        elif valve_function == "Moderate Stenosis" or (calcium_score is not None and calcium_score > 500): # Simplified threshold
             if any(variant in genetic_variants for variant in ["LRP5 variant"]): # Example check
                 diagnosis = "Moderate Aortic Stenosis (with genetic predisposition)"
             diagnosis = "Moderate Aortic Stenosis"
        else:
             diagnosis = "Aortic Stenosis (Mild or Undetermined Severity)"

    print(f"Orchestration: Received diagnosis: {diagnosis}")
    return diagnosis

def plan_treatment_placeholder(diagnosis, patient_data, echo_analysis=None, ct_scan_analysis=None, mri_analysis=None):
    """Placeholder for Treatment Planning Agent."""
    ct_scan_analysis = patient_data.get("ct_scan_analysis", {})
    mri_analysis = patient_data.get("mri_analysis", {})
    echo_analysis = patient_data.get("echo_analysis", {}) # Ensure echo_analysis is accessed if not passed directly
    genetic_variants = patient_data.get("genetic_variants", [])

    print(f"Orchestration: Sending diagnosis and patient data for treatment planning: {diagnosis}, {patient_data}")
    # Simplified logic: based on diagnosis
    treatment_plan = "Consult a medical professional for a personalized plan."
    if "Heart Attack" in diagnosis or "STEMI" in diagnosis or "NSTEMI" in diagnosis:
        treatment_plan = "Seek immediate medical attention. Treatment is critical and depends on the type of heart attack. May include medication (aspirin, nitroglycerin), angioplasty, or bypass surgery."
        if mri_analysis.get("infarct_detected"):
            infarct_location = mri_analysis.get("infarct_location", "unknown location")
            infarct_size = mri_analysis.get("infarct_size", "unknown size")
            treatment_plan += f" MRI shows infarct detected in the {infarct_location} region."

        if patient_data.get("genetic_variants"):
            treatment_plan += " Genetic variants associated with increased heart attack risk detected. Aggressive risk factor management and family screening are recommended."
    elif "Coronary Artery Disease" in diagnosis:
        if any(variant in genetic_variants for variant in ["CYP2C19 variant"]): # Example variant for antiplatelet response
            treatment_plan = "Management of Coronary Artery Disease typically involves lifestyle changes (diet, exercise, smoking cessation), medications (e.g., statins, antiplatelets, beta-blockers), and potentially procedures like angioplasty or bypass surgery depending on the severity. **Considering genetic variants (e.g., CYP2C19), pharmacological therapy may need adjustment (e.g., alternative antiplatelets or dosage) to optimize effectiveness and avoid complications like increased bleeding or major cardiac events.**"
        else:
            treatment_plan = "Management of Coronary Artery Disease typically involves lifestyle changes (diet, exercise, smoking cessation), medications (e.g., statins, antiplatelets, beta-blockers), and potentially procedures like angioplasty or bypass surgery depending on the severity."
        if ct_scan_analysis.get("aortic_valve_calcium_score") is not None:
            treatment_plan += f" CT scan shows an aortic valve calcium score of {ct_scan_analysis['aortic_valve_calcium_score']}, which helps assess risk."
        if echo_analysis:
             treatment_plan += f" Echo results ({echo_analysis.get('ejection_fraction', 'not available')} EF, {echo_analysis.get('chamber_size', 'not available')} chamber size) provide important information about heart function to guide management."
        if patient_data.get("genetic_variants"):
             treatment_plan += " Genetic variants associated with CAD risk detected. Intensified risk factor management and consideration of family screening are important."
    elif "Heart Failure" in diagnosis:
        if any(variant in genetic_variants for variant in ["beta-1 adrenergic receptor variant"]): # Example variant for beta-blocker response
             treatment_plan = "Treatment for Heart Failure involves managing symptoms and improving heart function. May include lifestyle changes, medications (ACE inhibitors, beta-blockers, diuretics), and potentially devices or surgery. **Considering genetic variants (e.g., beta-1 adrenergic receptor), beta-blocker therapy may require dosage adjustment or closer monitoring to optimize effectiveness and minimize adverse events.**"
        else:
            treatment_plan = "Treatment for Heart Failure involves managing symptoms and improving heart function. May include lifestyle changes, medications (ACE inhibitors, beta-blockers, diuretics), and potentially devices or surgery."
        if echo_analysis:
             treatment_plan += f" Echo results ({echo_analysis.get('ejection_fraction', 'not available')} EF, {echo_analysis.get('chamber_size', 'not available')} chamber size) are key to guiding treatment strategy for Heart Failure."
        if patient_data.get("genetic_variants"):
            treatment_plan += " Genetic variants associated with Heart Failure risk detected. Consider targeted therapies and family screening."
    elif "Aortic Regurgitation" in diagnosis:
        treatment_plan = "Management of Aortic Regurgitation depends on severity. Severe cases may require surgical valve replacement or repair. Mild to moderate cases are typically monitored."
        if echo_analysis and echo_analysis.get("aortic_valve_function"):
            treatment_plan += f" Echo shows {echo_analysis['aortic_valve_function']}. Review other factors that may influence severity."
        if patient_data.get("genetic_variants"):
             # While direct AR genetic variants are less common than AS, illustrating the principle
             treatment_plan += " Genetic factors may influence valve development or connective tissue, consider relevant genetic testing and family screening."
    elif "Mitral Regurgitation" in diagnosis:
        treatment_plan = "Management of Mitral Regurgitation depends on severity. Severe cases may require surgical valve repair or replacement. Mild to moderate cases are typically monitored."
        if echo_analysis and echo_analysis.get("mitral_valve_function"):
            treatment_plan += f" Echo shows {echo_analysis['mitral_valve_function']}. Review other factors that may influence severity."
        if patient_data.get("genetic_variants"):
             # Similar to AR, for illustration
             treatment_plan += " Genetic factors may influence valve development or connective tissue, consider relevant genetic testing and family screening."
    elif "Dilated Cardiomyopathy" in diagnosis:
        treatment_plan = "Treatment for Dilated Cardiomyopathy focuses on managing heart failure symptoms and improving cardiac function. May include medications, devices, or in severe cases, heart transplant."
        if patient_data.get("genetic_variants"):
             treatment_plan += " Genetic variants associated with Dilated Cardiomyopathy detected. Genetic counseling and family screening are strongly recommended. Specific therapies may be influenced by the underlying genetic cause."
             # Example of genetic-guided therapy (highly simplified)
             if any(variant in genetic_variants for variant in ["beta-1 adrenergic receptor variant"]): # Example variant for beta-blocker response
                 treatment_plan += " **Considering genetic variants (e.g., beta-1 adrenergic receptor), beta-blocker therapy may require dosage adjustment or closer monitoring.**"

             if "TTN variant" in patient_data.get("genetic_variants", []):
                 treatment_plan += " Consider therapies relevant to Titin-related cardiomyopathy."

        if echo_analysis:
            treatment_plan += f" Echo results ({echo_analysis.get('ejection_fraction', 'not available')} EF, {echo_analysis.get('chamber_size', 'not available')} chamber size) are important for assessing the severity and guiding treatment."
    elif "Aortic Stenosis" in diagnosis:
        treatment_plan = "Management of Aortic Stenosis depends on severity. Severe cases typically require valve replacement (TAVR or SAVR). Moderate cases are monitored."
        if any(variant in genetic_variants for variant in ["LRP5 variant"]): # Example variant
            treatment_plan += " **Considering genetic variants (e.g., LRP5), management and timing of intervention for Aortic Stenosis may need careful consideration.**"

        if echo_analysis and echo_analysis.get("valve_function"):
            treatment_plan += f" Echo shows {echo_analysis['valve_function']}. Review calcium score and symptoms for severity."
        if ct_scan_analysis.get("aortic_valve_calcium_score") is not None:
            treatment_plan += f" CT scan shows an aortic valve calcium score of {ct_scan_analysis['aortic_valve_calcium_score']}. This score is important for assessing severity."
        if patient_data.get("genetic_variants"):
             treatment_plan += " Genetic variants associated with Aortic Stenosis risk detected. Family screening and potentially earlier intervention may be considered."
    elif "Cardiac Arrhythmia" in diagnosis:
        treatment_plan = "Management of Cardiac Arrhythmia depends on the specific type. May include medications, cardioversion, ablation, or device implantation (pacemaker, defibrillator). Genetic testing may be relevant for some types of inherited arrhythmias."

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
            "ecg_data": "simulated_ecg_waveform", # Simulate presence of ECG data
            "mri_data": "simulated_mri_data", # Simulate presence of MRI data
            "genetic_variants": ["9p21.3 variant", "APOE E4 allele"] # Example genetic variants
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
            results = {
                "valve_function": "Normal",
                "chamber_size": "Enlarged" if patient_data.get("bmi", 25) > 30 else "Normal",
                "regional_wall_motion_abnormalities": False,
                "ejection_fraction": "Normal" # Default EF
            }
            if 'Aortic Regurgitation' in potential_conditions:
                results['aortic_valve_function'] = 'Severe Regurgitation'
            if 'Mitral Regurgitation' in potential_conditions:
                results['mitral_valve_function'] = 'Severe Regurgitation'
            if 'Dilated Cardiomyopathy' in potential_conditions:
                results['chamber_size'] = 'Enlarged'
                results['ejection_fraction'] = 'Reduced'
            if 'Heart Failure' in potential_conditions:
                 if results['ejection_fraction'] == 'Normal': # Simulate preserved EF for some HF cases
                     results['ejection_fraction'] = 'Preserved'
            return results

        # Placeholder for CT Scan Analysis Agent (for calcium scoring)
        def analyze_ct_scan_placeholder(ct_data, potential_conditions):
            print(f"Orchestration: Sending simulated CT scan data for analysis: {ct_data}")
            results = {}
            # Simplified logic for demo: simulate calcium score based on potential conditions
            if "Aortic Stenosis" in potential_conditions:
                 results["aortic_valve_calcium_score"] = 2500 # High score for severe AS
            if "Aortic Regurgitation" in potential_conditions:
                 results["aortic_valve_calcium_score"] = 800 # Moderately elevated for AR (can be present)
            if "Coronary Artery Disease" in potential_conditions:
                 results["coronary_calcium_score"] = 1200 # Simulate elevated calcium score for CAD
            # In a real scenario, this would involve image analysis
            return results

        # Placeholder for MRI Analysis Agent (for infarct detection and characterization)
        def analyze_mri_placeholder(mri_data, potential_conditions):
            print(f"Orchestration: Sending simulated MRI data for analysis: {mri_data}")
            results = {}
            # Simplified logic for demo: simulate infarct detection based on potential conditions
            if "Heart Attack" in potential_conditions or "Coronary Artery Disease" in potential_conditions:
                results = {"infarct_detected": True, "infarct_location": "Anterior", "infarct_size": "simulated_size"} # Simulate infarct detection
            else: # Simulate no infarct if heart attack or CAD not suspected
                results = {"infarct_detected": False}
            # In a real scenario, this would involve image analysis
            return results

        # 1. Call Symptom Analysis Agent
        potential_conditions = analyze_symptoms_placeholder(symptoms)

        # 2. Optional: Call ECG Analysis Agent if heart attack is suspected
        ecg_analysis_results = {}
        if "Heart Attack" in potential_conditions and patient_data.get("ecg_data"):
            print("Orchestration: Potential heart attack detected, proceeding with ECG analysis...")
            ecg_analysis_results = analyze_ecg_placeholder(patient_data["ecg_data"])
            patient_data["ecg_analysis"] = ecg_analysis_results # Add results to patient data.
            print(f"Orchestration: Received ECG analysis results: {ecg_analysis_results}")

            # Optional: Call MRI Analysis Agent if heart attack is suspected and MRI data is available
            mri_analysis_results = {}
            # Assuming patient_data might contain mri_data key if available
            if "mri_data" in patient_data:
                print("Orchestration: Potential heart issue detected, proceeding with MRI analysis...")
                mri_analysis_results = analyze_mri_placeholder(patient_data["mri_data"], potential_conditions) # Pass potential_conditions
                patient_data["mri_analysis"] = mri_analysis_results # Add results to patient data
            print(f"Orchestration: Received MRI analysis results: {mri_analysis_results}")

        # 3. Optional: Call Echocardiogram Analysis Agent if heart failure is suspected
        # Also call CT Scan Analysis Agent for Aortic Stenosis for calcium scoring
        echo_analysis_results = {}
        ct_scan_analysis_results = {}

        # Determine if imaging analysis is needed based on potential conditions
        needs_imaging = any(cond in potential_conditions for cond in ["Heart Failure", "Aortic Stenosis", "Aortic Regurgitation", "Mitral Regurgitation", "Dilated Cardiomyopathy", "Coronary Artery Disease"])

        if needs_imaging:
            print("Orchestration: Potential heart issue detected, proceeding with imaging analysis...")

            # Call Echocardiogram Analysis Agent if relevant conditions are present
            if any(cond in potential_conditions for cond in ["Heart Failure", "Aortic Stenosis", "Aortic Regurgitation", "Mitral Regurgitation", "Dilated Cardiomyopathy"]):
                echo_analysis_results = analyze_echo_placeholder("simulated_echo_data")
                patient_data["echo_analysis"] = echo_analysis_results # Add results to patient data
                print(f"Orchestration: Received Echo analysis results: {echo_analysis_results}")

            # Call CT Scan Analysis Agent if relevant conditions are present
            if "Aortic Stenosis" in potential_conditions or "Aortic Regurgitation" in potential_conditions or "Coronary Artery Disease" in potential_conditions:
                ct_scan_analysis_results = analyze_ct_scan_placeholder("simulated_ct_data", potential_conditions)
                patient_data["ct_scan_analysis"] = ct_scan_analysis_results # Add results to patient data
                print(f"Orchestration: Received CT scan analysis results: {ct_scan_analysis_results}")

        # 4. Call Diagnostic Agent (including potential ECG and Echo results)
        # Pass ct_scan_analysis_results to diagnose_placeholder
        # Also pass mri_analysis_results
        diagnosis = diagnose_placeholder(potential_conditions, patient_data, echo_analysis=patient_data.get("echo_analysis"),
                                          ct_scan_analysis=patient_data.get("ct_scan_analysis"), mri_analysis=patient_data.get("mri_analysis"))
        print("--- Orchestration Service: Symptom processing finished ---\n")

        # 5. Call Treatment Planning Agent
        treatment_plan = plan_treatment_placeholder(diagnosis, patient_data, echo_analysis=patient_data.get("echo_analysis"), ct_scan_analysis=patient_data.get("ct_scan_analysis"), mri_analysis=patient_data.get("mri_analysis"))
        return {"diagnosis": diagnosis, "treatment_plan": treatment_plan}

if __name__ == "__main__":
    # Example usage (for testing the orchestration logic directly)
    test_symptoms = "chest pain and shortness of breath"
    orchestrator = OrchestrationServiceDemo()
    result = orchestrator.process_symptoms(test_symptoms)
    print("\nDemo Orchestration Result:")
    print(f"Diagnosis: {result['diagnosis']}")
    print(f"Treatment Plan: {result['treatment_plan']}")
    print("\n--- Another test case ---")
    test_symptoms_2 = "fatigue and swollen ankles"
    result_2 = orchestrator.process_symptoms(test_symptoms_2)
    print("\nDemo Orchestration Result:")
    print(f"Diagnosis: {result_2['diagnosis']}")
    print(f"Treatment Plan: {result_2['treatment_plan']}")