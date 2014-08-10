# -*- coding: utf-8 -*-
from opos.models import Customers

from django.forms import ModelForm

class CustomerAddForm (ModelForm):
	class Meta:
		model = Customers
		fields = ['name', 'searchkey', 'id', 'maxdebt', 'card']

class CustomerForm (ModelForm):
	class Meta:
		model = Customers
		fields = ['name', 'maxdebt', 'id', 'card']
