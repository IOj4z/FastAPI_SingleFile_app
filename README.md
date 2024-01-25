FastAPI CRUD Application

This is a simple FastAPI application that serves as a basic framework for a CRUD (Create, Read, Update, Delete) API. The application provides endpoints for managing books and albums.
Project Structure

plaintext

.
├── main.py
├── README.md

Files

    main.py: This file contains the FastAPI application code. It defines the data models (Book and Album) and provides CRUD operations for both entities.

    README.md: This README file provides an overview of the project, instructions for running the application, and any additional information about the structure and purpose of the code.

How to Run
Prerequisites

Ensure you have FastAPI and Uvicorn installed. You can install them using the following command:
 
pip install fastapi uvicorn

Running the Application

    Save the code in main.py.

    Open a terminal and navigate to the directory containing main.py.

    Run the following command to start the FastAPI application:

 
uvicorn main:app --reload

    Open your browser and go to http://127.0.0.1:8000 to access the FastAPI Swagger documentation and test the API endpoints.

API Endpoints

    Home: http://127.0.0.1:8000
        Provides a welcome message.

Books

    Get All Books: http://127.0.0.1:8000/books
    Get Book by ID: http://127.0.0.1:8000/books/{id}
    Add a Book: http://127.0.0.1:8000/books (POST)
    Update a Book: http://127.0.0.1:8000/books/{id} (PUT)
    Delete a Book: http://127.0.0.1:8000/books/{id} (DELETE)

Albums

    Get All Albums: http://127.0.0.1:8000/albums
    Get Album by ID: http://127.0.0.1:8000/albums/{id}
    Add an Album: http://127.0.0.1:8000/albums (POST)
    Update an Album: http://127.0.0.1:8000/albums/{id} (PUT)
    Delete an Album: http://127.0.0.1:8000/albums/{id} (DELETE)