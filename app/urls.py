from django.urls import URLPattern, path
from . import views
from .views import AllMessagesView, LoginView, MessageView


urlpatterns = [
    #path('',views.message,name='index'),
    path('message',MessageView.as_view(),name='message'),
    path('allmessages',AllMessagesView.as_view(),name='allmessages'),
    path('login',LoginView.as_view(),name='login')
]