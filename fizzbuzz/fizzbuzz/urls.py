from django.contrib import admin
from django.urls import path
from process_range import views

urlpatterns = [
    path('fizzbuzz',views.fizzy),
    path('admin/', admin.site.urls),
]
