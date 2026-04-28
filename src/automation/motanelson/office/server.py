from flask import Flask, request
import csv
import os
from datetime import datetime

app = Flask(__name__)
CSV_FILE = "data.csv"

# Criação do arquivo CSV, se não existir
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "campo1", "campo2"])  # Cabeçalho

@app.route('/form1', methods=['GET'])
def form_handler():
    campo1 = request.args.get('campo1', '')
    campo2 = request.args.get('campo2', '')
    timestamp = datetime.now().isoformat()

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, campo1, campo2])

    return f"Data received: campo1={campo1}, campo2={campo2}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
