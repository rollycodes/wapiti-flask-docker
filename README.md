Here's a sample GitHub README.md template for your project with the key information you provided:

```markdown
# Wapiti Flask Docker

This project integrates Wapiti with Flask and Docker to create a web application for scanning websites for vulnerabilities.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Docker](#docker)
- [Contributing](#contributing)
- [License](#license)

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

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any features, bugs, or documentation improvements.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/awesome-feature`)
3. Commit your changes (`git commit -m 'Add some awesome feature'`)
4. Push to the branch (`git push origin feature/awesome-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

This template includes sections for installation, usage, Docker, contributing, and the license. You can expand it further with more details about your project as needed.