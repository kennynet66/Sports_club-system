from django.contrib import admin

#I have imported the models from the models.py
from .models import Member_details,Sports_details,Patron,Store

#I Register the model down here
admin.site.register(Member_details)
admin.site.register(Sports_details)
admin.site.register(Patron)
admin.site.register(Store)