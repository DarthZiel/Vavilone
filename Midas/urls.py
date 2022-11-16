from django.urls import path
from .views import index, CreateIncomeRecord
urlpatterns = [
    path('', index),
    path('create/', CreateIncomeRecord.as_view())
]
