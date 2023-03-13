# Fastapi-Postgresql

* STEP 1 
Clone this repository

* STEP 2 
Open the repo in VS code.

* STEP 3
Create env file from python -m venv env 
then activate the environment with env/Scripts/activate

* STEP 4
Install requirements.txt by pip install -r requirements.txt

* STEP 5 
Install Postgres and table plus. open the database set the database name as python_db.In config.py file update the Database_url and change your username and password for postgresql.

* STEP 6
Open table plus and create a new connection in postgresql and give the credentials.

* STEP 7
Run the command uvicorn main:app --reload

* STEP 8 
Run the command python populate_db.py to populate the dummy data and reload the server again.

* STEP 9
Now use this url to see CRUD Operation http://localhost:8000/docs

