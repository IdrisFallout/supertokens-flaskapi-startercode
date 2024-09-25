# supertokens-flaskapi-startercode

This is a Flask boilerplate for building and deploying a backend API using Supertokens for authentication, authorization, and session management.

## Getting Started

Before starting, ensure you have a Supertokens account and the following installed:

- Python 3.8 or later
- Docker (optional, for local development)

### 1. Setup Supertokens

Create a Supertokens instance and obtain the following details:

- `supertokens_config`: API key and secret
- `app_info`: App ID and Client ID
- `recipe_list`: List of recipes to use

### 2. Clone and Configure Repository

```
git clone https://github.com/IdrisFallout/supertokens-flaskapi-startercode.git
cd supertokens-flaskapi-startercode
```

In `config.py`, update the following variables:

```python
app_info = {
    "app_name": os.getenv("APP_NAME", "Supertokens Flask Boilerplate"),
    "api_domain": os.getenv("BACKEND_URI", "http://localhost:5000"),
    "website_domain": os.getenv("FRONTEND_URI", "http://localhost:3000"),
}

framework = "flask"
```

### 3. Run Locally (Optional)

(Requires Docker)

```
docker-compose up --build
```

### 4. Run in Production

Deploy your API to the cloud of your choice. Ensure you set the following environment variables:

- `APP_NAME`
- `BACKEND_URI`
- `FRONTEND_URI` (for CORS)

## Features

- **Authentication** (email/password)
- **Authorization** (role-based access control)
- **Session Management** (single sign-on, session tracking)
- **CORS** configuration (for frontend integration)
- **Error Handling** (custom error responses)

## Contributions

Contributions are welcome! Please create a pull request with your changes and ensure tests pass.

## License

MIT
