import os

from flask import Flask, send_file, request, jsonify
from orchestration_service_demo import orchestrate_analysis

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('src/index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Create uploads directory if it doesn\'t exist
    uploads_dir = 'uploads'
if not os.path.exists(uploads_dir):
 os.makedirs(uploads_dir)

symptoms = request.form.get('symptoms', '')

    # Backend validation: check if symptoms are providedif not symptoms:
return jsonify({"error": "Symptoms are required."}), 400

patient_data = {"symptoms": symptoms}
response_message = {"status": "Analysis initiated", "symptoms": symptoms}

if 'ecg-file' in request.files:
        ecg_file = request.files['ecg-file']
        if ecg_file.filename != '':
            # Save the file temporarily (or process directly)
            # ecg_file_path = os.path.join(uploads_dir, ecg_file.filename)
            # ecg_file.save(ecg_file_path)
            response_message['ecg_file_received'] = ecg_file.filename

try:
    # In a real application, you would extract other relevant patient data here
        # You would likely pass file paths or content to orchestrate_analysis here
        analysis_results = orchestrate_analysis({"symptoms": symptoms})

        # For now, just return confirmation of received files along with analysis results
        return jsonify(analysis_results)
except FileNotFoundError:
        return jsonify({"error": "Required file not found."}), 404
except Exception as e:
        return jsonify({"error": str(e)}), 500

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
