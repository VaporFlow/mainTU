# mainTU

## Overview
mainTU is a planning tool that forecasts material demand and assigns maintenance tasks. It uses a Django backend and React frontend as described in `codexprompt.txt`.

## Features
- CSV Uploader and Manager that stores metadata and keeps the five most recent files.
- Parts forecasting and maintenance tasking modules exposed through a JSON API.
- Roles for Planner, Supervisor and Admin with local authentication.
- Responsive React interface using Material UI and D3 heat-map visualisations.
- Docker Compose environment to run PostgreSQL, Django and React.

## Setup
1. **Install prerequisites**: Docker, Compose v2, PostgreSQL 16 and Node.js 20.
2. **Clone this repository** and copy `.env.example` to `.env` with your credentials.
3. **Build and run** the containers:
   ```bash
   docker compose up -d --build
   ```
4. **Apply migrations** and create a superuser:
   ```bash
   docker compose exec backend python manage.py migrate
   docker compose exec backend python manage.py createsuperuser
   ```

## Development
Run tests with:
```bash
docker compose exec backend pytest
# frontend tests
docker compose exec frontend npm test
```

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines and development tips.

