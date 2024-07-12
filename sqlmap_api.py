from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

def run_sqlmap_command(target, options):
    command = ["sqlmap", "-u", target, "--batch"]
    command.extend(options)
    
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            return {"error": result.stderr}, 500
        
        output_lines = result.stdout.splitlines()
        return {"sqlmap_output": output_lines}, 200
    except Exception as e:
        return {"error": str(e)}, 500

@app.route("/sqlmap_scan", methods=["POST"])
def run_sqlmap_scan():
    data = request.json
    if not data or "target" not in data:
        return jsonify({"error": "Missing target parameter"}), 400
    
    target = data["target"]
    options = []

    if data.get("databases"):
        options.append("--dbs")
    if data.get("database"):
        options.extend(["-D", data["database"]])
    if data.get("tables"):
        options.append("--tables")   
    if data.get("table"):
        options.extend(["-T", data["table"]])
    if data.get("columns"): 
        options.append("--columns")   
    if data.get("column"):
        options.extend(["-C", data["column"]])
    if data.get("dump"):
        options.append("--dump")
    
    output, status_code = run_sqlmap_command(target, options)
    return jsonify(output), status_code

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
