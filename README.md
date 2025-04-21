# Parts API

A Django REST Framework API for managing parts and analyzing part descriptions.

## Features

- CRUD operations for parts (create, read, update, delete)
- Endpoint to find the 5 most common words in part descriptions
- Comprehensive test suite
- Containerization: Application is containerized using Docker for consistent deployments.

## Setup and Installation
# Prerequisites

- [Docker](https://www.docker.com/get-started) installed

# Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/igormbq/django-api
   cd django-api
   ```

2. **Build and start the containers**
   ```bash
   docker compose up --build
   ```

   This command will:
   - Build the Docker image
   - Start the Django application
   - Run database migrations automatically
   - Start the development server at [http://localhost:8000](http://localhost:8000)

3. **How to execute the tests**:
```bash
docker compose run --rm web python manage.py test
```

## API Endpoints

### Parts CRUD Operations

- `GET /api/parts/` - List all parts
- `POST /api/parts/` - Create a new part
- `GET /api/parts/{id}/` - Retrieve a specific part
- `PUT /api/parts/{id}/` - Update a specific part
- `PATCH /api/parts/{id}/` - Partially update a specific part
- `DELETE /api/parts/{id}/` - Delete a specific part

### Common Words Analysis

- `GET /api/common-words/` - Get the 5 most common words in part descriptions

## Design Decisions

1. **Django REST Framework**: Chosen for its robust features, excellent documentation, and adherence to REST principles.

2. **ModelViewSet**: Used to automatically provide all CRUD operations with minimal code, following DRY principles.

3. **Data Migration**: Created a migration to populate the database with initial data, ensuring consistency across environments.

4. **Comprehensive Testing**: Implemented tests for all API endpoints to ensure reliability.

5. **Common Words Algorithm**: Used Python's Counter class for efficient word counting, with preprocessing to clean text.

6. **API Structure**: Followed REST best practices with appropriate HTTP methods and status codes.
