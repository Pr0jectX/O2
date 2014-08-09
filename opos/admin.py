from django.contrib import admin

from opos.models import ( Customers )



class CustomerAdmin (admin.ModelAdmin):
	fields = ('name', 'card', ('maxdebt', 'curdebt',), )
	readonly_fields = ('curdebt',)


admin.site.register (Customers, CustomerAdmin)
