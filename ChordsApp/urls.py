from django.contrib import admin
from django.urls import include, path
from polls.views import index as polls_page

urlpatterns = [
    path('', polls_page),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
