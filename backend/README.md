# This is a Django REST APIs build for PASCO as a backend of Sales Forecasting Application.


## To set-up this project locally, follow these steps:


1. Clone the repository:


- git clone \<repository-url\>


2. Go to backend directory:


- cd backend/


3. Copy .env.example to .env and fill with value from your database credentials


- cp .env.example .env


4. Create and Activate a virtual environment:


- python3 -m venv venv
- source venv/bin/activate


5. Install the project dependencies:


- pip install -r requirements.txt


6. Run PostgreSQL


7. Create a database with the name following .env file DB_NAME


8. Now run migrations


- python3 manage.py migrate


9. Restore N-Deals DB from [n-deals.backup](https://drive.google.com/drive/folders/1ENaSuYXb5kL3gqtPnawBbAa1iWwNfQFb) file using following command


- pg_restore -h localhost -p 5432 -U postgres -d pasco_sales_forecast -v n-deals.backup


10. Start the development server:


- python3 manage.py runserver


11. Now you can now access the API Swagger documentation at :
- `http://localhost:8000/`