# MoonActiveTask
 
## teps to run django server in Windows env:
1. Clone the repository and download python.
2. Open cmd and run the following commands:
	a. pip install virtualenvwrapper-win
	b. mkvirtualenv env
	c. pip install django
	d. cd {your-path}/MoonActiveTask/pyapi
	e. pip install requests
	f. python manage.py runserver
	
## Steps to run django server in MacOS env:
1. Clone the repository and download python.
2. Open terminal and run the following commands:
	a. cd {your-path}/MoonActiveTask
	b. source env/bin/activate
	c. pip install django
	d. pip install requests
	e. cd pyapi
	f. python manage.py runserver
	
	
## Run vehicle validator service:
Open postman and send a post request to 'http://localhost:8000/vehicle_validation' with json type body:
{
	"path" : "{yourpath}/MoonActiveTask/images/{wanted-image}"
}

### image map:
1.jpg: VALID
2.jpeg: VALID

00.png - NOT VALID: 7 digit ends with '00'
5.jpg - NOT VALID: Public transportation
6.jpg - NOT VALID: Military and law
13.png - NOT VALID: Operated by gas

# Database:
DB type: SQLite
Location: ./MoonActiveTask/piapi/db.sqlite3

## How to run:
1. Download software 'DB Browser for SQLite' and open it.
2. Open/Drag db.sqlite3 to it.
3. Navigate to 'Browse Data' tab.
4. Choose table 'validator_vehicle' from dropdown.