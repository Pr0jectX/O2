from django.contrib import admin

from opos.models import ( Customers )



class CustomerAdmin (admin.ModelAdmin):
	list_display = ('name', 'maxdebt', 'curdebt', )
	fields = ('name', 'card', 'id', 'searchkey', ('maxdebt', 'curdebt',), )
	readonly_fields = ('curdebt',)
	pass


admin.site.register (Customers, CustomerAdmin)
