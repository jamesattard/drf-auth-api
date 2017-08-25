from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^products/$', views.ProductList.as_view()),
    url(r'^public-data/$', views.PublicData.as_view()),
    url(r'^protected-data/$', views.ProtectedData.as_view()),
]
