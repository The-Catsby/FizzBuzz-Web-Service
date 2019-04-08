# FizzBuzz-Web-Service
A web-service that calculates and returns FizzBuzz for a range

#### Requrements
- Python 3.7.2
- Django 2.2

#### Run the server
``` 
> python manage.py runserver 
...
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
#### Send request
```
> curl "http://127.0.0.1:8000/fizzbuzz?begin=1&end=15"
1 
2 
Fizz 
4 
Buzz 
Fizz 
7 
8 
Fizz 
Buzz 
11 
Fizz 
13 
14 
FizzBuzz 
```
