from django.contrib import admin
from django.urls import include, path
from polls.views import IndexView as polls_page
from users import views as users_views

urlpatterns = [
    path('', polls_page.as_view()),
    path('register/', users_views.register, name='register'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
