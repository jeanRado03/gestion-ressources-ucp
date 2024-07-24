from django.urls import path
from .views import UserCreate, CustomTokenObtainPairView

urlpatterns = [
    path("register/", UserCreate.as_view()),
    path('api/token/custom/', CustomTokenObtainPairView.as_view(), name='token_obtain_custom'),
]