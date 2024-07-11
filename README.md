Here's a sample GitHub README.md template for your project with the key information you provided:

```markdown
# Wapiti Flask Docker

This project integrates Wapiti with Flask and Docker to create a web application for scanning websites for vulnerabilities.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Docker](#docker)
- [API Endpoints](#api)

## Installation

To set up the environment for this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/rollycodes/wapiti-flask-docker.git
    cd wapiti-flask-docker
    ```

2. Activate the Python environment:
    ```bash
    pyenv activate wr-39-wapiti (python 3.9.12)
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

After setting up the environment, you can run the application with the following command:
```bash
python app.py
```

## Docker

To build and run the Docker container, use the following commands:

1. Build the Docker image:
    ```bash
    docker build -t wapiti-scanner .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 5000:5000 wapiti-scanner
    ```

This will run the application inside a Docker container and expose it on port 5000.


### API Endpoint Documentation

This section provides detailed information about the available API endpoints for the Wapiti-based security scan service. The API offers functionalities to start security scans and retrieve reports through HTTP requests.

#### 1. Start Scan

**Endpoint**: `/scan`

**Method**: `POST`

**Description**: Initiates a security scan on the specified domain and asynchronously sends a notification upon completion.

**Request Body**:
```json
{
  "domain": "https://example.com",
  "callback_url": "http://localhost:5001/notification"
}
```
- `domain`: The URL of the website to scan.
- `callback_url`: The URL where a notification will be sent once the scan is completed.

**Response**:
```json
{
  "message": "Scan started",
  "report_location": "path/to/report.json"
}
```
- `message`: Confirmation that the scan has started.
- `report_location`: The location where the report will be available after the scan.

#### 2. Get Scan Report

**Endpoint**: `/get-report`

**Method**: `POST`

**Description**: Retrieves the JSON report for a completed scan.

**Request Body**:
```json
{
  "report_directory": "path/to/report"
}
```
- `report_directory`: The directory path provided in the notification, where the scan report is stored.

**Response**:
```json
{
  "report": "{detailed JSON report}"
}
```
- `report`: Contains the detailed JSON output of the scan.

### Testing Endpoints

For local development and testing, you can use tools like Postman or curl to send requests to these endpoints. To test the notification mechanism, ensure your local notification handler is running and properly configured to receive POST requests.

**Example curl command to start a scan**:
```bash
curl -X POST http://localhost:5000/scan \
-H 'Content-Type: application/json' \
-d '{"domain": "https://example.com", "callback_url": "http://localhost:5001/notification"}'
```

### Notification Handler Request Packet

When a security scan is completed, the notification handler endpoint will receive a POST request with the following JSON payload structure:

**Payload Structure**:
```json
{
  "domain": "https://example.com",
  "report_directory": "path/to/report"
}
```

**Fields**:
- `domain`: The domain that was scanned.
- `report_directory`: The directory where the scan report is stored. This path can be used to fetch the report using the `/get-report` endpoint.

**Example Usage**:
Ensure that your notification endpoint is configured to parse the incoming JSON and utilize the information as needed, for example, logging details or triggering additional workflows based on the scan results.

**Setting Up a Listener**:
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notification', methods=['POST'])
def notification():
    data = request.json
    print(f"Notification received for domain: {data['domain']}")
    print(f"Report directory: {data['report_directory']}")
    return jsonify({"status": "success", "message": "Notification received"}), 200

if __name__ == '__main__':
    app.run(port=5001)
```

This snippet provides a basic setup for a Flask app that listens for notifications and processes them as they arrive. Make sure to adjust the port and endpoint as per your deployment and testing environment.