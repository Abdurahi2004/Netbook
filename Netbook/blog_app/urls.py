from django.urls import path
from .views import Articles_View

urlpatterns=[
    path('', Articles_View.as_view(), name='articles')
]

