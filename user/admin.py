from django.contrib import admin
from user.models import *
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Stories)
