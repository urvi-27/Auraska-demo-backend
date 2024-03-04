from django.contrib import admin

from website_admin.models import About_executive_team, About_executive_team2, About_functional_team, About_technical_team1, About_technical_team2, Message, News, Service, User


# Register your models here.
admin.site.register(Service)
admin.site.register(About_executive_team)
admin.site.register(About_functional_team)
admin.site.register(About_technical_team1)
admin.site.register(About_technical_team2)
admin.site.register(About_executive_team2)
admin.site.register(News)
admin.site.register(User)
admin.site.register(Message)

