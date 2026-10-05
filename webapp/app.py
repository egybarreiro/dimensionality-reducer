from flask import Flask, render_template, request, jsonify, send_from_directory
import pandas as pd
import os
from webapp.dimensionality_reducer.reducer import run_reducer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    try:
        file = request.files["file"]
        method = request.form["method"]

        df = pd.read_csv(file)
        result = run_reducer(df, method)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/download/csv/<name>")
def download_csv(name):
    return send_from_directory("static", name, as_attachment=True)

@app.route("/download/image/<name>")
def download_image(name):
    return send_from_directory("static", name, as_attachment=True)

@app.route("/history")
def history():
    if os.path.exists("webapp/history.json"):
        with open("webapp/history.json", "r") as f:
            return jsonify({"history": f.read()})
    return jsonify({"history": "[]"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
