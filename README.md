# MoonActiveTask - Tamir Hen
 
## steps to run django server in Windows env
1. Clone the repository and download python.
2. Open cmd and run the following commands:<br/>
	a. pip install virtualenvwrapper-win<br/>
	b. mkvirtualenv env<br/>
	c. pip install django<br/>
	d. cd {your-path}/MoonActiveTask/pyapi<br/>
	e. pip install requests<br/>
	f. python manage.py runserver<br/>
	
## Steps to run django server in MacOS env
1. Clone the repository and download python.
2. Open terminal and run the following commands:<br/>
	a. cd {your-path}/MoonActiveTask<br/>
	b. source env/bin/activate<br/>
	c. pip install django<br/>
	d. pip install requests<br/>
	e. cd pyapi<br/>
	f. python manage.py runserver<br/>
	
	
## Run vehicle validator service
Open postman and send a post request to 'http://localhost:8000/vehicle_validation' with json type body:<br/>
{<br/>
	"path" : "{yourpath}/MoonActiveTask/images/{wanted-image}"<br/>
}<br/>

### image map:
1.jpg: VALID<br/>
2.jpeg: VALID<br/>
<br/>
00.png - NOT VALID: 7 digit ends with '00'<br/>
5.jpg - NOT VALID: Public transportation<br/>
6.jpg - NOT VALID: Military and law<br/>
13.png - NOT VALID: Operated by gas<br/>

## Database
DB type: SQLite<br/>
Location: ./MoonActiveTask/piapi/db.sqlite3

### How to run
1. Download software 'DB Browser for SQLite' and open it.
2. Open/Drag db.sqlite3 to it.
3. Navigate to 'Browse Data' tab.
4. Choose table 'validator_vehicle' from dropdown.