
 # Rest Api

The Django User Profile Management API is a web application built using the Django framework and Django REST framework. It provides a RESTful API for managing user profiles, including user name, email, contact details, and resume files.It allows users to create, view, update, and delete user profiles, including their resumes in PDF format.


## Installation

1.Clone the repository to your local machine:

```bash
git clone https://github.com/abhisheksingh-17/Rest-Api.git

```
2.Install the required packages from requirements.txt:  
```bash
pip install -r requirements.txt
```
3.Run database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
4.Create a superuser to access the Django admin interface (optional):
```bash
python manage.py createsuperuser
```


## Configure Django Settings
In your Django project's settings.py, 
1.Add this in the Installed_Apps Section:
```bash
    'rest_framework',
    'api', #Your App Name
```    
2.Add REST_FRAMEWORK:
```bash
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',  # Enable handling file uploads
    ]
}
```
3.Update the database settings to use MySQL as the database backend. Modify the DATABASES dictionary as follows:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'your_mysql_host', # Set it to'localhost' if the database is on the same machine as Django
        'PORT': 'your_mysql_port', # The default MySQL port is usually 3306
    }
}
```
## Deployment

To deploy this project run

```bash
  python manage.py runserver
```


## After Deployment
a.Open the Postman software or download the extension in VS Code-
In Postman, you can use different HTTP methods to perform GET, PUT, PATCH, and DELETE requests to interact with your Django REST API. Here's how you can use Postman for each operation:

1.GET Request:

i).Set the request type to GET.

ii).Enter the URL to fetch all user profiles or a specific profile with its primary key (pk). For example:
  .Fetch all profiles: http://localhost:8000/profiles/
  .Fetch a specific profile (replace <pk> with the profile's primary key): http://localhost:8000/profiles/<pk>/

iii).Click on the "Send" button to make the GET request and view the response data.

2.POST Request:

i).Set the request type to POST.

ii).Enter the URL to create a new user profile: http://localhost:8000/profiles/

iii).Go to the "Body" tab, select "form-data," and add the following key-value pairs for the new profile:
  .user_name: [Your desired user name]
  .email: [Your email address]
  .contact_details: [Contact details]
  .resume: [Select a .pdf file using the "Choose Files" button]

iv).Click on the "Send" button to make the POST request and create a new user profile.

3.PUT Request:

i).Set the request type to PUT.

ii).Enter the URL to update an existing user profile with its primary key (pk). For example:
  .http://localhost:8000/profiles/<pk>/

iii).Go to the "Body" tab, select "form-data," and add the following key-value pairs to update the profile:
  .user_name: [Updated user name]
  .email: [Updated email address]
  .contact_details: [Updated contact details]
  .resume: [Select a new .pdf file using the "Choose Files" button to update the resume]

iv).Click on the "Send" button to make the PUT request and update the user profile.

4.PATCH Request:

i).Set the request type to PATCH.

ii).Enter the URL to partially update an existing user profile with its primary key (pk). For example:
  .http://localhost:8000/profiles/<pk>/

iii).Go to the "Body" tab, select "form-data," and add the key-value pairs you want to update:
  .user_name: [Updated user name]
  .email: [Updated email address]
  .contact_details: [Updated contact details]
  .resume: [Select a new .pdf file using the "Choose Files" button to update the resume if needed]

iv).Click on the "Send" button to make the PATCH request and partially update the user profile.

5.DELETE Request:

i).Set the request type to DELETE.

ii).Enter the URL to delete an existing user profile with its primary key (pk). For example:
  .http://localhost:8000/profiles/<pk>/

iii).Click on the "Send" button to make the DELETE request and delete the user profile.

b.Open your MySQL Workbench and verify the following request are adding in your database.

Make sure your Django development server is running (python manage.py runserver) while testing these requests in Postman. Also, ensure you have added appropriate error handling in your views to handle invalid requests gracefully.
## Usage
API Endpoints:The API provides the following endpoints to manage user profiles:

1.List/Create User Profile
```bash
GET /profiles/ : Fetch a list of all user profiles.
POST /profiles/ : Create a new user profile by providing user name, email, contact details, and resume (in PDF format).
```
2.Retrieve/Update/Delete User Profile:
```bash
GET /profiles/<profile_id>/ : Retrieve a specific user profile by its profile ID.
PUT /profiles/<profile_id>/ : Update an existing user profile identified by its profile ID.
PATCH /profiles/<profile_id>/ : Partially update an existing user profile by providing updated fields.
DELETE /profiles/<profile_id>/ : Delete a user profile identified by its profile ID.
```
## Code Description 
The code implements a Django-based REST API for managing user profiles, including user name, email, contact details, and resume files in PDF format. It follows the Model-View-Controller (MVC) architecture and utilizes the Django REST framework to simplify the API development process.

Key Components:

1.Models (models.py):

The UserProfile model defines the structure of the user profiles, with fields for user name, email, contact details, and a FileField to store resumes.

2.Serializers (serializers.py):

The UserProfileSerializer serializes and deserializes the UserProfile model, ensuring data validation and conversion to and from JSON format.
Custom validation is performed to ensure that the uploaded resume is in PDF format.

3.Views (views.py):

Class-based views are used to handle different HTTP methods for the API endpoints. Each view function corresponds to a specific HTTP method (GET, POST, PUT, PATCH, DELETE) and performs CRUD operations on user profiles.

4.URLs (urls.py):

URL patterns are defined to map the API endpoints to their corresponding view functions, making the API accessible through defined URLs.

5.Authentication (settings.py):

Token-based authentication is enabled in the Django settings to secure certain API endpoints. Users can obtain an access token by sending their credentials to /api/token/.

Main Functionality:

1.Listing and Creating Profiles:

The API allows users to fetch a list of all user profiles (GET /profiles/) and create a new profile (POST /profiles/) by providing necessary data, including the resume in PDF format.

2.Retrieve, Update, and Delete Profiles:

Users can retrieve a specific user profile (GET /profiles/<profile_id>/), update the profile data (PUT /profiles/<profile_id>/), or partially update specific fields (PATCH /profiles/<profile_id>/) identified by the profile's ID.
Deleting a profile is possible using the DELETE request to /profiles/<profile_id>/.

3.Authentication and Security:

Certain API endpoints are protected and require token-based authentication, ensuring that only authorized users can access them.
The API validates the uploaded resume to ensure it is in PDF format, using custom validation in the serializer.

## Contributing and License
i).Users and developers are encouraged to contribute to the project by opening issues, suggesting new features, or submitting pull requests with improvements.

ii).The project is licensed under the MIT License, allowing users to use, modify, and distribute the code with proper attribution and a copy of the license.

The code follows best practices for building a robust and secure Django REST API for user profile management. It can be further extended and adapted to fit various use cases and integrate with other systems as needed.