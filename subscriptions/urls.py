from django.urls import path
from subscriptions import views

urlpatterns = [
    path('subscriptions/', views.SubscribersList.as_view()),
    path('subscriptions/<int:pk>/', views.SubscribersDetail.as_view()),
    path('subscriptionmessages/', views.SubscribersMessageList.as_view()),
    path('subscriptionmessages/<int:pk>/', views.SubscribersMessageDetail.as_view()),
]