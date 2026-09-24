# Student Feedback App

A Flask student feedback application with NIET email validation, automated tests, Docker support, and GitHub Actions CI/CD.

## Email requirement

The form accepts only institute email addresses ending with `@niet.co.in`.

Example:

```text
student@niet.co.in
```

Emails from other domains are rejected.

## Run locally

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000.

## Run tests

```bash
python -m pytest -q
```

## Run with Docker

```bash
docker build -t student-feedback-app .
docker run -p 5000:5000 student-feedback-app
```

## Deploy on Render

1. Sign in to Render.
2. Choose **New > Blueprint**.
3. Connect the `codexashu/student-feedback-app` repository.
4. Select the `main` branch.
5. Render reads `render.yaml` and builds the Docker service.
6. Deploy the service.

The GitHub Actions workflow runs tests and builds the Docker image on pushes and pull requests.
