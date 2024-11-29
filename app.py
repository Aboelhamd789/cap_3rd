from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route to serve the HTML file for GET requests
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('/index.html')  # Render HTML file

    if request.method == 'POST':
        data = request.get_json()
        print(data)
        if not data:
            return jsonify({"error": "No JSON data received"}), 400
        print("Received Data:", data)
        return jsonify({"message": "Data received successfully", "received_data": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=21197)
