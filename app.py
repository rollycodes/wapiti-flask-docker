from flask import Flask, request, jsonify
import subprocess
import os
from datetime import datetime
import threading
import sys

app = Flask(__name__)

def run_scan(domain, report_dir):

    # Path for JSON output
    output_path = os.path.join(report_dir, "report.json")
    log_path = os.path.join(report_dir, "log.dat")

    cmd = [
        "wapiti",
        "-u", domain,
        "-f", "json",
        "-o", output_path,
        "-d", "1",
        "--max-links-per-page", "5",
        "--flush-session"
    ]
    
    with open(log_path, 'w') as f:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Stream output to log file and stdout
        for line in process.stdout:
            sys.stdout.write(line)  # This will also appear in Docker logs
            f.write(line)

        # Check for errors
        errors = process.stderr.read()
        if errors:
            sys.stderr.write(errors)  # This will also appear in Docker logs
            f.write(errors)

    if process.wait() == 0:
        print("Scan completed successfully")  # This will now appear in Docker logs
    else:
        print(f"Scan failed")  # Error messages are already logged


@app.route('/scan', methods=['POST'])
def scan_website():
    # Extract domain from the POST request
    content = request.json
    domain = content['domain']
    domain_folder = domain.replace("http://", "").replace("https://", "").replace("www.", "").replace("/", "_")
    
    # Current timestamp for uniqueness
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Unique report directory
    report_dir = f"./scan_reports/{domain_folder}_{timestamp}"
    os.makedirs(report_dir, exist_ok=True)
    
    # Start the scan in a new thread
    thread = threading.Thread(target=run_scan, args=(domain, report_dir))
    thread.start()
    
    return jsonify({"message": "Scan started", "report_location": f'{report_dir}/report.json'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
