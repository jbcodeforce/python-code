# Flask TDD Docker (Modernized with uv and Python 3.12)

This Flask project has been modernized to use:
- **Python 3.12** (upgraded from Python 3.7)
- **uv** for fast dependency management (replacing pip/pipenv)
- **pyproject.toml** for modern Python project configuration
- **Updated dependencies** with latest compatible versions

## Prerequisites

- Docker and Docker Compose
- uv (for local development): `curl -LsSf https://astral.sh/uv/install.sh | sh`

## Quick Start with Docker

1. **Build and run the services:**
   ```bash
   docker compose up --build
   ```

2. **Access the application:**
   - Application: http://localhost:5001
   - Database: PostgreSQL on port 5432

## Local Development with uv

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Activate the environment:**
   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Run tests:**
   ```bash
   uv run pytest
   ```

4. **Run linting:**
   ```bash
   uv run flake8
   uv run black --check .
   ```

5. **Format code:**
   ```bash
   uv run black .
   ```

## Project Structure

```
├── project/
│   ├── api/           # Flask API routes
│   ├── tests/         # Test suite
│   └── config.py      # Configuration settings
├── pyproject.toml     # Project configuration and dependencies
├── Dockerfile         # Development Docker image
├── Dockerfile.prod    # Production Docker image
├── docker-compose.yaml # Docker Compose configuration
└── entrypoint.sh      # Container entry point
```

## Key Changes from Original

- **Python 3.7 → 3.12**: Modern Python with better performance and features
- **pip/pipenv → uv**: 10-100x faster dependency resolution and installation
- **requirements.txt → pyproject.toml**: Modern Python project standard
- **Alpine → Debian Slim**: Better compatibility and performance for Python packages
- **Updated dependencies**: All packages updated to latest compatible versions

## Database

The project uses PostgreSQL with the following default configuration:
- **Host**: users-db (in Docker), localhost (local dev)
- **Port**: 5432
- **Database**: users_dev (development), users_test (testing)
- **User/Password**: postgres/postgres

## Environment Variables

- `FLASK_ENV`: development/production
- `APP_SETTINGS`: Configuration class path
- `DATABASE_URL`: PostgreSQL connection string
- `DATABASE_TEST_URL`: Test database connection string

## Testing

Run the test suite:
```bash
# With Docker
docker compose exec users uv run pytest

# Locally with uv
uv run pytest

# With coverage
uv run pytest --cov=project
```

## Production Deployment

Use the production Dockerfile:
```bash
docker build -f Dockerfile.prod -t flask-app:prod .
docker run -p 5000:5000 -e APP_SETTINGS=project.config.ProductionConfig flask-app:prod
```
