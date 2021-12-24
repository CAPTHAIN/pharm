from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('city/<int:city_pk>/', PointsPageView.as_view(), name='city'),
    path('city/<int:city_pk>/point/<int:point_pk>', MedicinePageView.as_view(), name='points'),
]