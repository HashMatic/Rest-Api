
# Django User Profile Management Api

![](https://res.cloudinary.com/practicaldev/image/fetch/s--rAk2-3Xf--/c_imagga_scale,f_auto,fl_progressive,h_900,q_auto,w_1600/https://thepracticaldev.s3.amazonaws.com/i/gz5xantp1vycu7ueleh4.jpg)

The Django User Profile Management API is a web application built to manage user profiles and their resumes. It provides a RESTful API that allows clients to perform CRUD operations on user profiles, including creating new profiles, retrieving existing profiles, updating profile information, and deleting profiles. Users can interact with the API through HTTP requests using tools like Postman or by integrating it into their own applications.


## Table Of Contents

 - [Installation](https://github.com/abhisheksingh-17/Rest-Api#installation)
 - [Configure Django Settings](https://github.com/abhisheksingh-17/Rest-Api#configure-django-settings)
 - [Acknowledgements](https://github.com/abhisheksingh-17/Rest-Api#acknowledgements)
 - [Usage](https://github.com/abhisheksingh-17/Rest-Api#usage)
 - [Technologies Used](https://github.com/abhisheksingh-17/Rest-Api#technologies-used)
 - [Code Description](https://github.com/abhisheksingh-17/Rest-Api#code-description)
 - [Roadmap](https://github.com/abhisheksingh-17/Rest-Api#roadmap)
 - [Screenshots](https://github.com/abhisheksingh-17/Rest-Api#screenshots)
 - [Future Scope](https://github.com/abhisheksingh-17/Rest-Api#future-scope)
 - [Contribution & Scope](https://github.com/abhisheksingh-17/Rest-Api#contribution--license)
## Installation

1.Clone the repository to your local machine:
```bash
 git clone https://github.com/abhisheksingh-17/Rest-Api.git
```

2.Create and activate a virtual environment (optional, but recommended):
```bash
  python -m venv venv

  source venv\Scripts\activate
  ```

3.Install the required packages from requirements.txt:   
```bash
pip install -r requirements.txt
````

4.Run database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
5.Create a superuser to access the Django admin interface (optional):
```bash
python manage.py createsuperuser
```
6.Run the server:
```bash
python manage.py runserver
```
## Configure Django Settings

In your Django project's settings.py file-

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
## Acknowledgements

 I would like to express my sincere gratitude to everyone who contributed to the creation and development of the "Django User Profile Management API" project. Their efforts and support have been invaluable in making this project a reality.

I want to thank the following individuals:

 - Django,Django REST Framework, and MySQL: for the powerful and flexible tools that formed the foundation of the project. Their user-friendly interfaces and comprehensive documentation made it easier to build and deploy the API.

 - Postman: for the intuitive API testing and development environment, simplifying the testing and validation of API endpoints.

 - MySQL Workbench: for the graphical tool that facilitated the management and interaction with the MySQL database.

 - Open Source Community: for providing a wealth of resources, libraries, and tools that made the development process more efficient and enjoyable.

 - GitHub: for providing a platform for collaboration and version control, enabling seamless cooperation among team members.

Lastly, I extend my gratitude to anyone who has used, tested, or provided feedback on the "Django User Profile Management API." Your engagement has been invaluable in improving the project and ensuring its usability.

Thank you all for being a part of this journey!


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

## Technologies Used

The project utilizes the following technologies:

 - Python: The programming language used for the entire Django project.

 - Django: A high-level web framework that provides various tools and utilities for building web applications. It handles URL routing, database migrations, and user authentication.

 - Django REST Framework (DRF): An extension of Django that simplifies the process of building RESTful APIs. It provides features like serializers, class-based views, authentication, and permissions.

 - MySQL: The relational database management system used to store user profile data and other related information.

 - MySQL Workbench: A graphical tool for managing and interacting with the MySQL database. It allows developers to visualize and modify the database structure and content.

 - Token-Based Authentication: DRF's built-in token-based authentication system is used to secure certain API endpoints. Users must obtain an access token by providing their credentials, which is then used in the Authorization header for authenticated requests.

 - Git: The version control system used for code management, collaboration, and tracking changes.

 - Postman: A popular API development and testing tool used to interact with the API endpoints. It allows users to send various types of HTTP requests and inspect the responses.

By leveraging these technologies, the Django User Profile Management API provides a robust and secure solution for managing user profiles, making it suitable for various web applications and services that require user profile functionality.
## Code Description

The code implements a Django-based REST API for managing user profiles, including user name, email, contact details, and resume files in PDF format. It follows the Model-View-Controller (MVC) architecture and utilizes the Django REST framework to simplify the API development process.

Key Components:

1.Models (models.py):

```python

from django.db import models

class UserProfile(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_details = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')
```
 - In the models.py file, we have defined the UserProfile model. This model represents the user profiles in the API. It has four fields: user_name, email, contact_details, and resume. Each field is represented by the appropriate Django model field, such as CharField and FileField. 

 - resume = models.FileField(upload_to='resumes/'): This line defines the resume field as a FileField in the UserProfile model. The upload_to attribute specifies the directory where uploaded resumes will be stored on the server. In this case, uploaded resumes will be stored in the resumes/ directory inside the media root (defined in Django settings).

2.Serializers (serializers.py):

```python
from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user_name', 'email', 'contact_details', 'resume']

    def validate_resume(self, resume):
        # Check if the uploaded file is a PDF
        if not resume.name.lower().endswith('.pdf'):
            raise serializers.ValidationError("Resume must be in PDF format.")
        return resume

```
 - In the serializers.py file, we have defined the UserProfileSerializer class. This serializer converts the UserProfile model instances into JSON format and vice versa. The Meta class specifies the model to be serialized (UserProfile) and includes all fields.

 - class UserProfileSerializer(serializers.ModelSerializer):: This line defines the UserProfileSerializer class, which is a subclass of serializers.ModelSerializer. It is responsible for converting UserProfile model instances to and from JSON format.

 - fields =['user_name', 'email', 'contact_details', 'resume']: This ensures that all fields (user_name, email, contact_details, resume) will be serialized when interacting with the API.

 - def validate_resume(self, value):: This line defines a custom validation method for the resume field. It validates the uploaded resume to ensure that it is in PDF format. If the uploaded file does not end with .pdf, a serializers.ValidationError is raised, indicating that the resume must be in PDF format.

3.Views (views.py):

```python

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer

class UserProfileListAPIView(APIView):
    def get(self, request):
        profiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        profile = self.get_object(pk)
        serializer = UserProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
```

 - Class-based views are used to handle different HTTP methods for the API endpoints. Each view function corresponds to a specific HTTP method (GET, POST, PUT, PATCH, DELETE) and performs CRUD operations on user profiles.

 - class UserProfileListAPIView(APIView):: This line defines the UserProfileListAPIView class, which is a subclass of APIView. It handles the /profiles/ endpoint for listing all user profiles (GET) and creating new profiles (POST).

 - profiles = UserProfile.objects.all(): This line retrieves all UserProfile objects from the database using the Django ORM. The UserProfile model's manager, objects, allows us to interact with the database and fetch all the profile objects.

 - serializer = UserProfileSerializer(profiles, many=True): This line creates an instance of the UserProfileSerializer and passes the profiles queryset as the data to be serialized. The many=True argument indicates that we are serializing multiple instances (profiles) rather than a single instance.

 - return Response(serializer.data): This line returns the serialized data in JSON format as the response to the client's GET request. The serializer.data contains the serialized representation of all user profiles in the database.

 - def post(self, request):: This method handles the POST request to create a new user profile. The request.data contains the data sent by the client in the request body.

 - serializer = UserProfileSerializer(data=request.data): This line creates an instance of UserProfileSerializer and passes the request.data as the data to be deserialized. It attempts to convert the JSON data from the request into a valid UserProfile object.

 - if serializer.is_valid():: This line checks if the deserialized data is valid according to the serializer's validation rules.

 - serializer.save(): This line saves the validated UserProfile instance to the database.

 - return Response(serializer.data, status=status.HTTP_201_CREATED): If the data is valid and the profile is successfully created, this line returns the serialized data of the created profile as the response with a status code 201 CREATED. The serializer.data contains the serialized representation of the created profile.

 - return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST): If the data is invalid and cannot be deserialized, this line returns the serializer errors as the response with a status code 400 BAD REQUEST. The errors contain information about what validation rules failed.

 - class UserProfileDetailAPIView(APIView):: This line defines the UserProfileDetailAPIView class, which is a subclass of APIView. It handles the /profiles/<int:pk>/ endpoint for retrieving, updating, and deleting individual user profiles.

 - def get_object(self, pk):: This method is a helper function used to retrieve the UserProfile instance based on the primary key (pk) provided in the URL. If the profile with the specified pk does not exist, it raises a status.HTTP_404_NOT_FOUND exception.

 - def get(self, request, pk):: This method handles the GET request to retrieve a specific user profile. It uses the get_object() method to fetch the profile from the database, serializes it using the UserProfileSerializer, and returns the serialized data as the response.

 - def put(self, request, pk):: This method handles the PUT request to update the entire user profile identified by pk. It retrieves the profile from the database using the get_object() method, deserializes the updated data from the request using the UserProfileSerializer, and saves the updated profile to the database. If the data is valid, it returns the serialized data of the updated profile as the response.

 - def patch(self, request, pk):: This method handles the PATCH request to update specific fields of the user profile identified by pk. It is similar to the put() method but allows partial updates. The partial=True argument in the serializer indicates that only the fields provided in the request will be updated, not the entire object.

 - def delete(self, request, pk):: This method handles the DELETE request to delete the user profile identified by pk. It retrieves the profile from the database using the get_object() method and then deletes it from the database. It returns a status.HTTP_204_NO_CONTENT response, indicating that the deletion was successful.

4.URLs (urls.py):

```python

from django.urls import path
from .views import UserProfileListAPIView, UserProfileDetailAPIView

urlpatterns = [
    path('profiles/', UserProfileListAPIView.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', UserProfileDetailAPIView.as_view(), name='profile-detail'),
]
```
 - In the urls.py file, we have defined URL patterns that map API endpoints to their corresponding views. For example, the /profiles/ endpoint is handled by the UserProfileListAPIView, and the /profiles/<int:pk>/ endpoint (where <int:pk> is the profile's primary key) is handled by the UserProfileDetailAPIView.


5.Authentication (settings.py):

 - Token-based authentication is enabled in the Django settings to secure certain API endpoints. Users can obtain an access token by sending their credentials to /api/token/.

Main Functionality:

1.Listing and Creating Profiles:

 - The API allows users to fetch a list of all user profiles (GET /profiles/) and create a new profile (POST /profiles/) by providing necessary data, including the resume in PDF format.

2.Retrieve, Update, and Delete Profiles:

 - Users can retrieve a specific user profile (GET /profiles/<profile_id>/),update the profile data (PUT /profiles/<profile_id>/), or partially update specific fields (PATCH /profiles/<profile_id>/) identified by the profile's ID. Deleting a profile is possible using the DELETE request to /profiles/<profile_id>/.

3.Authentication and Security:

 - Certain API endpoints are protected and require token-based authentication, ensuring that only authorized users can access them. The API validates the uploaded resume to ensure it is in PDF format, using custom validation in the serializer.
## Roadmap


To use the Project,follow these steps:

1.Clone the project repository and set up a virtual environment.(Optional)

2.Install the required packages using pip install -r requirements.txt.

3.Run the database migrations with python manage.py migrate.

4.Optionally, create a superuser with python manage.py createsuperuser to access the Django admin interface.

5.Start the Django development server with python manage.py runserver.

6.Use tools like Postman or Python's requests library to send HTTP requests to the API endpoints.

7.Open your MySQL Workbench and verify the following request are adding in your database.

8.Open the Postman software or download the extension in VS Code- In Postman, you can use different HTTP methods to perform GET, PUT, PATCH, and DELETE requests to interact with your Django REST API. Here's how you can use Postman for each operation:

a).GET Request:

 - Set the request type to GET.

 - Enter the URL to fetch all user profiles or a specific profile with its primary key (pk).

For example:

Fetch all profiles: http://localhost:8000/profiles/

Fetch a specific profile (replace (pk) with the profile's primary key): http://localhost:8000/profiles/(pk)/

 - Click on the "Send" button to make the GET request and view the response data.

b).POST Request:

 - Set the request type to POST.

 - Enter the URL to create a new user profile: http://localhost:8000/profiles/

 - Go to the "Body" tab, select "form-data," and add the following key-value pairs for the new profile:
```bash
user_name: [Your desired user name]

email: [Your email address]

contact_details: [Contact details]

resume: [Select a .pdf file using the "Choose Files" button]
```
 - Click on the "Send" button to make the POST request and create a new user profile.

c).PUT Request:

 - Set the request type to PUT.

 - Enter the URL to update an existing user profile with its primary key (pk).

For example:http://localhost:8000/profiles/(pk)/

 - Go to the "Body" tab, select "form-data," and add the following key-value pairs to update the profile:
```bash
user_name: [Updated user name]

email: [Updated email address]

contact_details: [Updated contact details]

resume: [Select a new .pdf file using the "Choose Files" button to update the resume]
```
 - Click on the "Send" button to make the PUT request and update the user profile.

d).PATCH Request:

 - Set the request type to PATCH.

 - Enter the URL to partially update an existing user profile with its primary key (pk).

For example:http://localhost:8000/profiles/(pk)/

 - Go to the "Body" tab, select "form-data," and add the key-value pairs you want to update:
```bash
user_name: [Updated user name]

email: [Updated email address]

contact_details: [Updated contact details]

resume: [Select a new .pdf file using the "Choose Files" button to update the resume if needed]
```
 - Click on the "Send" button to make the PATCH request and partially update the user profile.

e).DELETE Request:

 - Set the request type to DELETE.

 - Enter the URL to delete an existing user profile with its primary key (pk).

For example:http://localhost:8000/profiles/(pk)/

 - Click on the "Send" button to make the DELETE request and delete the user profile.

Make sure your Django development server is running (python manage.py runserver) while testing these requests in Postman. Also, ensure you have added appropriate error handling in your views to handle invalid requests gracefully.
## Screenshots

 - POST Request-

![](https://github.com/abhisheksingh-17/Rest-Api/blob/main/Results/1.png?raw=true)

 - Database-
 ![](https://github.com/abhisheksingh-17/Rest-Api/blob/main/Results/2.png?raw=true)

  - GET Request-
  ![](https://github.com/abhisheksingh-17/Rest-Api/blob/main/Results/3.png?raw=true)

  - PUT Request-
  ![](https://github.com/abhisheksingh-17/Rest-Api/blob/main/Results/5.png?raw=true)

  - Database-
  ![](https://github.com/abhisheksingh-17/Rest-Api/blob/main/Results/6.png?raw=true)

  - PATCH Request-
  ![](https://github.com/abhisheksingh-17/Rest-Api/blob/main/Results/7.png?raw=true)

  - Database-
  ![](https://github.com/abhisheksingh-17/Rest-Api/blob/main/Results/8.png?raw=true)

  - DELETE Request-
  ![](https://github.com/abhisheksingh-17/Rest-Api/blob/main/Results/9.png?raw=true)

  - Database-
  ![](https://github.com/abhisheksingh-17/Rest-Api/blob/main/Results/10.png?raw=true)



## Future Scope

The Django User Profile Management API has several potential areas for future improvement and expansion. Here are some future scope ideas to enhance the functionality and usability of the API:

1.User Authentication Enhancements:

 - Implement OAuth or JWT (JSON Web Tokens) for more secure and scalable authentication.

 - Provide options for social media logins (e.g., Google, Facebook, Twitter) to improve user registration and login experience.

2.User Profile Customization:

 - Allow users to personalize their profiles with additional information, such as profile pictures, cover photos, and bio.

 - Implement user preferences and settings to let users customize their interaction with the platform.

3.User Profile Search and Filters:

 - Add search and filter functionality to allow users to find specific profiles based on criteria like skills, location, or experience.

 - Implement sorting options to arrange profiles based on different attributes (e.g., alphabetical order, experience level).

4.User Profile Ratings and Reviews:

 - Introduce a rating and review system where users can rate and provide feedback on other users' profiles.

 - Allow users to endorse or recommend others for specific skills or qualifications.

5.API Versioning:

 - Implement versioning for the API to support backward compatibility when introducing changes in the future.

6.Pagination and Performance Optimization:

 - Implement pagination to handle large data sets efficiently and improve API performance.

 - Optimize database queries and use caching to reduce response times for frequently accessed data.

7.User Interactions and Connections:

 - Allow users to connect or follow other profiles to build professional networks.

 - Implement messaging or notification systems for user-to-user communication.

8.Profile Privacy Settings:

 - Provide privacy settings for users to control the visibility of their profile information to the public or specific user groups.

9.User Activity Tracking:

 - Track user activity and provide insights into profile visits, interactions, and engagement.

10.Analytics and Reporting:

 - Implement analytics and reporting features to analyze user data and identify trends or patterns.

11.Internationalization and Localization:

 - Make the API multilingual by adding support for different languages and locales.

 - Allow users to choose their preferred language for the user interface.

12.Integration with External Services:

 - Integrate with third-party services, such as email providers, cloud storage, or applicant tracking systems, to enhance functionality.

13.Unit Testing and Test Coverage:

 - Increase test coverage by writing more unit tests to ensure code quality and reliability.

14.Documentation and API Documentation:

 - Improve documentation for the project, including code comments and explanatory notes.

 - Generate comprehensive API documentation using tools like Swagger/OpenAPI.

15.Security Enhancements:

 - Implement additional security measures, such as rate limiting, input validation, and access control.

These future scope ideas can help expand the functionality of the Django User Profile Management API and make it a more comprehensive and feature-rich solution for managing user profiles in a wide range of web applications and platforms. Remember to prioritize features based on user feedback, industry trends, and the specific needs of your project's target audience.
## Contribution & License

 - Users and developers are encouraged to contribute to the project by opening issues, suggesting new features, or submitting pull requests with improvements.

 - The project is licensed under the MIT License, allowing users to use, modify, and distribute the code with proper attribution and a copy of the license.

 - The code follows best practices for building a robust and secure Django REST API for user profile management. It can be further extended and adapted to fit various use cases and integrate with other systems as needed.