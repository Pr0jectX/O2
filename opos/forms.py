# -*- coding: utf-8 -*-
from opos.models import Customers

from django.forms import ModelForm

class CustomerForm (ModelForm):
	class Meta:
		model = Customers
		fields = ['name', 'card', 'id', 'searchkey', 'maxdebt']
