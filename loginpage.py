from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        # GET method endpoint returns an operation code
        operation_code = "GET request received"
        return jsonify({"operation_code": operation_code})

    elif request.method == 'POST':
        try:
            # Receive JSON data from the POST request
            data = request.json

            # Check for required fields in the JSON data
            required_fields = ["user_id", "college_email_id", "college_roll_number", "numbers", "alphabets"]
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": f"Missing required field: {field}"}), 400

            # Process the data (you can replace this with your logic)
            # Calculate the highest alphabet in the input array of alphabets
            alphabets = data["alphabets"]
            highest_alphabet = max(alphabets)

            # Construct the response
            response_data = {
                "status": "success",
                "user_id": data["user_id"],
                "college_email_id": data["college_email_id"],
                "college_roll_number": data["college_roll_number"],
                "numbers": data["numbers"],
                "alphabets": data["alphabets"],
                "highest_alphabet": highest_alphabet
            }

            return jsonify(response_data)

        except Exception as e:
            return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)


