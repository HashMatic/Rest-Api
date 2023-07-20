
 # Django User Profile Management Api

The Django User Profile Management API is a web application built to manage user profiles and their resumes. It provides a RESTful API that allows clients to perform CRUD operations on user profiles, including creating new profiles, retrieving existing profiles, updating profile information, and deleting profiles. Users can interact with the API through HTTP requests using tools like Postman or by integrating it into their own applications.



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
5.Run the server:
```bash
python manage.py runserver
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
## Usage

The API supports token-based authentication, ensuring secure access to certain endpoints. Users can obtain an access token by sending their credentials to the /api/token/ endpoint. This token is then used in the Authorization header for authenticated requests.

Use tools like Postman or Python's requests library to send HTTP requests to the API endpoints.The API provides the following endpoints to manage user profiles:

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
## Roadmap
To use the Project,follow these steps:

  1.Clone the project repository and set up a virtual environment.(Optional)

  2.Install the required packages using pip install -r requirements.txt.

  3.Run the database migrations with python manage.py migrate.

  4.Optionally, create a superuser with python manage.py createsuperuser to access the Django admin interface.

  5.Start the Django development server with python manage.py runserver.

  6.Use tools like Postman or Python's requests library to send HTTP requests to the API endpoints.

  7.Open your MySQL Workbench and verify the following request are adding in your database.

  8.Open the Postman software or download the extension in VS Code-
  In Postman, you can use different HTTP methods to perform GET, PUT, PATCH, and DELETE requests to interact with your Django REST API. Here's how you can use Postman for each operation:

a).GET Request:

 i).Set the request type to GET.

 ii).Enter the URL to fetch all user profiles or a specific profile with its primary key (pk). 

 For example:
  
 Fetch all profiles: http://localhost:8000/profiles/

 Fetch a specific profile (replace (pk) with the profile's primary key): 
  http://localhost:8000/profiles/(pk)/

 iii).Click on the "Send" button to make the GET request and view the response data.

b).POST Request:

 i).Set the request type to POST.

 ii).Enter the URL to create a new user profile:
   http://localhost:8000/profiles/

 iii).Go to the "Body" tab, select "form-data," and add the following key-value pairs for the new profile:
  
    user_name: [Your desired user name]
  
    email: [Your email address]
  
    contact_details: [Contact details]
  
    resume: [Select a .pdf file using the "Choose Files" button]

 iv).Click on the "Send" button to make the POST request and create a new user profile.

c).PUT Request:

 i).Set the request type to PUT.

 ii).Enter the URL to update an existing user profile with its primary key (pk). 

  For example:http://localhost:8000/profiles/(pk)/

 iii).Go to the "Body" tab, select "form-data," and add the following key-value pairs to update the profile:

    user_name: [Updated user name]

    email: [Updated email address]
  
    contact_details: [Updated contact details]
  
    resume: [Select a new .pdf file using the "Choose Files" button to update the resume]

 iv).Click on the "Send" button to make the PUT request and update the user profile.

d).PATCH Request:

 i).Set the request type to PATCH.

 ii).Enter the URL to partially update an existing user profile with its primary key (pk).

  For example:http://localhost:8000/profiles/(pk)/

 iii).Go to the "Body" tab, select "form-data," and add the key-value pairs you want to update:
  
    user_name: [Updated user name]
  
    email: [Updated email address]
  
    contact_details: [Updated contact details]
  
    resume: [Select a new .pdf file using the "Choose Files" button to update the resume if needed]

 iv).Click on the "Send" button to make the PATCH request and partially update the user profile.

e).DELETE Request:

 i).Set the request type to DELETE.

 ii).Enter the URL to delete an existing user profile with its primary key (pk). 

  For example:http://localhost:8000/profiles/(pk)/

 iii).Click on the "Send" button to make the DELETE request and delete the user profile.

Make sure your Django development server is running (python manage.py runserver) while testing these requests in Postman. Also, ensure you have added appropriate error handling in your views to handle invalid requests gracefully.
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

Users can retrieve a specific user profile (GET /profiles/<profile_id>/),update the profile data (PUT /profiles/<profile_id>/), or partially update specific fields (PATCH /profiles/<profile_id>/) identified by the profile's ID.
Deleting a profile is possible using the DELETE request to /profiles/<profile_id>/.

3.Authentication and Security:

Certain API endpoints are protected and require token-based authentication, ensuring that only authorized users can access them.
The API validates the uploaded resume to ensure it is in PDF format, using custom validation in the serializer.

## Technology Used
The project utilizes the following technologies:

 1.Python: The programming language used for the entire Django project.

 2.Django: A high-level web framework that provides various tools and utilities for building web applications. It handles URL routing, database migrations, and user authentication.

 3.Django REST Framework (DRF): An extension of Django that simplifies the process of building RESTful APIs. It provides features like serializers, class-based views, authentication, and permissions.

 4.MySQL: The relational database management system used to store user profile data and other related information.

 5.MySQL Workbench: A graphical tool for managing and interacting with the MySQL database. It allows developers to visualize and modify the database structure and content.

 6.Token-Based Authentication: DRF's built-in token-based authentication system is used to secure certain API endpoints. Users must obtain an access token by providing their credentials, which is then used in the Authorization header for authenticated requests.

 7.Git: The version control system used for code management, collaboration, and tracking changes.

 8.Postman: A popular API development and testing tool used to interact with the API endpoints. It allows users to send various types of HTTP requests and inspect the responses.

By leveraging these technologies, the Django User Profile Management API provides a robust and secure solution for managing user profiles, making it suitable for various web applications and services that require user profile functionality.
## Future Scope
The Django User Profile Management API has several potential areas for future improvement and expansion. Here are some future scope ideas to enhance the functionality and usability of the API:

 1.User Authentication Enhancements:

   a.Implement OAuth or JWT (JSON Web Tokens) for more secure and scalable authentication.

   b.Provide options for social media logins (e.g.,    Google, Facebook, Twitter) to improve user  registration and login experience.

2.User Profile Customization:

   a.Allow users to personalize their profiles with additional information, such as profile pictures, cover photos, and bio.

   b.Implement user preferences and settings to let users customize their interaction with the platform.

3.User Profile Search and Filters:

   a.Add search and filter functionality to allow users to find specific profiles based on criteria like skills, location, or experience.
  
   b.Implement sorting options to arrange profiles based on different attributes (e.g., alphabetical order, experience level).

4.User Profile Ratings and Reviews:

   a.Introduce a rating and review system where users can rate and provide feedback on other users' profiles.
  
   b.Allow users to endorse or recommend others for specific skills or qualifications.

5.API Versioning:

  Implement versioning for the API to support backward compatibility when introducing changes in the future.

6.Pagination and Performance Optimization:

   a.Implement pagination to handle large data sets efficiently and improve API performance.

   b.Optimize database queries and use caching to reduce response times for frequently accessed data.

7.User Interactions and Connections:

   a.Allow users to connect or follow other profiles to build professional networks.

   b.Implement messaging or notification systems for user-to-user communication.

8.Profile Privacy Settings:

   Provide privacy settings for users to control the visibility of their profile information to the public or specific user groups.

9.User Activity Tracking:

   Track user activity and provide insights into profile visits, interactions, and engagement.

10.Analytics and Reporting:

   Implement analytics and reporting features to analyze user data and identify trends or patterns.

11.Internationalization and Localization:

   a.Make the API multilingual by adding support for different languages and locales.

   b.Allow users to choose their preferred language for the user interface.

12.Integration with External Services:

   Integrate with third-party services, such as email providers, cloud storage, or applicant tracking systems, to enhance functionality.

13.Unit Testing and Test Coverage:

   Increase test coverage by writing more unit tests to ensure code quality and reliability.

14.Documentation and API Documentation:

   a.Improve documentation for the project, including code comments and explanatory notes.

   b.Generate comprehensive API documentation using tools like Swagger/OpenAPI.

15.Security Enhancements:

   Implement additional security measures, such as rate limiting, input validation, and access control.

These future scope ideas can help expand the functionality of the Django User Profile Management API and make it a more comprehensive and feature-rich solution for managing user profiles in a wide range of web applications and platforms. Remember to prioritize features based on user feedback, industry trends, and the specific needs of your project's target audience.
## Contributing and License
i).Users and developers are encouraged to contribute to the project by opening issues, suggesting new features, or submitting pull requests with improvements.

ii).The project is licensed under the MIT License, allowing users to use, modify, and distribute the code with proper attribution and a copy of the license.

The code follows best practices for building a robust and secure Django REST API for user profile management. It can be further extended and adapted to fit various use cases and integrate with other systems as needed.