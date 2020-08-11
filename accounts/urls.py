from django.urls import path


from .views import ProfileView,ProfileDetailView



urlpatterns = [
    path('',ProfileView.as_view()),
    path('<slug:name>/',ProfileDetailView.as_view()),

]