# Django Polls Application

Creator: Sirawich Direkwattanachai
## Description
Web application from the Django Tutorial 
* ref > https://docs.djangoproject.com/en/2.2/intro/

> Use **newest_question_list** instead of **lastest_question_list** in views.py, index.html etc.

## Requirements

The application requires
* Python 3.6 or newer
* Django 2.1.2 or newer
* Python add-on modules as in [requirements.txt](requirements.txt)

## Installation
Install application
* Clone git,use the following command in your cmd.

* > git clone https://github.com/magmagcup/django-polls.git

* Go into your directory which you clone the file to then run this command to migrate databases

* > python manage.py migrate 

Install require library in requirements.txt

* > pip install -r requirements.txt

## runserver

If you're going to runserver and access the application without "Bad Request (400)" respone you need to change default value of DEBUG in setting.py to be True (The defualt which I use is False).

according to 
```
> https://docs.djangoproject.com/en/2.2/ref/settings/
"Finally, if DEBUG is False, you also need to properly set the ALLOWED_HOSTS setting. Failing to do so will result in all requests being returned as “Bad Request (400)”
```

Go to directory which you clone the repository to, then run the command down below in cmd. 

>  python manage.py runserver {HOST}:{PORT}
 
 
## Connect to the server!
 
Open your browser then use this url.
 
 > http://{HOST}:{PORT}/polls/
 



