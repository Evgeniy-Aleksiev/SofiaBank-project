from django.urls import path

from sofia_bank.accounts.views import UserLoginView, UserRegisterView, ProfileDetailsView, \
    ProfileEditView, ProfileDeleteView, UserLogoutView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
    path('register/', UserRegisterView.as_view(), name='register'),
    #path('activate/<uidb64>/<token>/', activate_user, name='activate'),

    path('profile/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('profile/<int:pk>/edit/', ProfileEditView.as_view(), name='profile edit'),
    path('profile/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile delete'),
)