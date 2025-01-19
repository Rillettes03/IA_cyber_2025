import re
import joblib
import json

# Load the saved model and vectorizer
model = joblib.load('syslog_classifier_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Preprocess function
def preprocess_log(log):
    return re.sub(r'[^a-zA-Z0-9 ]', '', log)

# Real-time Classification Function
def classify_log_from_json(json_file_path):
    # Load JSON file
    with open(json_file_path, 'r') as f:
        log_data = json.load(f)
    
    # Extract the log message
    if isinstance(log_data, list) and len(log_data) > 0 and 'message' in log_data[0]:
        log_message = log_data[0]['message']
    else:
        raise ValueError("Invalid JSON structure. Ensure it contains a list with a 'message' field.")

    # Preprocess the log message
    processed_log = preprocess_log(log_message)

    # Vectorize and classify
    vectorized_log = vectorizer.transform([processed_log])
    prediction = model.predict(vectorized_log)

    # Print the result
    if prediction[0] == 1:
        print("\nMalicious Log Detected!")
        print(f"Log: {log_message}")
    else:
        print("Log is benign.")

# Example usage
json_file_path = r'C:\\Users\\vixis\\Desktop\\Work\\Codespython\\AI ELK\\single_log.json'
classify_log_from_json(json_file_path)
