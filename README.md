# Student Feedback App

A simple Flask web application that collects a student's name, course, and feedback, then displays submitted feedback on the page.

## Run locally

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000.

## Run tests

```bash
pytest
```

## Run with Docker

```bash
docker build -t student-feedback-app .
docker run -p 5000:5000 student-feedback-app
```

## CI/CD

GitHub Actions installs dependencies, runs pytest, builds the Docker image, and executes a deployment placeholder after successful tests on the `main` branch. Replace the deployment placeholder with commands for the selected hosting provider.
