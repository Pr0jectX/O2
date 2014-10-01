from django.shortcuts import render, redirect

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from django import forms

from django.db.models import Max, Avg, Sum

from opos.models import Customers
from opos.forms import CustomerAddForm, CustomerForm


def is_staff (user):
	if user.is_staff or user.is_superuser:
		return True
	else:
		return False


@user_passes_test (is_staff)
def dashboard (request):

	c = {}

	c['curdebt'] = Customers.objects.all().aggregate(Sum('curdebt'))['curdebt__sum']
	c['maxdebt'] = Customers.objects.all().aggregate(Sum('maxdebt'))['maxdebt__sum']
	c['highestcurdebt'] = Customers.objects.all().aggregate(Max('curdebt'))['curdebt__max']



	from opos.sql import get_total_sale
	c['totalsale'] = get_total_sale ()[0]

	return render (request, "dashboard.html", c)


@user_passes_test (is_staff)
def customersales(request, customerpk):
	from opos.sql import get_customer_ticketlines

	customer = get_object_or_404 (Customers, pk=customerpk)

	ticketlines = get_customer_ticketlines (customer.pk)


	c = {}
	c['customer'] = customer
	c['ticketlines'] = ticketlines
	return render (request, "customer-sales.html", c)


@user_passes_test (is_staff)
def customers (request):
	customers = Customers.objects.all ()
	c = {}
	c['customers'] = customers
	return render (request, "customers.html", c)


@user_passes_test (is_staff)
def customeradd (request):

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



def selfdebtcheck (request):
	
	c = {}
	if request.method == 'POST':
		card = 'c' + request.POST.get("card")
		
		try:
			customer = Customers.objects.get (card=card)
		except:
			return render (request, "self-debtcheck.html", c)
		
		customer = get_object_or_404 (Customers, card=card)
		c['customer'] = customer
		c['leftdebt'] = customer.maxdebt - customer.curdebt
		return render (request, "self-debtshow.html", c)

	else:
		return render (request, "self-debtcheck.html", c)
