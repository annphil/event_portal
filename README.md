![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)

#Eventza

Eventza is an event portal for our college. A person should register(if he/she doesn't have an account already) and then log in to see upcoming events and to register for them. A user can create an event as well. 

## Team members
- Annamma T Philip  - 
- Christopher Roy
- Sreya Sabu
## Team Id 
BFH/recgtT8HqhB48Hytd/2021
## Link to product walkthrough
https://www.loom.com/share/28ee0005e871419cad3d5f9eef3007cf

## How it Works ?
It is coded in Python using Flask as web framework
The users and events are stored in databases.

## Libraries used
alembic==1.6.2
click==8.0.0
colorama==0.4.4
dnspython==2.1.0
email-validator==1.1.2
Flask==2.0.0
Flask-Login==0.5.0
Flask-Migrate==3.0.0
Flask-SQLAlchemy==2.5.1
Flask-WTF==0.14.3
greenlet==1.1.0
gunicorn==20.1.0
idna==3.1
itsdangerous==2.0.1
Jinja2==3.0.0
Mako==1.1.4
MarkupSafe==2.0.1
psycopg2==2.8.6
python-dateutil==2.8.1
python-editor==1.0.4
six==1.16.0
SQLAlchemy==1.4.15
Werkzeug==2.0.1
WTForms==2.3.3

## How to configure
Clone https://github.com/annphil/event_portal.git

## How to Run
Steps to follow inside cmd to open Project in development env in Google Browser
1) After cloning cd into event_portal
2) Copy Paste the following
   - set FLASK_APP=eventza.py
   - set FLASK_ENV=development
   - flask run
3) Use this to open the project in your browser -

    http://localhost:5000/index     or    http://localhost:5000/

App Link
https://eventza.herokuapp.com/     

