# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

from compositekey import db

class Applications(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255) # Field name made lowercase.
    version = models.CharField(db_column='VERSION', max_length=255) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'APPLICATIONS'

class Attribute(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ATTRIBUTE'

class Attributeinstance(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    attributesetinstance = models.ForeignKey('Attributesetinstance', db_column='ATTRIBUTESETINSTANCE_ID') # Field name made lowercase.
    attribute = models.ForeignKey(Attribute, db_column='ATTRIBUTE_ID') # Field name made lowercase.
    value = models.CharField(db_column='VALUE', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ATTRIBUTEINSTANCE'

class Attributeset(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ATTRIBUTESET'

class Attributesetinstance(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    attributeset = models.ForeignKey(Attributeset, db_column='ATTRIBUTESET_ID') # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ATTRIBUTESETINSTANCE'

class Attributeuse(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    attributeset = models.ForeignKey(Attributeset, db_column='ATTRIBUTESET_ID') # Field name made lowercase.
    attribute = models.ForeignKey(Attribute, db_column='ATTRIBUTE_ID') # Field name made lowercase.
    lineno = models.IntegerField(db_column='LINENO', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ATTRIBUTEUSE'

class Attributevalue(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    attribute = models.ForeignKey(Attribute, db_column='ATTRIBUTE_ID') # Field name made lowercase.
    value = models.CharField(db_column='VALUE', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ATTRIBUTEVALUE'

class Breaks(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255) # Field name made lowercase.
    visible = models.IntegerField(db_column='VISIBLE') # Field name made lowercase.
    notes = models.CharField(db_column='NOTES', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'BREAKS'

class Categories(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255) # Field name made lowercase.
    parentid = models.ForeignKey('self', db_column='PARENTID', blank=True, null=True) # Field name made lowercase.
    image = models.TextField(db_column='IMAGE', blank=True) # Field name made lowercase.
    texttip = models.CharField(db_column='TEXTTIP', max_length=255, blank=True) # Field name made lowercase.
    catshowname = models.IntegerField(db_column='CATSHOWNAME') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'CATEGORIES'

class Closedcash(models.Model):
    money = models.CharField(db_column='MONEY', primary_key=True, max_length=255) # Field name made lowercase.
    host = models.CharField(db_column='HOST', max_length=255) # Field name made lowercase.
    hostsequence = models.IntegerField(db_column='HOSTSEQUENCE') # Field name made lowercase.
    datestart = models.DateTimeField(db_column='DATESTART') # Field name made lowercase.
    dateend = models.DateTimeField(db_column='DATEEND', blank=True, null=True) # Field name made lowercase.
    nosales = models.IntegerField(db_column='NOSALES') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'CLOSEDCASH'

class Csvimport(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    rownumber = models.CharField(db_column='ROWNUMBER', max_length=255, blank=True) # Field name made lowercase.
    csverror = models.CharField(db_column='CSVERROR', max_length=255, blank=True) # Field name made lowercase.
    reference = models.CharField(db_column='REFERENCE', max_length=1024, blank=True) # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=1024, blank=True) # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=1024, blank=True) # Field name made lowercase.
    pricebuy = models.FloatField(db_column='PRICEBUY', blank=True, null=True) # Field name made lowercase.
    pricesell = models.FloatField(db_column='PRICESELL', blank=True, null=True) # Field name made lowercase.
    previousbuy = models.FloatField(db_column='PREVIOUSBUY', blank=True, null=True) # Field name made lowercase.
    previoussell = models.FloatField(db_column='PREVIOUSSELL', blank=True, null=True) # Field name made lowercase.
    category = models.CharField(db_column='CATEGORY', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'CSVIMPORT'

class Customers(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    searchkey = models.CharField(db_column='SEARCHKEY', unique=True, max_length=255) # Field name made lowercase.
    taxid = models.CharField(db_column='TAXID', max_length=255, blank=True) # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255) # Field name made lowercase.
    taxcategory = models.ForeignKey('Taxcustcategories', db_column='TAXCATEGORY', blank=True, null=True) # Field name made lowercase.
    card = models.CharField(db_column='CARD', max_length=255, blank=True) # Field name made lowercase.
    maxdebt = models.FloatField(db_column='MAXDEBT') # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=255, blank=True) # Field name made lowercase.
    address2 = models.CharField(db_column='ADDRESS2', max_length=255, blank=True) # Field name made lowercase.
    postal = models.CharField(db_column='POSTAL', max_length=255, blank=True) # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=255, blank=True) # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=255, blank=True) # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=255, blank=True) # Field name made lowercase.
    firstname = models.CharField(db_column='FIRSTNAME', max_length=255, blank=True) # Field name made lowercase.
    lastname = models.CharField(db_column='LASTNAME', max_length=255, blank=True) # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=255, blank=True) # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=255, blank=True) # Field name made lowercase.
    phone2 = models.CharField(db_column='PHONE2', max_length=255, blank=True) # Field name made lowercase.
    fax = models.CharField(db_column='FAX', max_length=255, blank=True) # Field name made lowercase.
    notes = models.CharField(db_column='NOTES', max_length=255, blank=True) # Field name made lowercase.
    visible = models.BooleanField(default=True, db_column='VISIBLE') # Field name made lowercase. This field type is a guess.
    curdate = models.DateTimeField(db_column='CURDATE', blank=True, null=True) # Field name made lowercase.
    curdebt = models.FloatField(db_column='CURDEBT', blank=True, null=True) # Field name made lowercase.
    image = models.TextField(db_column='IMAGE', blank=True) # Field name made lowercase.

    def __unicode__ (self):
        return self.name
    class Meta:
        managed = False
        db_table = 'CUSTOMERS'
        verbose_name = 'Customer'


class Draweropened(models.Model):
    opendate = models.DateTimeField(db_column='OPENDATE') # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True) # Field name made lowercase.
    ticketid = models.CharField(db_column='TICKETID', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'DRAWEROPENED'

class Floors(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255) # Field name made lowercase.
    image = models.TextField(db_column='IMAGE', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'FLOORS'

class Leaves(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    pplid = models.ForeignKey('People', db_column='PPLID') # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255) # Field name made lowercase.
    startdate = models.DateTimeField(db_column='STARTDATE') # Field name made lowercase.
    enddate = models.DateTimeField(db_column='ENDDATE') # Field name made lowercase.
    notes = models.CharField(db_column='NOTES', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'LEAVES'

class Lineremoved(models.Model):
    removeddate = models.DateTimeField(db_column='REMOVEDDATE') # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True) # Field name made lowercase.
    ticketid = models.CharField(db_column='TICKETID', max_length=255, blank=True) # Field name made lowercase.
    productid = models.CharField(db_column='PRODUCTID', max_length=255, blank=True) # Field name made lowercase.
    productname = models.CharField(db_column='PRODUCTNAME', max_length=255, blank=True) # Field name made lowercase.
    units = models.FloatField(db_column='UNITS') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'LINEREMOVED'

class Locations(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255) # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'LOCATIONS'

class Moorers(models.Model):
    vesselname = models.CharField(db_column='VESSELNAME', max_length=255, blank=True) # Field name made lowercase.
    size = models.IntegerField(db_column='SIZE', blank=True, null=True) # Field name made lowercase.
    days = models.IntegerField(db_column='DAYS', blank=True, null=True) # Field name made lowercase.
    power = models.TextField(db_column='POWER') # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'MOORERS'

class Payments(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    receipt = models.ForeignKey('Receipts', db_column='RECEIPT') # Field name made lowercase.
    payment = models.CharField(db_column='PAYMENT', max_length=255) # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL') # Field name made lowercase.
    transid = models.CharField(db_column='TRANSID', max_length=255, blank=True) # Field name made lowercase.
    returnmsg = models.TextField(db_column='RETURNMSG', blank=True) # Field name made lowercase.
    notes = models.CharField(db_column='NOTES', max_length=255, blank=True) # Field name made lowercase.
    tendered = models.FloatField(db_column='TENDERED', blank=True, null=True) # Field name made lowercase.
    cardname = models.CharField(db_column='CARDNAME', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'PAYMENTS'

class People(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255) # Field name made lowercase.
    apppassword = models.CharField(db_column='APPPASSWORD', max_length=255, blank=True) # Field name made lowercase.
    card = models.CharField(db_column='CARD', max_length=255, blank=True) # Field name made lowercase.
    role = models.ForeignKey('Roles', db_column='ROLE') # Field name made lowercase.
    visible = models.TextField(db_column='VISIBLE') # Field name made lowercase. This field type is a guess.
    image = models.TextField(db_column='IMAGE', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'PEOPLE'

class PickupNumber(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'PICKUP_NUMBER'

class Places(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255) # Field name made lowercase.
    x = models.IntegerField(db_column='X') # Field name made lowercase.
    y = models.IntegerField(db_column='Y') # Field name made lowercase.
    floor = models.ForeignKey(Floors, db_column='FLOOR') # Field name made lowercase.
    customer = models.CharField(db_column='CUSTOMER', max_length=255, blank=True) # Field name made lowercase.
    waiter = models.CharField(db_column='WAITER', max_length=255, blank=True) # Field name made lowercase.
    ticketid = models.CharField(db_column='TICKETID', max_length=255, blank=True) # Field name made lowercase.
    tablemoved = models.IntegerField(db_column='TABLEMOVED') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'PLACES'

class Products(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    reference = models.CharField(db_column='REFERENCE', unique=True, max_length=255) # Field name made lowercase.
    code = models.CharField(db_column='CODE', unique=True, max_length=255) # Field name made lowercase.
    codetype = models.CharField(db_column='CODETYPE', max_length=255, blank=True) # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255) # Field name made lowercase.
    pricebuy = models.FloatField(db_column='PRICEBUY') # Field name made lowercase.
    pricesell = models.FloatField(db_column='PRICESELL') # Field name made lowercase.
    category = models.ForeignKey(Categories, db_column='CATEGORY') # Field name made lowercase.
    taxcat = models.ForeignKey('Taxcategories', db_column='TAXCAT') # Field name made lowercase.
    attributeset = models.ForeignKey(Attributeset, db_column='ATTRIBUTESET_ID', blank=True, null=True) # Field name made lowercase.
    stockcost = models.FloatField(db_column='STOCKCOST', blank=True, null=True) # Field name made lowercase.
    stockvolume = models.FloatField(db_column='STOCKVOLUME', blank=True, null=True) # Field name made lowercase.
    image = models.TextField(db_column='IMAGE', blank=True) # Field name made lowercase.
    iscom = models.TextField(db_column='ISCOM') # Field name made lowercase. This field type is a guess.
    isscale = models.TextField(db_column='ISSCALE') # Field name made lowercase. This field type is a guess.
    iskitchen = models.TextField(db_column='ISKITCHEN') # Field name made lowercase. This field type is a guess.
    printkb = models.TextField(db_column='PRINTKB') # Field name made lowercase. This field type is a guess.
    sendstatus = models.TextField(db_column='SENDSTATUS') # Field name made lowercase. This field type is a guess.
    isservice = models.TextField(db_column='ISSERVICE') # Field name made lowercase. This field type is a guess.
    attributes = models.TextField(db_column='ATTRIBUTES', blank=True) # Field name made lowercase.
    display = models.CharField(db_column='DISPLAY', max_length=255, blank=True) # Field name made lowercase.
    isvprice = models.IntegerField(db_column='ISVPRICE') # Field name made lowercase.
    isverpatrib = models.IntegerField(db_column='ISVERPATRIB') # Field name made lowercase.
    texttip = models.CharField(db_column='TEXTTIP', max_length=255, blank=True) # Field name made lowercase.
    warranty = models.IntegerField(db_column='WARRANTY') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'PRODUCTS'

class ProductsCat(models.Model):
    product = models.ForeignKey(Products, db_column='PRODUCT', primary_key=True) # Field name made lowercase.
    catorder = models.IntegerField(db_column='CATORDER', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'PRODUCTS_CAT'

class ProductsCom(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    product = models.ForeignKey(Products, db_column='PRODUCT', related_name='productscom_rel') # Field name made lowercase.
    product2 = models.ForeignKey(Products, db_column='PRODUCT2', related_name='productscom_rel2') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'PRODUCTS_COM'

class Receipts(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    money = models.ForeignKey(Closedcash, db_column='MONEY') # Field name made lowercase.
    datenew = models.DateTimeField(db_column='DATENEW') # Field name made lowercase.
    attributes = models.TextField(db_column='ATTRIBUTES', blank=True) # Field name made lowercase.
    person = models.CharField(db_column='PERSON', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'RECEIPTS'

class Reservations(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    created = models.DateTimeField(db_column='CREATED') # Field name made lowercase.
    datenew = models.DateTimeField(db_column='DATENEW') # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=255) # Field name made lowercase.
    chairs = models.IntegerField(db_column='CHAIRS') # Field name made lowercase.
    isdone = models.TextField(db_column='ISDONE') # Field name made lowercase. This field type is a guess.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'RESERVATIONS'

class ReservationCustomers(models.Model):
    id = models.ForeignKey(Reservations, db_column='ID', primary_key=True) # Field name made lowercase.
    customer = models.ForeignKey(Customers, db_column='CUSTOMER') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'RESERVATION_CUSTOMERS'

class Resources(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255) # Field name made lowercase.
    restype = models.IntegerField(db_column='RESTYPE') # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'RESOURCES'

class Roles(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255) # Field name made lowercase.
    permissions = models.TextField(db_column='PERMISSIONS', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ROLES'

class Sharedtickets(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255) # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True) # Field name made lowercase.
    appuser = models.CharField(db_column='APPUSER', max_length=255, blank=True) # Field name made lowercase.
    pickupid = models.IntegerField(db_column='PICKUPID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'SHAREDTICKETS'

class Shifts(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    startshift = models.DateTimeField(db_column='STARTSHIFT') # Field name made lowercase.
    endshift = models.DateTimeField(db_column='ENDSHIFT', blank=True, null=True) # Field name made lowercase.
    pplid = models.CharField(db_column='PPLID', max_length=255) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'SHIFTS'

class ShiftBreaks(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    shiftid = models.ForeignKey(Shifts, db_column='SHIFTID') # Field name made lowercase.
    breakid = models.ForeignKey(Breaks, db_column='BREAKID') # Field name made lowercase.
    starttime = models.DateTimeField(db_column='STARTTIME') # Field name made lowercase.
    endtime = models.DateTimeField(db_column='ENDTIME') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'SHIFT_BREAKS'

class Stockcurrent(models.Model):
    location = models.ForeignKey(Locations, db_column='LOCATION') # Field name made lowercase.
    product = models.ForeignKey(Products, db_column='PRODUCT') # Field name made lowercase.
    attributesetinstance = models.ForeignKey(Attributesetinstance, db_column='ATTRIBUTESETINSTANCE_ID', blank=True, null=True) # Field name made lowercase.
    units = models.FloatField(db_column='UNITS') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'STOCKCURRENT'

class Stockdiary(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    datenew = models.DateTimeField(db_column='DATENEW') # Field name made lowercase.
    reason = models.IntegerField(db_column='REASON') # Field name made lowercase.
    location = models.ForeignKey(Locations, db_column='LOCATION') # Field name made lowercase.
    product = models.ForeignKey(Products, db_column='PRODUCT') # Field name made lowercase.
    attributesetinstance = models.ForeignKey(Attributesetinstance, db_column='ATTRIBUTESETINSTANCE_ID', blank=True, null=True) # Field name made lowercase.
    units = models.FloatField(db_column='UNITS') # Field name made lowercase.
    price = models.FloatField(db_column='PRICE') # Field name made lowercase.
    appuser = models.CharField(db_column='APPUSER', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'STOCKDIARY'

class Stocklevel(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    location = models.ForeignKey(Locations, db_column='LOCATION') # Field name made lowercase.
    product = models.ForeignKey(Products, db_column='PRODUCT') # Field name made lowercase.
    stocksecurity = models.FloatField(db_column='STOCKSECURITY', blank=True, null=True) # Field name made lowercase.
    stockmaximum = models.FloatField(db_column='STOCKMAXIMUM', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'STOCKLEVEL'

class Taxcategories(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'TAXCATEGORIES'

class Taxcustcategories(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'TAXCUSTCATEGORIES'

class Taxes(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255) # Field name made lowercase.
    category = models.ForeignKey(Taxcategories, db_column='CATEGORY') # Field name made lowercase.
    custcategory = models.ForeignKey(Taxcustcategories, db_column='CUSTCATEGORY', blank=True, null=True) # Field name made lowercase.
    parentid = models.ForeignKey('self', db_column='PARENTID', blank=True, null=True) # Field name made lowercase.
    rate = models.FloatField(db_column='RATE') # Field name made lowercase.
    ratecascade = models.TextField(db_column='RATECASCADE') # Field name made lowercase. This field type is a guess.
    rateorder = models.IntegerField(db_column='RATEORDER', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'TAXES'

class Taxlines(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    receipt = models.ForeignKey(Receipts, db_column='RECEIPT') # Field name made lowercase.
    taxid = models.ForeignKey(Taxes, db_column='TAXID') # Field name made lowercase.
    base = models.FloatField(db_column='BASE') # Field name made lowercase.
    amount = models.FloatField(db_column='AMOUNT') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'TAXLINES'

class Thirdparties(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) # Field name made lowercase.
    cif = models.CharField(db_column='CIF', unique=True, max_length=255) # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255) # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=255, blank=True) # Field name made lowercase.
    contactcomm = models.CharField(db_column='CONTACTCOMM', max_length=255, blank=True) # Field name made lowercase.
    contactfact = models.CharField(db_column='CONTACTFACT', max_length=255, blank=True) # Field name made lowercase.
    payrule = models.CharField(db_column='PAYRULE', max_length=255, blank=True) # Field name made lowercase.
    faxnumber = models.CharField(db_column='FAXNUMBER', max_length=255, blank=True) # Field name made lowercase.
    phonenumber = models.CharField(db_column='PHONENUMBER', max_length=255, blank=True) # Field name made lowercase.
    mobilenumber = models.CharField(db_column='MOBILENUMBER', max_length=255, blank=True) # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=255, blank=True) # Field name made lowercase.
    webpage = models.CharField(db_column='WEBPAGE', max_length=255, blank=True) # Field name made lowercase.
    notes = models.CharField(db_column='NOTES', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'THIRDPARTIES'

class Ticketlines(models.Model):
    ticket = models.ForeignKey('Tickets', db_column='TICKET') # Field name made lowercase.
    line = models.IntegerField(db_column='LINE') # Field name made lowercase.
    product = models.ForeignKey(Products, db_column='PRODUCT', blank=True, null=True) # Field name made lowercase.
    attributesetinstance = models.ForeignKey(Attributesetinstance, db_column='ATTRIBUTESETINSTANCE_ID', blank=True, null=True) # Field name made lowercase.
    units = models.FloatField(db_column='UNITS') # Field name made lowercase.
    price = models.FloatField(db_column='PRICE') # Field name made lowercase.
    taxid = models.ForeignKey(Taxes, db_column='TAXID') # Field name made lowercase.
    attributes = models.TextField(db_column='ATTRIBUTES', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'TICKETLINES'

class Tickets(models.Model):
    id = models.ForeignKey(Receipts, db_column='ID', primary_key=True) # Field name made lowercase.
    tickettype = models.IntegerField(db_column='TICKETTYPE') # Field name made lowercase.
    ticketid = models.IntegerField(db_column='TICKETID') # Field name made lowercase.
    person = models.ForeignKey(People, db_column='PERSON') # Field name made lowercase.
    customer = models.ForeignKey(Customers, db_column='CUSTOMER', blank=True, null=True) # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'TICKETS'

class Ticketsnum(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'TICKETSNUM'

class TicketsnumPayment(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'TICKETSNUM_PAYMENT'

class TicketsnumRefund(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'TICKETSNUM_REFUND'

