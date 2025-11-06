# DevOps Demo with a simple Flask App with Health check

Production ready Flask app demonstrating DevOps best Practices

## Features Implemented

### 1. Multi-Stage Docker Build
- **Before:** 1.13 GB (python:3.11 base)
- **After:** 155 MB (python:3.11-slim runtime)
- **Reduction:** ~87%

**Benefits:**
- Smaller image size = faster deployments
- Reduced attack surface
- Lower storage costs


### 2. Docker Secrets Management
- Secrets stored in `secrets/` directory (gitignored)
- Mounted as files in `/run/secrets/`
- No hardcoded passwords in compose file
- Supports both Docker secrets and env vars (for local dev)

**How it works:**
```python
# App reads from /run/secrets/ first, falls back to env var
def get_secret(secret_name):
    secret_path = f'/run/secrets/{secret_name}'
    if os.path.exists(secret_path):
        with open(secret_path, 'r') as f:
            return f.read().strip()
    return os.getenv('APP_SECRET', 'no-secret-set')
```

## Quick Start
```bash
# Clone repo
git clone 
cd devops-flask-demo

# Create secret file
mkdir -p secrets
echo "your-secret-here" > secrets/app_secret.txt

# Build and run
docker-compose up --build

# Test endpoints
curl http://localhost:5001        # Home endpoint
curl http://localhost:5001/health # Health check
```

## Project Structure
```
devops-flask-demo/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile.dev         # Single stage Docker file, not used in current build 
├── Dockerfile            # Multi-stage Docker build
├── docker-compose.yml    # Docker Compose with secrets
├── secrets/              # Secret files (gitignored)
│   └── app_secret.txt
└── README.md
```

## Next Steps

- [ ] Add CI/CD pipeline with GitHub Actions
- [ ] Automate image tag updates in compose file
- [ ] Implement GitHub App for automated deployments
- [ ] Add production monitoring

## Technologies Used

- Python 3.11
- Flask 3.0
- Docker & Docker Compose
- Multi-stage builds
- Docker secrets

## CI/CD Pipeline

**Automated:** Push to main -> Build -> Push image to Dockerhub with following tags:
    - 'latest': easy to access
    - '<commit-sha>': specific version, easy to track

**Pull and Run:** 
```bash
docker pull YOUR_DOCKERHUB_USERNAME/devops-flask-demo:latest
docker run -p 5000:5000 YOUR_USERNAME/devops-flask-demo:latest
```
---

