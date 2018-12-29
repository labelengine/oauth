# oauth
**To run application:**
* Install packages from requirements.txt
* Init DB
* Run flask application

_To init db:_
1) Download and install PostgreSQL
2) Create a database named "identities"
3) Make migration to DB. For this point you need run commands:
    * `flask db init`
    * `flask db migrate`
    * `flask db upgrade`
   
_To run flask application:_
1) Set the main point of the application. Windows: `set FLAKS_APP=oauth.py` Linux: `export FLASK_APP=oauth.py`
2) Launch the flask by the following command: `flask run`