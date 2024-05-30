# Project: Basic CRUD APIs for Products

This Django project provides a RESTful API for managing products, including Create, Read, Update, and Delete (CRUD) operations. It utilizes Django REST framework for building the API endpoints and leverages SQLite as the default database.

**Features:**

- CRUD Operations:
  - Create new products
  - Retrieve all existing products
  - Get details of a specific product by ID
  - Update product information
  - Delete products
- Docker Support:
  - Includes `Dockerfile` and `docker-compose.yml` for easy containerization and deployment

**Running the Project:**

**1. Database Migration:**

- Run `python manage.py migrate` to create the necessary database tables.

**2. Running the API:**

**Option 1: Using Docker:**

     - Build the image: `docker-compose build`
     - Start the container: `docker-compose up -d` (detached mode)
     - Access the API: http://localhost:8000/api/v1/products/

**Option 2: Without Docker:**

     - Start the development server: `python manage.py runserver`
     - Access the API: http://localhost:8000/api/v1/products/

**API Endpoints:**

**POST:** http://localhost:8000/api/v1/products/

**Body (JSON):**

json
{
"name": "Headphone",
"category": "Electronics",
"price": 10000.0
}

**Response:**

JSON
{
"url": "http://localhost:8000/api/v1/products/5/",
"id": 5,
"name": "Headphone",
"category": "Electronics",
"price": 10000.0,
"created_at": "2024-05-30T05:27:41.917203Z"
}

**GET All Products:** http://localhost:8000/api/v1/products/

**Response:**

JSON
[
{ ...product details ... },
{ ...product details ... }
]

**GET Product by ID:** http://localhost:8000/api/v1/products/{id}

# Replace {id} with the actual product ID.

**Response:**

JSON
{
"url": "...",
"id": ...,
"name": "...",
"category": "...",
"price": ...,
"created_at": "..."
}

**PUT (Update):** http://localhost:8000/api/v1/products/{id}

**Body (JSON):**

JSON
{
"name": "Updated Name" // Optional fields to update
"category": "Updated Category"
"price": 12000.0
}

**Response:**

The updated product details will be returned.

**DELETE:** http://localhost:8000/api/v1/products/{id}

Replace {id} with the product ID to delete.

**Response:**

No content will be returned upon successful deletion.

# Additional Notes:

- Consider implementing pagination for GET All Products to handle large datasets in the future.
