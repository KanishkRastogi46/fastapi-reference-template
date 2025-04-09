# FastAPI Project Template

A base template for starting FastAPI projects with proper structure and configuration.

## Overview

This template provides a starting point for building APIs with FastAPI, with a structured layout and common configurations already set up.

## Prerequisites

- Python 3.10+
- pip (Python package installer)

## Getting Started

### Setting Up Virtual Environment

1. Navigate to the project directory:
   ```bash
   cd path/to/funAPI
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

### Installing Dependencies

Install all required dependencies:

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, create one with the following minimum dependencies:

```bash
fastapi
uvicorn
pydantic
python-dotenv
sqlalchemy
pyjwt
passlib[bcrypt]
```

Then run:

```bash
pip install -r requirements.txt
```

## Project Structure

```
funAPI/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application instance
│   ├── routers/         # API route definitions
│   │   ├── __init__.py
│   │   └── users.py     # Example router for items
│   │
│   ├── config/          # Configuration settings
│   │   ├── __init__.py
│   │   └── settings.py  # Application settings
│   │
│   ├── schemas/         # Pydantic models/schemas
│   │   ├── __init__.py
│   │   └── item.py      # Data models for items
│   │
│   └── utils/           # Utility functions
│       ├── __init__.py
│       └── helpers.py   # Common helper functions
│
├── tests/               # Test cases
├── .venv/                # Virtual environment
├── .env                 # Environment variables (create this)
├── requirements.txt     # Project dependencies
├── .gitignore
└── README.md
```

## Running the Application

Start the development server:

```bash
uvicorn app.main:app --reload
```

This command:
- Uses `uvicorn` to serve the FastAPI application
- Points to `app.main:app` which should be the FastAPI instance
- `--reload` enables auto-reload on code changes (for development)

## API Documentation

Once the server is running:
- Interactive API documentation (Swagger UI): http://127.0.0.1:8000/docs
- Alternative API documentation (ReDoc): http://127.0.0.1:8000/redoc
- OpenAPI JSON schema: http://127.0.0.1:8000/openapi.json

## Customizing the Template

1. Update `app/core/settings.py` for application-specific settings
2. Add routes in `app/api/routes/`
3. Create models in `app/models/`
4. Implement business logic in `app/services/`

## Deployment Considerations

- Use Gunicorn with Uvicorn workers for production
- Set up proper environment variables
- Configure CORS if necessary
- Set up logging
