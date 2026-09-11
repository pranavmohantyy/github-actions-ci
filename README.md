# CI/CD Pipeline Templates

This repository contains CI/CD pipeline templates for testing, linting, Docker builds, and deployment workflows using GitHub Actions.

## Workflows

### Test Workflow
- **File**: `.github/workflows/test.yml`
- **Triggered by**: Pushes to `main` branch and pull requests to `main`.
- **Actions**:
  - Checkout code
  - Set up Python
  - Cache pip dependencies
  - Install dependencies
  - Run tests with pytest

### Docker Workflow
- **File**: `.github/workflows/docker.yml`
- **Triggered by**: Pushes to `main` branch.
- **Actions**:
  - Checkout code
  - Set up Docker Buildx
  - Log in to GitHub Container Registry
  - Build and push Docker image

### Release Workflow
- **File**: `.github/workflows/release.yml`
- **Triggered by**: Pushing tags matching `v*.*.*`.
- **Actions**:
  - Checkout code
  - Get version from tags
  - Create a release in GitHub

## Running Locally with act
You can run the workflows locally using [act](https://github.com/nektos/act). Here's how:

1. Install act:
   ```bash
   brew install act
   ```

2. Run the test workflow:
   ```bash
   act -j test
   ```

3. Run the Docker workflow:
   ```bash
   act -j build
   ```

4. Run the release workflow:
   ```bash
   act -j release
   ```

Make sure you have Docker running for the Docker workflow to work properly.

## License
This project is licensed under the MIT License.