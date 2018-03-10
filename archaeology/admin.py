from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Artifact)
admin.site.register(Museum)
admin.site.register(Library)
admin.site.register(Books)
admin.site.register(Monument)
admin.site.register(Ticket)
admin.site.register(Excavations)
admin.site.register(Projects)
admin.site.register(Museum_ticket)
admin.site.register(Excavation_ticket)
admin.site.register(User_profile)
admin.site.register(message)
admin.site.register(Publication)
#admin.site.register(museum_feedback)
admin.site.register(Buy_museum_ticket)
admin.site.register(Buy_excavation_ticket)
admin.site.register(Buy_ticket)
admin.site.site_header = "Archaeology"