from django.contrib import admin
from django.urls import include, path
from polls.views import IndexView as polls_page

urlpatterns = [
    path('', polls_page.as_view()),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
