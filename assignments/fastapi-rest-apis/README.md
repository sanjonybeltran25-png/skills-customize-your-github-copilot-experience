# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Learn how to build a simple REST API using the FastAPI framework, including routing, request handling, and JSON responses.

## 📝 Tasks

### 🛠️ Create API Endpoints

#### Description
Build a FastAPI application with endpoints for creating, reading, updating, and deleting items in a simple in-memory store.

#### Requirements
Completed program should:

- Use FastAPI to define API routes
- Implement routes for `GET`, `POST`, `PUT`, and `DELETE`
- Return JSON responses for all requests
- Use path and query parameters where appropriate

### 🛠️ Validate Input and Handle Errors

#### Description
Add request validation using Pydantic models and return meaningful error responses for invalid input.

#### Requirements
Completed program should:

- Define a Pydantic model for the item schema
- Validate request bodies for `POST` and `PUT`
- Return a `400` response for invalid input
- Return a `404` response when an item is not found

### 🛠️ Run and Test the API

#### Description
Start the FastAPI server and verify API behavior using sample requests.

#### Requirements
Completed program should:

- Include a main application file that can be run with Uvicorn
- Provide example requests for testing each endpoint
- Confirm that the API returns correct JSON and status codes
