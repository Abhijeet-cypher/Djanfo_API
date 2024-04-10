# Django_API
This project is basically build in Django REST Framework, which has Clients, Users and Projects.


To setup this project you have save the Project1 file in your system in a specific folder.
This is the Django project so you will need a create a virtual environment.

Before running the proejct in virtual environment make sure to install Django REST framework by using this command in your terminal
"pip install dajngorestframework"

After that just try to migrate all the models with the command "python manage.py makemigrations" and after that "python manage.py migrate".
This will save the models in the database.

And now you are ready to go run the command "python manage.py runserver" to run the project on local server.


Firstly, you will need to create a supseruser before accessing the API, so create a super user before running the following urls in your browser.

If you want to aaccess the links i will provide you with the details.
1. "api/users/create/" --- to create a new user for the project 
2. "api/clients/" --- to see the list of clients
3. "clients/create/" --- to create a new client for the project
4. "clients/<int:pk>/"> --- i used a dynamic url to get the specific clients detail 
5. "user-projects/" --- to see the list of projects 
6. "projects/create/" --- to create a new project and assign users
7. "projects/<int:pk>/" --- to see the details of particular project
8. "projects/<int:pk>/assign-users/" --- to assign users for a project(if not assigned while creating a proejct)


Thats it you there are the urls to access the whole project and make chanegs according to specific requirements.
