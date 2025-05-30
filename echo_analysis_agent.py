import json

def analyze_echo_data(echo_data):
    """
    Analyzes echocardiogram data and provides an interpretation.

    Args:
        echo_data (dict): A dictionary containing echocardiogram measurements and findings.

    Returns:
        dict: A dictionary containing the analysis and interpretation.
    """
    analysis_results = {}

    # Example analysis logic (replace with actual medical analysis)
    if "ejection_fraction" in echo_data and echo_data["ejection_fraction"] < 50:
        analysis_results["overall_function"] = "Reduced left ventricular ejection fraction."
    else:
        analysis_results["overall_function"] = "Normal left ventricular ejection fraction."

    # Analyze for Aortic Regurgitation
    if "aortic_regurgitation" in echo_data and echo_data["aortic_regurgitation"].lower() != "none":
        analysis_results["aortic_regurgitation"] = f"Aortic Regurgitation: {echo_data['aortic_regurgitation']}"

    # Analyze for Aortic Stenosis
    if "aortic_stenosis" in echo_data and echo_data["aortic_stenosis"].lower() != "none":
        analysis_results["aortic_stenosis"] = f"Aortic Stenosis: {echo_data['aortic_stenosis']}"

    # Analyze for Dilated Cardiomyopathy (simplified based on chamber size)
    # A more robust analysis would involve multiple measurements and clinical context
    if "chamber_sizes" in echo_data and "left_ventricular_end_diastolic_dimension" in echo_data["chamber_sizes"]:
        lvidd = echo_data["chamber_sizes"]["left_ventricular_end_diastolic_dimension"]
        # Assuming a threshold for adult males (this needs to be adjusted based on patient factors)
        if lvidd > 5.8:
            analysis_results["dilated_cardiomyopathy"] = f"Findings suggestive of Dilated Cardiomyopathy (LVIDd: {lvidd} cm). Further evaluation recommended."

    # Analyze for Regional Wall Motion Abnormalities
    if "regional_wall_motion" in echo_data and echo_data["regional_wall_motion"].lower() != "normal":
        analysis_results["regional_wall_motion_abnormalities"] = f"Regional Wall Motion Abnormalities: {echo_data['regional_wall_motion']}"

    # Add valve status to the results
    if "valve_status" in echo_data:
        valve_findings = {}
        if "mitral" in echo_data["valve_status"]:
            valve_findings["mitral"] = echo_data["valve_status"]["mitral"]
        if "aortic" in echo_data["valve_status"]:
            valve_findings["aortic"] = echo_data["valve_status"]["aortic"]
        analysis_results["valve_status"] = valve_findings
    if "valve_status" in echo_data:
        analysis_results["valve_status"] = f"Mitral valve: {echo_data['valve_status'].get('mitral', 'Not assessed')}, Aortic valve: {echo_data['valve_status'].get('aortic', 'Not assessed')}"

    if "pericardial_effusion" in echo_data and echo_data["pericardial_effusion"] == "present":
        analysis_results["pericardium"] = "Pericardial effusion noted."
    else:
        analysis_results["pericardium"] = "No significant pericardial effusion."

    return analysis_results

if __name__ == "__main__":
    # Example usage
    sample_echo_data = {
        "patient_id": "12345",
        "date": "2023-10-27",
        "ejection_fraction": 45,
        "valve_status": {
            "mitral": "mild regurgitation",
            "aortic": "normal",
        },
        "chamber_sizes": {
            "left_ventricular_end_diastolic_dimension": 6.0

        },
        "pericardial_effusion": "absent"
    }

    analysis = analyze_echo_data(sample_echo_data)
    print("Echocardiogram Analysis:")
    print(json.dumps(analysis, indent=4))

    sample_echo_data_2 = {
        "patient_id": "67890",
        "date": "2023-10-27",
        "ejection_fraction": 60,
        "valve_status": {
            "mitral": "normal",
            "aortic": "mild stenosis",
        },
        "regional_wall_motion": "apical hypokinesis",
        "pericardial_effusion": "present"
    }

    analysis_2 = analyze_echo_data(sample_echo_data_2)
    print("\nEchocardiogram Analysis 2:")
    print(json.dumps(analysis_2, indent=4))