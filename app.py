from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(
    app,
    origins=["http://localhost:3000"],
    methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"]
)

@app.get("/andmed")
def get_andmed():
    return jsonify({
        "message": "Andmed edukalt saadud"
    }), 200

@app.post("/andmed")
def post_andmed():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Vigased andmed"
        }), 400

    return jsonify({
        "message": "Andmed edukalt vastu võetud",
        "data": data
    }), 201

if __name__ == "__main__":
    app.run(debug=True)