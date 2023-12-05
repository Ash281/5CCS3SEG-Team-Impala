from django.contrib import admin

from .models import User, Team, Task
# Register your models here.
#admin.site.register(User)
admin.site.register(Team)
admin.site.register(Task)

from django.contrib.auth import get_user_model
# Register your models here.

admin.site.register(get_user_model())


