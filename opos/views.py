from django.shortcuts import render, redirect

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404

def is_staff (user):
	if user.is_staff or user.is_superuser:
		return True
	else:
		return False


@user_passes_test (is_staff)
def dashboard (request):
	c = {}
	return render (request, "dashboard.html", c)

@user_passes_test (is_staff)
def customers (request):
	from opos.models import Customers
	customers = Customers.objects.all ()
	c = {}
	c['customers'] = customers
	return render (request, "customers.html", c)

@user_passes_test (is_staff)
def customeradd (request):
	from opos.models import Customers
	from opos.forms import CustomerAddForm

	if request.method == 'POST':
		form = CustomerAddForm (request.POST)
		if form.is_valid ():
			form.save ()
			return redirect ('customers')
	c = {}
	c['customeredit'] = CustomerAddForm ()
	return render (request, "customer-add.html", c)

@user_passes_test (is_staff)
def customeredit (request, customerpk):
	from opos.models import Customers
	from opos.forms import CustomerForm
	from django import forms
	
	customer = get_object_or_404 (Customers, pk=customerpk)

	if request.method == 'POST':
		form = CustomerForm (request.POST, instance=customer)
		if form.is_valid ():
			form.save ()
			return redirect ('customers')
	else:
		form = CustomerForm (instance=customer)


	c = {}
	c['customer'] = customer
	form.fields['id'] = forms.CharField (widget=forms.widgets.HiddenInput())
	c['customeredit'] = form
	
	return render (request, "customer-edit.html", c)
