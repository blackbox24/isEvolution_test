## Objective
- Build a basic multi-tenant application with Django and Django REST Framework (DRF) that supports:
    - Tenant isolation for managing "products."
    - User authentication.
    - RESTful API endpoints for CRUD operations on products.

## Deliverables
- A Django project implementing:

    - Multi-tenancy for isolating tenant data.
    - User authentication using Django's default authentication system.
    - RESTful API endpoints for creating, retrieving, updating, and deleting products.
    - Tenant-aware access control to ensure data isolation.
    
- Clear instructions for:

    - Setting up and running the project locally.
    - Testing API functionality.

## STEPS
- [x] install packages 
- [x] create django project
- [x] create product app
- [x] append "products","rest_framework" to INSTALLED_APPS in `settings.py`
- [x] create product models
- [x] make migrations and migrate to database
- [x] create product serializer views and urls
- [x] create unit test for product model
- [x] decouple product urls into root url conf
- [x] implement session authentication in the project
- [x] create documentation for APIs using swagger


## HOW SETUP AND RUN PROJECT ON LOCAL MACHINE
1. clone repo from GitHub
    - : Run this in terminal `git clone <github repo>`

2. Create a virtual environment 
    - : Run this in terminal `py -m venv venv` (Windows)
    - : Run this in terminal `python3 -m venv venv` (MacOS) 

3. Activate virtual environment
    - : Run this in terminal `cd venv && cd Scripts && activate` (Windows)
    - : Run this in terminal `source ./venv/bin/activate` (MacOS) 

4. Run migrations
    - cd directory into the project repo
    - : Run this in terminal: `py manage.py makemigrations && py manage.py migrate`

5. Create a super User
    - : Run this in terminal: `py manage.py createsuperuser`

5. Run server
    - : Run this in terminal: `py manage.py runserver`

6. In your browser type `127.0.0.1:8000/api/docs/` to access the docs

7. Click on Authorize and type username and password of user you created

Now you are good to go

### Note !!
 - By default django uses session authentication so you will have to login as admin before performing CRUD commands