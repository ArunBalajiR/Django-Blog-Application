# Django-Blog-Application
![py35](https://img.shields.io/badge/Python-3.5-red.svg) 
![Django2.2](https://img.shields.io/badge/Django-2.2.0-green.svg)
[![](https://img.shields.io/badge/Powered%20by-@ArunBalajiR-blue.svg)](mailto:arunbalaji25062k@gmail.com)


## Screen Shots

![screenshot1](https://github.com/ArunBalajiR/Django-Blog-Application/blob/master/media/1.gif?raw=true)
![screenshot2](https://github.com/ArunBalajiR/Django-Blog-Application/blob/master/media/2.gif?raw=true)
![screenshot3](https://raw.githubusercontent.com/ArunBalajiR/Django-Blog-Application/master/media/3.jpg)
![screenshot4](https://raw.githubusercontent.com/ArunBalajiR/Django-Blog-Application/master/media/4.jpg)
![screenshot5](https://raw.githubusercontent.com/ArunBalajiR/Django-Blog-Application/master/media/5.jpg)

This is a demo project for practicing Django.
The idea was to build some basic blogging platform.

It was made using **Python 3.6** + **Django** and database is **SQLite**.
**Bootstrap** was used for styling.


There is a login and registration functionality included.

User has his own blog page, where he can add new blog posts. 
Every authenticated user can comment on posts made by other users.
Home page is paginated list of all posts.
Non-authenticated users can see all blog posts, but cannot add new posts or comment.

Clone This Project (Make Sure You Have Git Installed)

[Click Here](https://github.com/ArunBalajiR/Django-Blog-Application.git)

## Install Dependencies

```
pip install -r requirements.txt
```

Set Database (Make Sure you are in directory same as manage.py)
```
python manage.py makemigrations
python manage.py migrate
```
Create SuperUser 
```
python manage.py createsuperuser
```

After all these steps , you can start testing and developing this project. 

#### That's it! Happy Coding!

