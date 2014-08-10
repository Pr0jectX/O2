# -*- coding: utf-8 -*-
from opos.models import Customers

from django.forms import ModelForm

class CustomerAddForm (ModelForm):
	class Meta:
		model = Customers
		fields = ['name', 'searchkey', 'id', 'card', 'maxdebt']

class CustomerForm (ModelForm):
	class Meta:
		model = Customers
		fields = ['name', 'card', 'maxdebt', 'id']
