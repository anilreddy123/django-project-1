from django.conf.urls import include, url,patterns
import views

urlpatterns=[
    url(r'^$',views.User, name='User')
]


