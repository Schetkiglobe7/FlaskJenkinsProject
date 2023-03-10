from flask import Flask, jsonify    

app = Flask(__name__)   


@app.route("/")
def home():
    return "Hello, World NEW! 3"


@app.route("/health.json")  
def health():
    return jsonify({"status": "UP"}), 200   

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8085", debug=True)
