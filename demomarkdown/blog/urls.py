
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('', BlogView.as_view(), name="BlogView"),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)