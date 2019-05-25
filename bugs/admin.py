from django.contrib import admin
from .models import Bugs, BugComment

admin.site.register(Bugs)
admin.site.register(BugComment)
