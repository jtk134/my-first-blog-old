from django.urls import path
from . import views

"""
urlpatterns = [
path('', views.post_list, name='post_list'),
]
"""

urlpatterns = [
path('', views.yun_dongju, name='yun_dongju'),
]
