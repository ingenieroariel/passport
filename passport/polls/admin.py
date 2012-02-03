from django.contrib import admin
from passport.polls.models import Poll

class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'pub_date')
    list_filter = ('pub_date',)

admin.site.register(Poll, PollAdmin)
