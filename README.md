# Cash Collection Application

## Introduction

This project implements a Cash Collection application with a Django backend that provides RESTful APIs for managing cash collection tasks and collectors.

## Prerequisites

Before running the project, ensure you have the following installed:
- Python (version 3.6 or higher)
- Django
- Django REST Framework

## Setup

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd cashcollection

   
Install dependencies:
   bash
   pip install -r requirements.txt

Apply database migrations:
   bash
   python manage.py makemigrations
   python manage.py migrate

Create a superuser (for accessing Django admin):
   bash
   python manage.py createsuperuser


Start the development server:
   bash
   python manage.py runserver

The server will start running at http://127.0.0.1:8000/.

APIs

1) Task List
Endpoint: /api/tasks/
Method: GET
body: None
Description: Retrieves a list of tasks that have been done by the CashCollector.

2) Next Task
Endpoint: /api/next_task/
Method: GET
Description: Retrieves the next task that the CashCollector should do now.
Request Body:
{
    "collector_id": 1,
}


4) Collector Status
Endpoint: /api/collector_status/
Method: GET
Description: Retrieves a flag indicating whether the CashCollector is frozen or not.
Request Body:
{
    "collector_id": 1,
}


6) Collect Cash
Endpoint: /api/collect/
Method: POST
Description: Records the amount collected for a specific task.
Request Body:
{
    "task_id": 1
}

7) Pay Cash
Endpoint: /api/pay/
Method: POST
Description: Marks all collected tasks as paid to the manager and unfreezes the CashCollector.
Request Body:
{
    "collector_id": 1
}


Create Task
Endpoint: /api/create_task/
Method: POST
Description: Creates a new task for cash collection.
Request Body:
{
    "collector_id": 1,
    "customer_name": "John Doe",
    "customer_address": "123 Main St",
    "amount_due": 1500,
}


Create Collector
Endpoint: /api/create_collector/
Method: POST
Description: Creates a new CashCollector user.
Request Body:
{
    "name": "omar zekry",
    "balance": 0,
    "frozen_since": null,
    "is_frozen": false
}



Testing APIs
To test the APIs, you can use tools like Postman or cURL.
Open Postman.
Import the provided Postman collection or manually create requests for each API endpoint.
Set up necessary headers and request bodies as described for each API.
Send requests and verify responses to ensure proper functionality.
