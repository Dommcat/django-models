

# 401 Advanced Python LAB - Class 27
## Project: django-models


## Author: Dominck Martin




### N/A [Back-end server] ()
### N/A [Front-end application] ()


## Links and Resources


<!-- back-end server url (when applicable)
front-end application (when applicable)
Setup
.env requirements (where applicable)
i.e. -->




## Initialization/Installs: 
- django-admin startproject snacks_project
- python manage.py
- python manage.py migrate
- python manage.py startapp snacks
- pip install django-compressor (note:3rd party application)
- npm install -D tailwindscss
- npx tailwindcss init
- npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
- npm install flowbite

<!-- ## Checklist: 

mkdir project name 
create enviroment: vi 
shecl into using: vs
pip install django
pip freeze >requirements
django-admin startproject ("example: snack_tracker_project") . 
python manage.py runserver 
****Rocket Ship**** check server is up/rerun or shutdoen 18 unabplied migrations 
python manage.py migrate (Note: sql data base gets added & adds in the built in models)
*************************Application 
python manage.py startapp (Note: need to link project to apps in settings.py under installed_apps) 
**************************Model: create a model class in models 
(Note: Register the Snack model in the admin.py file of your Django app)
(Note: Modify the Snack model to have a user-friendly display in the admin site by adding a __str__ method that returns a string representation of the model instance)
python manage.py makemigrations 
python manage.py migrate
*******************************Super User Admin Login  
python manage.py createsuperuser (Note: Runserver and Login to admin site run server Http: /admin)
*****Optional Install: DB Browser for SQLite*************
sudo add-apt-repository -y ppa:linuxgndu/sqlitebrowser
sudo apt-get update
sudo apt-get install sqlitebrowser
**********************************************************
****************************views.py
(Note: go into views.py and create listview, detailview models) 

****************************Urls.py for both 
touch snacks/urls.py
In Project urls.py enter the paths: path ('', include('snacks.urls')), and add includes above liek this: from django.urls import path, include 
Set the url patterns route 
***********************Templates
--create templates folder --
mkdir templates 
touch templates/base.html
touch templates/snack_details.html
touch templates/snack_list.html
(Note: In settings.py Do somthing with BASE_DIR templates folder DIRS': [BASE_DIR / 'templates'])
******************************Access 
******************************Testing
python manage.py test
404 Check? 
*****************************CSS
 pip install django-compressor (note:3rd party application)
npm install -D tailwindscss
npx tailwindcss init
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
npm install flowbite -->