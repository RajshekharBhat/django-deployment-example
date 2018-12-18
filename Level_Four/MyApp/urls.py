from django.urls import path
from . import views

#Template Tagging
app_name="MyApp"

urlpatterns=[
#path('mane/',views.mane_view,name="mane"),
path('other/',views.other_view,name="other"),
path('relative_templates/',views.relative_templates_view,name="relative"),
]
