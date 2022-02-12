from django.contrib import admin
from backend_app.models import *

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(UserProfile)
admin.site.register(MenuItem)
admin.site.register(DietTag)
admin.site.register(Event)
admin.site.register(EventUserBridge)


