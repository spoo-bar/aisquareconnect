## Running the code

### Backend
Flask application
```
\aisquareconnect$ virtualenv env
\aisquareconnect$ env\scripts\activate
\aisquareconnect$ pip install -r requirements.txt
\aisquareconnect$ set FLASK_APP=app
\aisquareconnect$ flask run
```
The flask application runs on http://127.0.0.1:5000/

### Frontend
VueJS application
```
\aisquareconnect\client$ npm install
\aisquareconnect\client$ npm run serve
```
The frontend application runs on http://localhost:8080/
