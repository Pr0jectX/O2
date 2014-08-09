class oposRouter (object):
	
	def db_for_read (self, model, **hints):
		if model._meta.app_label == 'opos':
			return 'opos'

	def db_for_write (self, model, **hints):
		if model._meta.app_label == 'opos':
			return 'opos'
	
	def allow_relation (self, obj1, obj2, **hints):
		if obj1._meta.app_label == 'opos' or obj2._meta.app_label == 'opos':
			return True

	def allow_syncdb (self, db, model):
		if model._meta.app_label == 'opos':
			return False
		else:
			return True
