# This is a FastAPI Backend APP, SQLite DB has been used for this assignment to make things easy and SQLAlchemy as ORM.

## To set-up this project locally, follow these steps:

1. Clone the repository:

- git clone \<repository-url\>

2. Go to backend directory:

- cd backend/

3. Create and Activate a virtual environment:

- python3 -m venv venv
- source venv/bin/activate

4. Install the project dependencies:

- pip install -r requirements.txt

5. Start the development server:

- python3 run.py

6. DB - On app start

- dev.db will be created (if not exists)
- All tables will be migrated
- Seed Categories Table(To ease the relationship with Services for CRUD operations)
- Seed AdminUsers Tabale
 - username: admin
 - password: admin123

11. Now you can now access the API Swagger documentation at:
- `http://localhost:8000/docs`


## To run the project using Docker, follow these steps:

1. Go to backend directory:

- cd backend/

1. Build & Run With Docker Compose:

- `docker-compose up --build`


## API documentation (Swagger)

1. After successfull set-up and run, go to:
- `http://localhost:8000/docs`

2. You will get a Authorize button at the top right corner.

3. Duringn the app start, admin user has alreday been created.

4. Now you can authorize the admin by OAuth2 Scheme using the following credentials:
- username: admin
- password: admin123

5. Now Bearer token(JWT) will be automatically passed for protected end-points.

## How to run tests

1. For local environment:
- Go to backend
- Enable venv
- Now Run tests using: `pytest`

2. For Docker environment:
- Afetr running the container successfully
- Enter the container: `docker exec -it fastapi-sheba /bin/bash`
- Now Run tests using: `pytest`

## Assumptions

1. dev.db has also been pushed, so you get some data to test the end-points.

2. You can delete the dev.db for fresh tables. On app start, db and tables will be automatically created.

3. Admin Credentials:
- username: admin
- password: admin123

4. All the config data has been set in `app>core>config.py` also `.env` file linked here. Variables can also be accessed from `.env` using Settings Instance.