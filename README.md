# mainTU

## Overview
This repository demonstrates a simple setup for the **mainTU** project described in
`codexprompt.txt`. The app uses a Django backend and React frontend, packaged
with Docker for easy deployment.

## Setup

1. **Install Docker & Compose v2**
   Follow the [Docker Engine installation guide for Ubuntu](https://docs.docker.com/engine/install/ubuntu/).
2. **Install PostgreSQL 16**
   Use the [PostgreSQL Ubuntu instructions](https://www.postgresql.org/download/linux/ubuntu/) to add the PGDG repo and install `postgresql-16`.
3. **Install Node.js 20**
   Either use nvm or the [NodeSource setup script](https://github.com/nodesource/distributions#debinstall).
4. **Clone this repository** and create a `.env` file with your database URL and OAuth secrets.
5. **Build and run** the containers:
   ```bash
   docker compose build
   docker compose up -d
   ```
6. **Apply migrations** and create a Django superuser:
   ```bash
   docker compose exec backend python manage.py migrate
   docker compose exec backend python manage.py createsuperuser
   ```

## Basic Usage
Visit `http://localhost:8000` after the containers start. Upload the required CSV
files to generate parts forecasts and maintenance tasking data.
