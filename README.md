Plan your tasks
====================

Installation:
--------
##### 1. Make sure you have: python2, pip, virtualenv, git.
##### 2. Clone the repository:
```
$ git clone https://github.com/radziejewskikamil/plan_your_tasks.git
```
##### 3. Create a new virtualenv into cloned repository:
```
$ cd plan_your_tasks
$ virtualenv env
```
##### 4. Activate virtualenv:
```
$ source env/bin/activate
```
##### 5. Install django 1.8.6:
```
$ pip install -r requirements.txt
```
##### 6. Sync database
```
$ python manage.py syncdb
```
##### 7. Run app:
```
$ python manage.py runserver
```

Tests:
--------
```
$ python manage.py test
```
