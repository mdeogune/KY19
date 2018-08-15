# Kashiyatra IIT (BHU) Website Source Code

Kashiyatra is socio-cultural festival of Indian Institute of Technology (B.H.U), Varanasi, India. 

Webiste: www.kashiyatra.org

## Stack:
 * Django 1.10
 * Angular 4.0

## Instuctions:

### To build angular code:

* `cd angular/user/`
* `ng build -op=../../templates/angular/user --prod -d /static/`

OR

* `cd angular/ca/`
* `ng build -op=../../templates/angular/ca/ --prod -d /static/`

### To install python dependencies:

* pip install -r requirements.txt

### To run Development server:

* python manage.py runserver


