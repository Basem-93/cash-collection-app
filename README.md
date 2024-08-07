# Cash Collection Application

This repository contains a Django project for a Cash Collection application with RESTful APIs.

## Overview

The Cash Collection application is designed to manage cash collection tasks performed by Cash Collectors, ensuring accountability and transparency in the process.

## Features

- **Task Management**: Manage tasks assigned to Cash Collectors.
- **Cash Collection**: Record and track cash collected from customers.
- **Manager Interaction**: Enable interaction between Cash Collectors and Managers.
- **Freeze Mechanism**: Automatically freeze Cash Collectors with large amounts for extended periods.

## Installation

# Cash Collection Application

This repository contains a Django project for a Cash Collection application with RESTful APIs.

## Overview

The Cash Collection application is designed to manage cash collection tasks performed by Cash Collectors, ensuring accountability and transparency in the process.

## Features

- **Task Management**: Manage tasks assigned to Cash Collectors.
- **Cash Collection**: Record and track cash collected from customers.
- **Manager Interaction**: Enable interaction between Cash Collectors and Managers.
- **Freeze Mechanism**: Automatically freeze Cash Collectors with large amounts for extended periods.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Basem-93/cash-collection-app.git
   cd cash-collection-app


2. **Set Up Virtual Environment:
   ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`


3. **Install Dependencies:
   ```bash
    pip install -r requirements.txt


4. **Database Migration:
   ```bash
    python manage.py migrate


5. **Run Development Server:
   ```bash
    python manage.py runserver


Access the Application:
    Open http://localhost:8000/ in your web browser.

# APIs

## 1) Task List
- **Endpoint**: `/api/tasks/`
- **Method**: `GET`
- **Body**: None
- **Description**: Retrieves a list of tasks that have been done by the CashCollector.

## 2) Next Task
- **Endpoint**: `/api/next_task/`
- **Method**: `GET`
- **Description**: Retrieves the next task that the CashCollector should do now.
- **Request Body**: ```json { "collector_id": 1 } ```

## 3) Collector Status
- **Endpoint**: `/api/collector_status/`
- **Method**: `GET`
- **Description**: Retrieves a flag indicating whether the CashCollector is frozen or not.
- **Request Body**: ```json { "collector_id": 1 } ```

## 4) Collect Cash
- **Endpoint**: `/api/collect/`
- **Method**: `POST`
- **Description**: Records the amount collected for a specific task.
- **Request Body**: ```json { "task_id": 1 } ```

## 5) Pay Cash
- **Endpoint**: `/api/pay/`
- **Method**: `POST`
- **Description**: Marks all collected tasks as paid to the manager and unfreezes the CashCollector.
- **Request Body**: ```json { "collector_id": 1 } ```

## 6) Create Task
- **Endpoint**: `/api/create_task/`
- **Method**: `POST`
- **Description**: Creates a new task for cash collection.
- **Request Body**: ```json { "collector_id": 1, "customer_name": "John Doe", "customer_address": "123 Main St", "amount_due": 1500 } ```

## 7) Create Collector
- **Endpoint**: `/api/create_collector/`
- **Method**: `POST`
- **Description**: Creates a new CashCollector user.
- **Request Body**: ```json { "name": "omar zekry", "balance": 0, "frozen_since": null, "is_frozen": false } ```




Testing APIs
To test the APIs, you can use tools like Postman or cURL.
Open Postman.
Import the provided Postman collection or manually create requests for each API endpoint.
Set up necessary headers and request bodies as described for each API.
Send requests and verify responses to ensure proper functionality.
