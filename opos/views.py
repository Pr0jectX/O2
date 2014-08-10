from django.shortcuts import render

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
def customeredit (request, customerpk):
	from opos.models import Customers
	from opos.forms import CustomerForm

	customer = get_object_or_404 (Customers, pk=customerpk)
	
	customeredit = CustomerForm (instance=customer)
	
	c = {}
	c['customer'] = customer
	c['customeredit'] = customeredit
	
	return render (request, "customeredit.html", c)
