# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI to understand routing, request validation, and JSON responses. By the end of this assignment, you will have a working API with create and read endpoints for a small resource collection.

## 📝 Tasks

### 🛠️ Set Up the FastAPI App and Health Endpoint

#### Description
Create the base FastAPI application and confirm it runs locally. Add a basic endpoint that proves the API is online.

#### Requirements
Completed program should:

- Define a FastAPI app instance in starter-code.py.
- Implement a GET /health endpoint that returns a JSON success message.
- Run with uvicorn and respond successfully in the browser or API docs.


### 🛠️ Build Item Endpoints with Validation

#### Description
Implement core REST endpoints for managing items in memory. Use Pydantic models to validate incoming data and return structured responses.

#### Requirements
Completed program should:

- Implement GET /items to return all items and POST /items to create a new item.
- Validate request bodies using a Pydantic model with at least name and price fields.
- Return clear status messages and include the created item in the POST response.
