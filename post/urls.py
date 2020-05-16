from django.urls import include, path

# views
from .views import NewPostView

app_name='post'

urlpatterns = [
    path('new/', NewPostView.as_view(), name='new'), # new post
]