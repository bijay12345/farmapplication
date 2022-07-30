from django.contrib import admin
from .models import Medicine,Cow,Milk,CowInfo

admin.site.register(Cow)
admin.site.register(Medicine)
admin.site.register(Milk)
admin.site.register(CowInfo)
