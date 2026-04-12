# Feminist Women Website

A full-stack web application for feminist voices, built with Spring Boot 3.x backend and Vue 3 frontend.

## Project Structure

```
women/
├── backend/                    # Spring Boot backend
│   ├── src/main/java/com/feminist/women/
│   │   ├── controller/         # REST API controllers
│   │   ├── entity/             # Data entities
│   │   ├── mapper/             # MyBatis mapper interfaces
│   │   └── service/            # Business logic
│   ├── src/main/resources/
│   │   ├── mapper/             # MyBatis XML mappers
│   │   ├── sql/                # Database initialization
│   │   └── application.yml     # App configuration
│   └── pom.xml
├── frontend/                   # Vue 3 frontend
│   ├── src/
│   │   ├── api/                # Axios API calls
│   │   ├── components/         # Vue components
│   │   ├── views/              # Page views
│   │   └── router/             # Vue Router config
│   └── package.json
└── SPEC.md                     # Design specification
```

## Features

- **Homepage**: Hero section, featured articles, mission statement, category browsing
- **Articles**: Filterable article list with pagination
- **Article Detail**: Full article view with share functionality
- **About**: Information about feminism and the movement
- **Contact**: Contact form for inquiries

## Tech Stack

### Backend
- Spring Boot 3.2.0
- MyBatis 3.0.3
- MySQL 8.0
- Java 17

### Frontend
- Vue 3.5
- Vue Router 4.6
- Axios 1.15
- Vite 8.0

## Prerequisites

- **Java 17+** (for backend)
- **Node.js 18+** (for frontend)
- **MySQL 8.0+** (for database)

## Setup

### 1. Database Setup

Create the database and seed initial data:

```bash
mysql -u root -p < backend/src/main/resources/sql/init.sql
```

Or manually:
```sql
CREATE DATABASE feminist_women;
USE feminist_women;
-- Run the SQL commands from init.sql
```

### 2. Backend Setup

```bash
cd backend

# Compile
mvn compile

# Run (or use your IDE)
mvn spring-boot:run

# The backend starts at http://localhost:8080
```

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies (if needed)
npm install

# Start development server
npm run dev

# The frontend starts at http://localhost:5173
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/articles | List articles (paginated) |
| GET | /api/articles/{id} | Get single article |
| GET | /api/articles/{id}/related | Get related articles |
| POST | /api/articles | Create article |
| PUT | /api/articles/{id} | Update article |
| DELETE | /api/articles/{id} | Delete article |
| GET | /api/categories | List all categories |
| POST | /api/contact | Submit contact form |

## Design

Apple-inspired aesthetic with:
- Clean, minimalist UI
- Large typography
- Smooth animations
- White/black/blue color scheme
- Mobile-first responsive design

See `SPEC.md` for detailed design specifications.

## Development

The frontend automatically proxies API requests to `http://localhost:8080` during development (configured in `vite.config.js`).

## Building for Production

### Frontend
```bash
cd frontend
npm run build
# Output is in frontend/dist/
```

### Backend
```bash
cd backend
mvn package
# Output JAR is in backend/target/
```
