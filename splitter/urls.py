# splitter/urls.py
from django.urls import path
from .views import SKUSplitterView

urlpatterns = [
    path('api/split-by-sku/', SKUSplitterView.as_view(), name='split-by-sku'),
]