from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:product_id>', views.detail, name='detail'),

]