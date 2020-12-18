## Description
Online store project, based on `Django`.
In this project you will see the following technologies:
```
Django
Redis
Celery
JQuery
```
The payment method is also implemented here using the [Braintree](https://www.braintreepayments.com/) payment system

This site works in two languages - Russian and English
## Installation

Firslty you need to install package manager [pip](https://pip.pypa.io/en/stable/) an then use 
```pip install -r requirements.txt```
---

Open online_shop/settings.py and find next lines:
```python
BRAINTREE_MERCHANT_ID = ''
BRAINTREE_PUBLIC_KEY = ''
BRAINTREE_PRIVATE_KEY = ''
```
Enter here your sandbox braintree merchant id, public and private keys.
___
Then go to your environment folder --> lib/python3.8/site-packages/parler/fields.py
Find this line 
```python
from django.forms.forms import pretty_name
```
and raplace it with 
```python
from django.forms.utils import pretty_name
```

Then go to your environment folder --> lib/python3.8/site-packages/parler/forms.py
```python
from django.forms.forms import BoundField
```
and raplace it with 
```python
from django.forms import BoundField
```
## Usage

Enter the command in the terminal in the project folder
```
python manage.py runsslserver
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
