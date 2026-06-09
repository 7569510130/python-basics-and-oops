Django – Complete Concepts with Detailed Examples
1. What is Django?
Django is a high-level Python web framework used to build web applications quickly and securely.
Real-world Example
Instagram (initially)
Pinterest
Educational portals
E-commerce websites
Job portals
Why Django?
Fast development
Built-in admin panel
Secure
Scalable
Follows MVT architecture
2. Django Architecture (MVT)
Django uses MVT (Model-View-Template) architecture.
Model
Handles database operations.
Python
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
View
Contains business logic.
Python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome")
Template
Displays data to users.
HTML
<h1>Welcome to Django</h1>
URL
Python
path('', views.home)
Flow:
User → URL → View → Model → Template → Browser
3. Project and App
Project
Entire website.
Bash
django-admin startproject myproject
App
Specific functionality.
Examples:
Authentication App
Student App
Employee App
Bash
python manage.py startapp student
4. Models
Models represent database tables.
Python
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
Database Table
id
name
salary
1
John
50000
Migration
Bash
python manage.py makemigrations
python manage.py migrate
5. ORM (Object Relational Mapping)
Converts Python code into SQL.
Create
Python
Employee.objects.create(
    name="Hari",
    salary=40000
)
Read
Python
Employee.objects.all()
Filter
Python
Employee.objects.filter(salary=40000)
Update
Python
emp = Employee.objects.get(id=1)
emp.salary = 50000
emp.save()
Delete
Python
emp.delete()
6. Views
Views process requests and return responses.
Function Based View
Python
def home(request):
    return HttpResponse("Hello Django")
Class Based View
Python
from django.views import View

class Home(View):
    def get(self, request):
        return HttpResponse("Hello")
7. URL Routing
Maps URLs to views.
Python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home)
]
Example

localhost:8000/about
Python
path('about/', views.about)
8. Templates
Templates generate HTML pages.
View
Python
def home(request):
    return render(request, 'home.html')
Template
HTML
<h1>Welcome {{ name }}</h1>
Context
Python
return render(request,'home.html',
             {'name':'Hari'})
Output:

Welcome Hari
9. Template Tags
For Loop
HTML
{% for student in students %}
    {{ student }}
{% endfor %}
If Condition
HTML
{% if age > 18 %}
Adult
{% endif %}
10. Static Files
Used for CSS, JS, Images.

static/
    css/
    js/
    images/
Example
HTML
<link rel="stylesheet"
href="{% static 'css/style.css' %}">
11. Forms
Collect user input.
forms.py
Python
from django import forms

class StudentForm(forms.Form):
    name = forms.CharField()
View
Python
form = StudentForm()
Template
HTML
{{ form }}
12. Model Forms
Connect forms directly with models.
Python
class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
13. Admin Panel
Django provides built-in admin.
Create Admin
Bash
python manage.py createsuperuser
Register Model
Python
from django.contrib import admin
from .models import Student

admin.site.register(Student)
Admin URL:

localhost:8000/admin
14. Authentication
User Registration
Python
User.objects.create_user(
    username="hari",
    password="123"
)
Login
Python
from django.contrib.auth import authenticate

user = authenticate(
    username="hari",
    password="123"
)
Logout
Python
logout(request)
15. Sessions
Store user information.
Python
request.session['name'] = 'Hari'
Retrieve
Python
request.session['name']
16. Cookies
Stored in browser.
Python
response.set_cookie(
    'username',
    'Hari'
)
Get Cookie
Python
request.COOKIES.get('username')
17. Middleware
Processes requests before views.
Example
Python
class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
18. Relationships
One-to-Many
Department → Employees
Python
class Department(models.Model):
    name=models.CharField(max_length=100)

class Employee(models.Model):
    department=models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
One-to-One
User → Profile
Python
class Profile(models.Model):
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
Many-to-Many
Student ↔ Course
Python
class Course(models.Model):
    name=models.CharField(max_length=100)

class Student(models.Model):
    courses=models.ManyToManyField(Course)
19. QuerySets
All Records
Python
Student.objects.all()
First Record
Python
Student.objects.first()
Count
Python
Student.objects.count()
Order By
Python
Student.objects.order_by('name')
20. File Uploads
Model
Python
class Document(models.Model):
    file=models.FileField(
        upload_to='files/'
    )
Template
HTML
<form enctype="multipart/form-data">
21. Pagination
Used for large datasets.
Python
from django.core.paginator import Paginator

paginator = Paginator(data,5)
Shows 5 records per page.
22. Signals
Automatically execute actions.
Python
from django.db.models.signals import post_save
Example:
Send welcome email after user registration.
23. Django Messages Framework
Python
messages.success(
    request,
    "Data Saved Successfully"
)
Template:
HTML
{{ messages }}
24. Caching
Improves performance.
Python
from django.views.decorators.cache import cache_page

@cache_page(60)
def home(request):
    pass
60 seconds cache.
25. Django REST Framework (DRF)
Used for APIs.
Serializer
Python
class StudentSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Student
        fields = '__all__'
API View
Python
class StudentAPI(APIView):

    def get(self, request):
        students = Student.objects.all()
Response JSON:
JSON
{
  "id":1,
  "name":"Hari"
}
26. Security Features
CSRF Protection
HTML
{% csrf_token %}
SQL Injection Protection
Handled by ORM.
XSS Protection
Templates escape dangerous HTML automatically.
27. Deployment
Popular servers:
Gunicorn
Nginx
Apache
Commands:
Bash
pip freeze > requirements.txt
Bash
python manage.py collectstatic
28. Django Interview Flow Project Example
Student Management System
Features:
Login
Registration
Add Student
Update Student
Delete Student
Search Student
Pagination
Admin Panel
REST API
File Upload
Concepts Used:
Models
Views
Templates
Forms
Authentication
ORM
CRUD Operations
Middleware
Sessions
Deployment
Learning Order
Python Basics
HTML/CSS
Django Setup
MVT Architecture
URLs
Views
Templates
Models
ORM
Forms
Authentication
Relationships
CRUD Project
REST API (DRF)
Deployment
Mastering these topics covers most Django fresher and intermediate interview questions and enables you to build real-world applications such as e-commerce sites, job portals, ERP systems, and learning management systems.