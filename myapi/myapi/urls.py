from django.urls import path, include
from users.views import user_search

urlpatterns = [
    path('api/users/', user_search),
    path('', include('users.urls')),  # Add this line to include the users app URLs
]
